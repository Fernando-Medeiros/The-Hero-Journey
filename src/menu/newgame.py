import os
from time import sleep

import pygame as pg

from paths import *

from ..character.settings.settings import INFO_HERALDRY, INFO_SKILLS, LIST_CLASSES
from ..database.character_db import CharacterDB
from ..tools import COLORS, Obj, draw_rect, draw_texts
from .settings import INFO_MAX_RECORDS, list_ethnicities, title_new_game

DISPLAY_NONE = int(os.getenv("DISPLAY_NONE", "-1080"))
MAX_RECORDS = int(os.getenv("MAX_RECORDS", "9"))
MIN_CHARACTERS_NAME = int(os.getenv("MIN_CHARACTERS_NAME", "3"))
MAX_CHARACTERS_NAME = int(os.getenv("MAX_CHARACTERS_NAME", "20"))


class NewGame:
    ETHNICITY = ""
    CLASSE = ""
    NAME = ""

    is_active = True
    block = False
    inbox = False

    db = CharacterDB()

    def __init__(self, *groups):

        self.main_screen = pg.display.get_surface()

        self.ethnicity = []
        self.class_ = []

        self.pos_y_e, self.pos_y_c = 70, 560

        self.bg = Obj(IMG_NEW_GAME["bg"], 0, 0, *groups)

        self.boxes = [
            Obj(IMG_NEW_GAME["HERALDRY_BOX"], 0, 111, *groups),
            Obj(IMG_NEW_GAME["BOX_STATUS"], 8, 632, *groups),
            pg.Rect(183, 942, 376, 35),
        ]
        self.interactive_ = [
            Obj(IMG_NEW_GAME["select"], DISPLAY_NONE, self.pos_y_e, *groups),
            Obj(IMG_NEW_GAME["select"], DISPLAY_NONE, self.pos_y_c, *groups),
            Obj(IMG_NEW_GAME["interactive"], DISPLAY_NONE, DISPLAY_NONE, *groups),
        ]
        self.max_records = Obj(IMG_NEW_GAME["max_records"], 0, DISPLAY_NONE, *groups)
        self.add_icon = Obj(IMG_NEW_GAME["add"], 559, 942, *groups)
        self.return_icon = Obj(IMG_MENU["return"], 100, 942, *groups)

        self.index_list_class = LIST_CLASSES[0]

    def _select_guides(self, pos_mouse) -> None:
        self._list_ethnicity_and_classes(
            self.ethnicity[0], "dark-elf", "info_dark", pos_mouse
        )
        self._list_ethnicity_and_classes(
            self.ethnicity[1], "forest-elf", "info_forest", pos_mouse
        )
        self._list_ethnicity_and_classes(
            self.ethnicity[2], "grey-elf", "info_grey", pos_mouse
        )

    def _return_menu(self, pos_mouse) -> None:
        if self.return_icon.rect.collidepoint(pos_mouse):
            self.is_active = False
            self._reset_changes()

    def register_character(self, pos_mouse) -> None:
        if not self.block:
            if self.add_icon.rect.collidepoint(pos_mouse):
                if len(self.NAME) >= MIN_CHARACTERS_NAME:
                    self.db.create(self.NAME, self.ETHNICITY, self.CLASSE)

                    sleep(1)
                    os.environ["EVENTS"] = "loading"
                    os.environ["CHAR_NAME"] = self.NAME

    def _active_input_box(self, pos_mouse) -> None:

        if not self.block:
            if self.boxes[2].collidepoint(pos_mouse):
                self.inbox = True
            else:
                self.inbox = False

            COLORS["ACTIVE"] = COLORS["WHITE"] if self.inbox else COLORS["BLACK"]

    def _receives_character_name(self, event) -> None:
        """
        NAME RECEIVES THE PRESSED CHARACTERS, REMOVED FROM THE KEY/EVENT.UNICODE
        PREVENTS TEXT FROM BEING GREATER THAN MAX_C CHARACTERS
        """
        if not self.block:

            if event.type == pg.KEYDOWN and self.inbox:

                if len(self.ETHNICITY) > 2 < len(self.CLASSE):
                    if event.key == pg.KSCAN_UNKNOWN:
                        self.NAME = ""
                    if event.key == pg.K_BACKSPACE:
                        self.NAME = self.NAME[:-1]
                    else:
                        self.NAME += (
                            str(event.unicode)
                            .replace("\r", "")
                            .replace("\t", "")
                            .strip()
                            .casefold()
                        )

        self.NAME = (
            self.NAME[:-1] if len(self.NAME) >= MAX_CHARACTERS_NAME else self.NAME
        )

    def _get_mouse_events_to_show_interactive(self, pos_mouse) -> None:

        topleft = DISPLAY_NONE, DISPLAY_NONE
        img_return = "return"

        if self.return_icon.rect.collidepoint(pos_mouse):
            img_return = "select_return"

        for obj in self.ethnicity + self.class_:

            if obj.collidepoint(pos_mouse):
                topleft = obj.topleft

        self.interactive_[2].rect.topleft = topleft

        self.return_icon.image = pg.image.load(IMG_MENU[img_return])

    def _enable_icon_to_save_record(self) -> None:

        img_add = "add"

        if self.inbox and len(self.NAME) >= MIN_CHARACTERS_NAME:
            img_add = "select_add"

        self.add_icon.image = pg.image.load(IMG_LOAD[img_add])

    def _draw_box(self) -> None:
        # DRAW USER TEXT INPUT
        draw_texts(
            screen=self.main_screen,
            text=self.NAME.title(),
            pos_x=self.boxes[2].x + 5,
            pos_y=self.boxes[2].y + 5,
            size=25,
            color=COLORS["BLACK"],
        )

        # DRAW THE BOX FOR TEXT INPUT
        draw_rect(self.main_screen, COLORS["ACTIVE"], self.boxes[2], 2)

    def _draw_info_max_records(self) -> None:

        if self.block:

            pos_y = 500
            for line in INFO_MAX_RECORDS.split("|"):
                draw_texts(
                    screen=self.main_screen,
                    text="{}".format(line.replace("|", "\n").title().strip()),
                    pos_x=230,
                    pos_y=pos_y,
                    size=20,
                    color=COLORS["BLACK"],
                )
                pos_y += 30

    def _draw_subtitles(self) -> None:

        pos_x_txt = [75, 324, 573]
        pos_x_rect = [0, 249, 498]
        pos_y_etn, pos_y_clas = 70, 560

        for item in range(3):
            # TEXT AND BOX FOR ETHNICITIES
            draw_texts(
                screen=self.main_screen,
                text="{}".format(list_ethnicities[item].title()),
                pos_x=pos_x_txt[item],
                pos_y=pos_y_etn + 10,
                size=20,
            )
            self.ethnicity.append(pg.rect.Rect(pos_x_rect[item], pos_y_etn, 249, 41))

            # TEXT AND BOX FOR CLASSES
            draw_texts(
                screen=self.main_screen,
                text="{}".format(self.index_list_class[item].title()),
                pos_x=pos_x_txt[item] + 20,
                pos_y=pos_y_clas + 10,
                size=20,
            )

            self.class_.append(pg.rect.Rect(pos_x_rect[item], pos_y_clas, 249, 41))

    def _draw_info_ethnicity(self) -> None:

        if self.ETHNICITY != "":
            pos_y = 240

            for line in INFO_HERALDRY[self.ETHNICITY].replace("\n", "").split("\r"):
                draw_texts(
                    screen=self.main_screen,
                    text="{}".format(line),
                    pos_x=0,
                    pos_y=pos_y,
                    color=COLORS["BLACK"],
                )

                pos_y += 30 if len(INFO_HERALDRY[self.ETHNICITY]) < 600 else 15

    def _draw_info_classes(self) -> None:

        draw_rect(self.main_screen, COLORS["BLACK"], [185, 610, 550, 300], 1)

        if self.CLASSE:

            # SPRITE
            sprite = pg.image.load(
                "{}{}-{}.png".format(FOLDERS["classes"], self.ETHNICITY, self.CLASSE)
            )
            self.main_screen.blit(sprite, (25, 680))

            # TITLE
            draw_texts(
                screen=self.main_screen,
                text="{:^35}{:^35}".format("Status", "Skills"),
                pos_x=190,
                pos_y=620,
                color=COLORS["BLACK"],
                size=20,
            )
            # ATTRIBUTES
            classes: dict[str, dict] = self.db.read_json(
                "src/character/settings/classes.json"
            )
            pos_y = 680
            for attr, value in classes[self.ETHNICITY][self.CLASSE].items():
                if attr != "skills":
                    draw_texts(
                        screen=self.main_screen,
                        text="{:<} - {:>.1f}".format(attr.title(), value),
                        pos_x=210,
                        pos_y=pos_y,
                        color=COLORS["BLACK"],
                        size=18,
                    )
                    pos_y += 30

                    # SKILLS
            pos_y = 680
            skills = (
                INFO_SKILLS[f"{self.ETHNICITY}-{self.CLASSE}"]
                .replace("\n", "")
                .split("\r")
            )
            for line in skills:
                draw_texts(
                    screen=self.main_screen,
                    text="{}".format(line),
                    pos_x=375,
                    pos_y=pos_y,
                    color=COLORS["BLACK"],
                )
                pos_y += 20

    def _list_ethnicity_and_classes(
        self, ethnicity: object, name: str, background_img: str, pos_mouse
    ) -> None:

        classes = LIST_CLASSES[0] if "dark" in name else LIST_CLASSES[1]

        if ethnicity.collidepoint(pos_mouse):
            self._reset_changes()

            self.interactive_[0].rect.x = ethnicity.x
            self.boxes[0].image = pg.image.load(IMG_NEW_GAME[background_img])

            self.index_list_class = classes
            self.ETHNICITY = name.casefold()

        if self.interactive_[0].rect.x == ethnicity.x:

            for index in range(3):
                if self.class_[index].collidepoint(pos_mouse):
                    self.interactive_[1].rect.x = self.class_[index].x

                    self.CLASSE = classes[index].casefold()

    def _reset_changes(self) -> None:

        self.NAME, self.ETHNICITY, self.CLASSE = "", "", ""

        for index in range(2):
            self.interactive_[index].rect.x = DISPLAY_NONE
            self.boxes[0].image = pg.image.load(IMG_NEW_GAME["HERALDRY_BOX"])

    def events(self, event, pos_mouse) -> None:

        if event.type == pg.MOUSEBUTTONDOWN:
            self._return_menu(pos_mouse)

            if not self.block:
                self._select_guides(pos_mouse)
                self._active_input_box(pos_mouse)
                self.register_character(pos_mouse)

        self._get_mouse_events_to_show_interactive(pos_mouse)

        self._receives_character_name(event)

    def update(self) -> None:

        self._enable_icon_to_save_record()
        self._draw_info_max_records()

        if not self.block:
            self._draw_box()
            self._draw_subtitles()
            self._draw_info_ethnicity()
            self._draw_info_classes()

            draw_texts(
                screen=self.main_screen,
                text="{}".format(title_new_game[0]),
                pos_x=300 + len(title_new_game[0]),
                pos_y=15,
                size=27,
            )
            draw_texts(
                screen=self.main_screen,
                text="{}".format(title_new_game[1]),
                pos_x=300 + len(title_new_game[1]),
                pos_y=510,
                size=27,
            )
