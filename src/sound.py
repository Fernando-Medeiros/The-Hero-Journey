import pygame as pg

from paths import FOLDERS

"""
SOUND SETTINGS
"""
SOUNDS = {"click": pg.mixer.Sound("{}{}".format(FOLDERS["sound"], "click.mp3"))}

SONGS = {"orpheus": pg.mixer.Sound("{}{}".format(FOLDERS["soundtrack"], "orpheus.mp3"))}
