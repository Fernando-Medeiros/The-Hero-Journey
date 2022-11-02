import pygame as pg

from paths import *
from functiontools import *


pg.init(), pg.font.init(), pg.mixer.init()

VERSION = '2.1'

NAME_OF_THE_GAME = "The Hero's Journey"

URL_CREDIT = 'https://github.com/Fernando-Medeiros'

DATETIME_INIT_APP = datetime.today().strftime('%d/%m/%Y %H:%M:%S')

pg.display.set_caption(NAME_OF_THE_GAME)

"""
DISPLAY SETTINGS
"""
DISPLAY_DEFAULT_Y = 747
DISPLAY_DEFAULT_X = 1050

MAIN_SCREEN = pg.display.set_mode((DISPLAY_DEFAULT_Y, DISPLAY_DEFAULT_X), pg.SCALED | pg.RESIZABLE)


FONT_SETTINGS = pg.font.SysFont('arial', 25, True)

FRAMES = pg.time.Clock()
MAX_FRAMES = 30

GROUPS = {
    'menu': pg.sprite.Group(),
    'new': pg.sprite.Group(),
    'load': pg.sprite.Group(),
    'options': pg.sprite.Group(),
    'opponent': pg.sprite.Group(),
    'game': pg.sprite.Group()
}

"""
CHARACTER SETTINGS
"""
MAX_RECORDS = 9
MIN_CHARACTERS_NAME = 3
MAX_CHARACTERS_NAME = 20

"""
OTHERS
"""
DISPLAY_NONE = -1080

COLORS = {
    'WHITE': (255, 255, 255),
    'BLACK': (0, 0, 0),
    'RED': (176, 31, 31),
    'GREEN': (29, 161, 85),
    'BLUE': (67, 138, 167),
    'YELLOW': (235, 197, 70),
    'BLUE_2': (6, 0, 56),
    'WOOD': (210, 180, 140),
    'PURPLE': (38, 1, 36),
    'ACTIVE': 0
}

"""
SOUND SETTINGS
"""
SOUNDS = {
    'click': pg.mixer.Sound(FOLDER['sound'] + 'click.mp3')
}

SONGS = {
    'orpheus': pg.mixer.Sound(FOLDER['soundtrack'] + 'orpheus.mp3')
}

click_sound = SOUNDS['click']