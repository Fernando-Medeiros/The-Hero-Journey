import os

import pygame as pg

from .game import Game
from .menu.load import Load
from .menu.menu import Menu
from .menu.newgame import NewGame
from .menu.options import Options


class MenuController:
    is_active = True

    group_options = pg.sprite.Group()
    group_load = pg.sprite.Group()
    group_new_game = pg.sprite.Group()
    group_menu = pg.sprite.Group()

    def __init__(self):
        self.menu_ = Menu(self.group_menu)
        self.new = NewGame(self.group_new_game)
        self.load = Load(self.group_load)
        self.options = Options(self.group_options)

    def draw(self, main_screen):
        if os.environ["EVENTS"] == "" and self.is_active:

            if self.menu_.is_active:
                self.group_menu.draw(main_screen)
                self.menu_.update()

            elif self.menu_.check == "new" and self.new.is_active:
                self.group_new_game.draw(main_screen)
                self.new.update()

            elif self.menu_.check == "load" and self.load.is_active:
                self.group_load.draw(main_screen)
                self.load.update()

            elif self.menu_.check == "options" and self.options.is_active:
                self.group_options.draw(main_screen)
                self.options.update()

            else:
                self.menu_.is_active = True
                self.new.is_active = True
                self.load.is_active = True
                self.options.is_active = True

        else:
            os.environ["EVENTS"] = ""
            self.menu_.check = ""
            self.is_active = False

    def events(self, event):

        pos_mouse = pg.mouse.get_pos()

        if self.is_active:

            if self.menu_.is_active:
                self.menu_.events(event, pos_mouse)

            elif self.menu_.check == "new" and self.new.is_active:
                self.new.events(event, pos_mouse)

            elif self.menu_.check == "load" and self.load.is_active:
                self.load.events(event, pos_mouse)

            elif self.menu_.check == "options" and self.options.is_active:
                self.options.events(event, pos_mouse)


class GameController:
    is_active = True
    group_game = pg.sprite.Group()

    def __init__(self):
        self.game = Game(self.group_game)

    def draw(self, main_screen):

        if self.is_active:

            if self.game.is_active:
                self.group_game.draw(main_screen)
                self.game.update()

            else:
                self.is_active = False
                self.game.is_active = True

    def events(self, event):

        pos_mouse = pg.mouse.get_pos()

        if self.is_active and self.game.is_active:
            self.game.events(event, pos_mouse)
