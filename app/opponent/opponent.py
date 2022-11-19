from random import randint

import pygame as pg

from app.functiontools import Obj

from ..character.settings import BASIC_ATTRIBUTES
from .base import BaseEntity
from .view import Views


class Enemy(Obj, BaseEntity, Views):

    show_status = False
    is_alive = True

    def __init__(self, data: dict, img, pos_x, pos_y, main_screen: pg.Surface, *groups):

        Obj.__init__(self, img, pos_x, pos_y, *groups)
        BaseEntity.__init__(self)
        self.entity['attributes'].update(data)
        Views.__init__(self, main_screen)

        self.list_of_loots = []
        
        self.assign_status_secondary()
        self.assign_current_status()      


    def _check_if_the_object_is_dead(self):

        if self.entity['current']['hp'] <= 0.1:

            self.is_alive = False


    def _show_status(self, pos_mouse):

        if self.rect.collidepoint(pos_mouse):

            self.show_status = True
        else:
            self.show_status = False


    def events(self, pos_mouse):
        self._show_status(pos_mouse)


    def update(self):

        self._check_if_the_object_is_dead()

        self.check_current_status()

        self.level_progression_enemy(self.level_up())

        self._draw_name_and_level(
            self.entity['attributes'], self.show_status, self.rect)

        self.draw_status_on_hover(
            self.entity['attributes'], self.entity['status'], self.show_status, self.rect)

        if self.is_alive:

            self.status_regen()
