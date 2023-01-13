import os

import pygame as pg

from paths import *

from ..tools import COLORS, Obj
from .settings import txt_options

DISPLAY_NONE = int(os.getenv("DISPLAY_NONE", "-1080"))
DEFAULT_HEIGHT = int(os.getenv("DEFAULT_HEIGHT", "747"))
DEFAULT_WIDTH = int(os.getenv("DEFAULT_WIDTH", "1050"))

MAX_FRAMES = os.getenv("MAX_FRAMES", "60")
MIN_FRAMES = os.getenv("MIN_FRAMES", "30")

MAX_RECORDS = int(os.getenv("MAX_RECORDS", "9"))

MIN_CHARACTERS_NAME = int(os.getenv("MIN_CHARACTERS_NAME", "3"))
MAX_CHARACTERS_NAME = int(os.getenv("MAX_CHARACTERS_NAME", "20"))


class Options:
    is_active = True

    def __init__(self, *groups):

        self.main_screen = pg.display.get_surface()

        self.center = self.main_screen.get_width() / 2

        self.title = txt_options["title"]
        self.caption = txt_options["caption"]
        self.screen = txt_options["screen"]
        self.fps = txt_options["fps"]
        self.sound = txt_options["sound"]

        self.bg = Obj(IMG_OPTIONS["bg"], 0, 0, *groups)

        self.objects = {
            "full_screen": Obj(IMG_OPTIONS["inactive"], self.center, 0, *groups),
            "default": Obj(IMG_OPTIONS["inactive"], self.center, 0, *groups),
            "30fps": Obj(IMG_OPTIONS["inactive"], self.center, 0, *groups),
            "60fps": Obj(IMG_OPTIONS["inactive"], self.center, 0, *groups),
            "on": Obj(IMG_OPTIONS["inactive"], self.center, 0, *groups),
            "off": Obj(IMG_OPTIONS["inactive"], self.center, 0, *groups),
        }

        self.active = pg.image.load(IMG_OPTIONS["active"])
        self.inactive = pg.image.load(IMG_OPTIONS["inactive"])

        self.return_icon = Obj(IMG_MENU["return"], 206, 942, *groups)

    def _select_options(self, pos_mouse) -> None:

        for key, value in self.objects.items():
            if value.rect.collidepoint(pos_mouse):
                match key:
                    case "full_screen":
                        pg.display.set_mode(
                            (1080, DEFAULT_HEIGHT), pg.SCALED | pg.FULLSCREEN
                        )

                    case "default":
                        pg.display.set_mode(
                            (DEFAULT_WIDTH, DEFAULT_HEIGHT), pg.SCALED | pg.RESIZABLE
                        )

                    case "30fps":
                        os.environ["FRAMES"] = str(MIN_FRAMES)

                    case "60fps":
                        os.environ["FRAMES"] = str(MAX_FRAMES)

                    case "on":
                        pg.mixer.unpause()
                        os.environ["MIXER"] = str("mixer_is_active")

                    case "off":
                        pg.mixer.pause()
                        os.environ["MIXER"] = str("mixer_is_stopped")

    def _check_options(self) -> None:

        for item in self.objects:
            match item:
                case "full_screen":
                    result = (
                        self.active
                        if pg.display.get_window_size()[0] >= 1920
                        else self.inactive
                    )

                case "default":
                    result = (
                        self.active
                        if pg.display.get_window_size()[0] <= DEFAULT_WIDTH
                        else self.inactive
                    )

                case "30fps":
                    result = (
                        self.active
                        if int(os.environ["FRAMES"]) <= 30
                        else self.inactive
                    )

                case "60fps":
                    result = (
                        self.active if int(os.environ["FRAMES"]) > 30 else self.inactive
                    )

                case "on":
                    result = (
                        self.active
                        if "active" in os.environ["MIXER"]
                        else self.inactive
                    )

                case "off":
                    result = (
                        self.active
                        if "stopped" in os.environ["MIXER"]
                        else self.inactive
                    )

                case _:
                    result = self.inactive

            self.objects[item].image = result

    def _draw_options(self) -> None:
        """
        DRAW ICONS AND CONFIGURATION TEXTS
        """
        pos_y = 240
        for item in self.objects:
            self.objects[item].rect.y = pos_y
            pos_y += 40

        self._draw_txt_in_options(self.caption[0], self.screen)
        self._draw_txt_in_options(self.caption[1], self.fps, pos=280)
        self._draw_txt_in_options(self.caption[2], self.sound, pos=360)

    def _return_menu(self, pos_mouse) -> None:
        if self.return_icon.rect.collidepoint(pos_mouse):
            self.is_active = False

    def _get_mouse_events_to_show_interactives(self, pos_mouse) -> None:

        img_return = "return"
        if self.return_icon.rect.collidepoint(pos_mouse):
            img_return = "select_return"

        self.return_icon.image = pg.image.load(IMG_MENU[img_return])

    def _draw_txt_in_options(self, caption, args, gap=40, pos=200) -> None:

        font = pg.font.SysFont("arial", 15, True)
        color = COLORS["WHITE"]

        draw = [
            (
                font.render(f"{self.title}", True, color),
                (self.center - len(self.title) * 9.5, 100),
            ),
            (
                font.render(f"{caption}", True, color),
                (self.center - 150, pos + gap * 2),
            ),
            (font.render(f"{args[0]}", True, color), (self.center + 30, pos + gap)),
            (font.render(f"{args[1]}", True, color), (self.center + 30, pos + gap * 2)),
        ]
        self.main_screen.blits(draw)

    def events(self, event, pos_mouse) -> None:
        self._check_options()

        if event.type == pg.MOUSEBUTTONDOWN:
            self._return_menu(pos_mouse)
            self._select_options(pos_mouse)

        self._get_mouse_events_to_show_interactives(pos_mouse)

    def update(self) -> None:
        self._draw_options()
