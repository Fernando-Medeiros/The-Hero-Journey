import os
import pygame as pg
from datetime import datetime


VERSION = '2.1'

GAME_NAME = "The Hero's Journey"

URL_CREDIT = 'https://github.com/Fernando-Medeiros'

STATIC = 'static/'

MIXER = 'mixer_is_active'

DATETIME_APP = datetime.today().strftime('%d/%m/%Y %H:%M:%S')

# DISPLAY SETTINGS
DISPLAY_DEFAULT_Y = 747
DISPLAY_DEFAULT_X = 1050
DISPLAY_NONE = -1080

FRAMES = 30
MIN_FRAMES = 30
MAX_FRAMES = 60

# CHARACTER SETTINGS
CHARNAME = '' 
MAX_RECORDS = 9
MIN_CHARACTERS_NAME = 3
MAX_CHARACTERS_NAME = 20


class Main:

    def __init__(self) -> None:
        self.init_const()
        self.init_game()

        self.main_screen = pg.display.set_mode(
            (DISPLAY_DEFAULT_Y, DISPLAY_DEFAULT_X),
            pg.SCALED | pg.RESIZABLE
            )

        self.frames = pg.time.Clock()

        from app.events import MenuController, GameController

        self.menu = MenuController(self.main_screen)
        self.game = GameController(self.main_screen)
        

    def init_const(self):
        list_const = {        
            'VERSION': VERSION,
            'GAME_NAME': GAME_NAME,
            'URL_CREDIT': URL_CREDIT,
            'DATETIME_APP': DATETIME_APP,
            'MIXER': MIXER,
            'STATIC': STATIC,
            'DISPLAY_DEFAULT_Y' : DISPLAY_DEFAULT_Y,
            'DISPLAY_DEFAULT_X' : DISPLAY_DEFAULT_X, 
            'DISPLAY_NONE' : DISPLAY_NONE,
            'FRAMES': FRAMES,
            'MIN_FRAMES': MIN_FRAMES,
            'MAX_FRAMES': MAX_FRAMES,
            'MAX_RECORDS': MAX_RECORDS,
            'CHARNAME': CHARNAME,
            'MIN_CHARACTERS_NAME': MIN_CHARACTERS_NAME,
            'MAX_CHARACTERS_NAME': MAX_CHARACTERS_NAME,        
        }
        for const in list_const:
            os.environ[const] = str(list_const[const])


    def init_game(self):
        pg.init()
        pg.font.init()
        pg.mixer.init()
        pg.display.set_caption(GAME_NAME)
                

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
                
                from app.functiontools import save_log_and_exit
                save_log_and_exit()

            if self.menu.is_active:
                self.menu.events(event)

            elif self.game.is_active:
                self.game.events(event)


    def update(self):
        self.frames.tick(int(os.environ['FRAMES']))
        self.draw()
        self.events()
        pg.display.update()

   

if __name__ == '__main__':
    
    main = Main()
    
    while True:
        main.update()
