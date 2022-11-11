import pygame as pg
from paths import FOLDER

"""
SOUND SETTINGS
"""
SOUNDS = {
    'click': pg.mixer.Sound('{}{}'.format(FOLDER['sound'], 'click.mp3'))
}

SONGS = {
    'orpheus': pg.mixer.Sound('{}{}'.format(FOLDER['soundtrack'], 'orpheus.mp3'))
}