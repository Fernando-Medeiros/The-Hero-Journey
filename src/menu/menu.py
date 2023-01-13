import os

import pygame as pg

from ..tools import Obj, draw_texts, save_log_and_exit
from paths import *

from .settings import list_guides_menu

VERSION = os.environ.get("VERSION")
TITLE = os.environ.get("TITLE")
DISPLAY_NONE = int(os.getenv("DISPLAY_NONE", "-1080"))


class Menu:
    is_active = True
    block = False
    check = ""

    def __init__(self, *groups):

        self.main_screen = pg.display.get_surface()

        self.guides = []

        self.background = Obj(IMG_MENU["bg"], 0, 0, *groups)

        self.objects = {
            "select": Obj(IMG_MENU["select"], 0, DISPLAY_NONE, *groups),
            "info_credit": Obj(IMG_MENU["info_c"], 0, DISPLAY_NONE, *groups),
            "return": Obj(IMG_MENU["return"], 206, DISPLAY_NONE, *groups),
        }
        self._draw_guides()

    def _draw_guides(self) -> None:
        pos_x, pos_y = 195, 317

        for item in list_guides_menu:
            draw_texts(
                screen=self.main_screen,
                text="{:^45}".format(item.title().replace("_", " ")),
                pos_x=pos_x,
                pos_y=pos_y + 15,
                size=25,
            )
            self.guides.append(pg.rect.Rect(pos_x, pos_y, 356, 65))

            pos_y += 90

    def _guide_new_game(self, pos_mouse) -> None:
        if self.guides[0].collidepoint(pos_mouse):
            self.check = "new"
            self.is_active = False

    def _guide_load(self, pos_mouse) -> None:
        if self.guides[1].collidepoint(pos_mouse):
            self.check = "load"
            self.is_active = False

    def _guide_options(self, pos_mouse) -> None:
        if self.guides[3].collidepoint(pos_mouse):
            self.check = "options"
            self.is_active = False

    def _guide_credit(self, pos_mouse) -> bool | None:

        if self.guides[2].collidepoint(pos_mouse):
            y, y_ = 0, 942
            self.block = True

        elif self.objects["return"].rect.collidepoint(pos_mouse):
            y, y_ = DISPLAY_NONE, DISPLAY_NONE
            self.block = False
        else:
            return False

        self.objects["info_credit"].rect.y = y
        self.objects["return"].rect.y = y_

    def _guide_quit(self, pos_mouse) -> None:
        if self.guides[4].collidepoint(pos_mouse):
            save_log_and_exit()

    def _get_mouse_events_to_show_interactive(self, pos_mouse) -> None:
        img_return = "return"

        if self.objects["return"].rect.collidepoint(pos_mouse):
            img_return = "select_return"

        self.objects["return"].image = pg.image.load(IMG_MENU[img_return])

    def _select_guides(self, pos_mouse) -> None:

        topleft = DISPLAY_NONE, DISPLAY_NONE

        for obj in self.guides:

            if obj.collidepoint(pos_mouse):
                topleft = obj.topleft

        self.objects["select"].rect.topleft = topleft

    def events(self, event, pos_mouse) -> None:

        if event.type == pg.MOUSEBUTTONDOWN:
            self._guide_credit(pos_mouse)

            if not self.block:
                self._guide_new_game(pos_mouse)
                self._guide_load(pos_mouse)
                self._guide_options(pos_mouse)
                self._guide_quit(pos_mouse)

        if not self.block:
            self._select_guides(pos_mouse)

        self._get_mouse_events_to_show_interactive(pos_mouse)

    def update(self) -> None:
        draw_texts(
            screen=self.main_screen,
            text=TITLE,
            pos_x=self.main_screen.get_width() / 2 - len(TITLE) * 6.5,
            pos_y=100,
            size=25,
        )
        draw_texts(
            screen=self.main_screen,
            text=VERSION,
            pos_x=self.main_screen.get_width() / 2 - len(VERSION),
            pos_y=980,
        )

        if not self.block:
            self._draw_guides()
