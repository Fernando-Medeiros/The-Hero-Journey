import os
from datetime import datetime

import pygame as pg

VERSION = "3.0"

TITLE = "The Hero's Journey"

URL_CREDIT = "https://github.com/Fernando-Medeiros"

STATIC = "static/"

MIXER = "mixer_is_active"

DATETIME_APP = datetime.today().strftime("%d/%m/%Y %H:%M:%S")

# DISPLAY SETTINGS
DEFAULT_WIDTH = 747
DEFAULT_HEIGHT = 1050
DISPLAY_NONE = -1080

FRAMES = 30
MIN_FRAMES = 30
MAX_FRAMES = 60

# CHARACTER SETTINGS
CHAR_NAME = ""
MIN_CHARACTERS_NAME = 3
MAX_CHARACTERS_NAME = 20


class Main:
    def __init__(self) -> None:
        self.init_const()
        self.init_game()

        self.main_screen = pg.display.set_mode(
            (DEFAULT_WIDTH, DEFAULT_HEIGHT), pg.SCALED | pg.RESIZABLE
        )

        self.clock = pg.time.Clock()

        from src.events import GameController, MenuController

        self.menu = MenuController()
        self.game = GameController()

    def init_const(self):
        consts = {
            "VERSION": VERSION,
            "TITLE": TITLE,
            "URL_CREDIT": URL_CREDIT,
            "DATETIME_APP": DATETIME_APP,
            "MIXER": MIXER,
            "STATIC": STATIC,
            "DEFAULT_HEIGHT": DEFAULT_HEIGHT,
            "DEFAULT_WIDTH": DEFAULT_WIDTH,
            "DISPLAY_NONE": DISPLAY_NONE,
            "FRAMES": FRAMES,
            "MIN_FRAMES": MIN_FRAMES,
            "MAX_FRAMES": MAX_FRAMES,
            "CHAR_NAME": CHAR_NAME,
            "MIN_CHARACTERS_NAME": MIN_CHARACTERS_NAME,
            "MAX_CHARACTERS_NAME": MAX_CHARACTERS_NAME,
            "EVENTS": "",
        }
        for key, value in consts.items():
            os.environ[key] = str(value)

    def init_game(self):
        pg.init()
        pg.font.init()
        pg.mixer.init()

    def draw(self):
        if self.menu.is_active:
            self.menu.draw(self.main_screen)

        elif self.game.is_active:
            self.game.draw(self.main_screen)

        else:
            self.menu.is_active = True
            self.game.is_active = True

    def events(self):
        for event in pg.event.get():

            if event.type == pg.QUIT:
                from src.tools import save_log_and_exit

                save_log_and_exit()

            if self.menu.is_active:
                self.menu.events(event)

            elif self.game.is_active:
                self.game.events(event)

    def update(self):
        self.clock.tick(int(os.getenv("FRAMES", "30")))
        self.draw()
        self.events()
        pg.display.set_caption("{} | {:.2f}".format(TITLE, self.clock.get_fps()))
        pg.display.update()


if __name__ == "__main__":
    main = Main()
    while True:
        main.update()
