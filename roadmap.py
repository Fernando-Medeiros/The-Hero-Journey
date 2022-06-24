from settings import *
from menu import Menu
from newgame import NewGame
from load import Load
from options import Options


class RoadMapMenu:
    grupo_sprite_options = GROUPS['options']
    grupo_sprite_load = GROUPS['load']
    grupo_sprite_new_game = GROUPS['new']
    grupo_sprite_menu = GROUPS['menu']

    menu_ = Menu(grupo_sprite_menu)
    new = NewGame(grupo_sprite_new_game)
    load = Load(grupo_sprite_load)
    options = Options(grupo_sprite_options)

    def __int__(self):
        pass

    def draw(self, main_screen):
        if self.menu_.class_menu:
            self.grupo_sprite_menu.draw(main_screen)

        elif self.menu_.check == 'new' and self.new.class_new_game:
            self.grupo_sprite_new_game.draw(main_screen)

        elif self.menu_.check == 'load' and self.load.class_load:
            self.grupo_sprite_load.draw(main_screen)

        elif self.menu_.check == 'options' and self.options.class_options:
            self.grupo_sprite_options.draw(main_screen)

        else:
            self.menu_.class_menu = True
            self.new.class_new_game = True
            self.load.class_load = True
            self.options.class_options = True

    def events(self, event):
        if self.menu_.class_menu:
            self.menu_.events_menu(event)

        elif self.menu_.check == 'new' and self.new.class_new_game:
            self.new.events_new_game(event)

        elif self.menu_.check == 'load' and self.load.class_load:
            self.load.events_load(event)

        elif self.menu_.check == 'options' and self.options.class_options:
            self.options.events_options(event)

    def update(self):
        if self.menu_.class_menu:
            self.menu_.update()
        elif self.menu_.check == 'new' and self.new.class_new_game:
            self.new.update()
        elif self.menu_.check == 'load' and self.load.class_load:
            self.load.update()
        elif self.menu_.check == 'options' and self.options.class_options:
            self.options.update()
