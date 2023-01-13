import os

import pygame as pg

from ..database.character_db import CharacterDB
from ..tools import COLORS, Obj, draw_texts
from paths import FOLDERS, IMG_LOAD, IMG_MENU, IMG_NEW_GAME

from .settings import title_load

DISPLAY_NONE = int(os.getenv("DISPLAY_NONE", "-1080"))


class Load:
    is_active = True
    db = CharacterDB()

    def __init__(self, *groups):

        self.main_screen = pg.display.get_surface()
        self.box = []
        self.icon_del = []
        self.icon_add = []

        rect = [
            (29, 74),
            (305, 74),
            (581, 74),
            (29, 389),
            (305, 389),
            (581, 389),
            (29, 703),
            (305, 703),
            (581, 703),
        ]

        self.bg = Obj(IMG_LOAD["bg"], 0, 0, *groups)

        for pos in rect:
            self.box.append(Obj(IMG_LOAD["box"], pos[0], pos[1], *groups))
            self.icon_del.append(
                Obj(IMG_LOAD["del"], DISPLAY_NONE, DISPLAY_NONE, *groups)
            )
            self.icon_add.append(
                Obj(IMG_NEW_GAME["add"], DISPLAY_NONE, DISPLAY_NONE, *groups)
            )

        self.return_icon = Obj(IMG_MENU["return"], 100, 970, *groups)

    def _draw_records(self) -> None:

        records = self.db.get_all()
        black = COLORS["BLACK"]
        include_attrs = ["name", "level", "ethnicity", "classe", "location"]

        for index, name in enumerate(records):

            character = records[name]

            self.box[index].image = pg.image.load(
                "{}{}".format(FOLDERS["classes"], character["sprite"])
            )

            pos_x, pos_y = self.box[index].rect.bottomleft

            for attr in include_attrs:
                att = attr.title() if attr != "location" else ""

                draw_texts(
                    screen=self.main_screen,
                    text="> {} - {}".format(att, character[attr]),
                    pos_x=pos_x,
                    pos_y=pos_y + 10,
                    color=black,
                )
                pos_y += 20

            self.icon_del[index].rect.topleft = (pos_x, pos_y + 20)
            self.icon_add[index].rect.topleft = (pos_x + 85, pos_y + 20)

    def _delete(self, pos_mouse) -> None:

        records = self.db.get_all()

        for index, name in enumerate(records.keys()):

            if self.icon_del[index].rect.collidepoint(pos_mouse):
                self.db.delete(name)

                self.icon_add[index].rect.y = DISPLAY_NONE
                self.icon_del[index].rect.y = DISPLAY_NONE
                self.box[index].image = pg.image.load(IMG_LOAD["box"])

    def _load(self, pos_mouse) -> None:

        records = self.db.get_all()

        for icon in range(len(self.icon_add)):
            if self.icon_add[icon].rect.collidepoint(pos_mouse):
                os.environ["EVENTS"] = "loading"
                os.environ["CHAR_NAME"] = list(records.keys())[icon]

    def _return_menu(self, pos_mouse) -> None:
        if self.return_icon.rect.collidepoint(pos_mouse):
            self.is_active = False

    def _get_mouse_events_to_show_interactive(self, pos_mouse) -> None:

        for index in range(len(self.icon_del)):

            if self.icon_del[index].rect.collidepoint(pos_mouse):
                img_del = "select_del"
            else:
                img_del = "del"

            if self.icon_add[index].rect.collidepoint(pos_mouse):
                img_add = "select_add"
            else:
                img_add = "add"

            self.icon_del[index].image = pg.image.load(IMG_LOAD[img_del])
            self.icon_add[index].image = pg.image.load(IMG_LOAD[img_add])

        img_return = "return"

        if self.return_icon.rect.collidepoint(pos_mouse):
            img_return = "select_return"

        self.return_icon.image = pg.image.load(IMG_MENU[img_return])

    def events(self, event, pos_mouse):
        if event.type == pg.MOUSEBUTTONDOWN:
            self._delete(pos_mouse)
            self._load(pos_mouse)
            self._return_menu(pos_mouse)

        self._get_mouse_events_to_show_interactive(pos_mouse)

    def update(self):

        self._draw_records()

        draw_texts(
            screen=self.main_screen,
            text=str(title_load),
            pos_x=300 + len(title_load),
            pos_y=15,
            size=27,
        )
