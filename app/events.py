import pygame as pg

from .game import Game
from .menu.load import Load
from .menu.menu import Menu
from .menu.newgame import NewGame
from .menu.options import Options


class MenuController:

    is_active = True

    options_group = pg.sprite.Group()
    load_group = pg.sprite.Group()
    new_game_group = pg.sprite.Group()
    menu_group = pg.sprite.Group()

    def __init__(self, main_screen):
        self.menu_ = Menu(main_screen, self.menu_group)
        self.new = NewGame(main_screen, self.new_game_group)
        self.load = Load(main_screen, self.load_group)
        self.options = Options(main_screen, self.options_group)


    def draw(self, main_screen):

        loading = self.new.check + self.load.check

        if loading == '' and self.is_active:

            if self.menu_.is_active:
                self.menu_group.draw(main_screen)
                self.menu_.update()

            elif self.menu_.check == 'new' and self.new.is_active:
                self.new_game_group.draw(main_screen)
                self.new.update()

            elif self.menu_.check == 'load' and self.load.is_active:
                self.load_group.draw(main_screen)
                self.load.update()

            elif self.menu_.check == 'options' and self.options.is_active:
                self.options_group.draw(main_screen)
                self.options.update()

            else:
                self.menu_.is_active = True
                self.new.is_active = True
                self.load.is_active = True
                self.options.is_active = True

        else:
            self.menu_.check = ''
            self.new.check = ''
            self.load.check = ''
            self.is_active = False


    def events(self, event):
        if self.is_active:

            if self.menu_.is_active:
                self.menu_.events_menu(event)

            elif self.menu_.check == 'new' and self.new.is_active:
                self.new.events_new_game(event)

            elif self.menu_.check == 'load' and self.load.is_active:
                self.load.events_load(event)

            elif self.menu_.check == 'options' and self.options.is_active:
                self.options.events(event)


class GameController:

    is_active = True 
    game_group = pg.sprite.Group()

    def __init__(self, main_screen):
        self.game = Game(main_screen, self.game_group)

    def draw(self, main_screen):

        if self.is_active:

            if self.game.is_active:
                self.game_group.draw(main_screen)
                self.game.update()
               
            else:
                self.is_active = False
                self.game.is_active = True

    def events(self, event):

        if self.is_active and self.game.is_active:
            
            self.game.events(event)
