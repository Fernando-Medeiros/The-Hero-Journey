import pygame as pg
from random import randint

from ..character.settings import BASIC_ATTRIBUTES
from app.functiontools import Obj

from .base import BaseEntity
from .view import Views


class Enemy(Obj, BaseEntity, Views):

    show_status = False
    is_alive = True

    def __init__(self, list_,  img, x, y, main_screen, *groups):

        Obj.__init__(self, img, x, y, *groups)
        BaseEntity.__init__(self)
        Views.__init__(self, main_screen)

        self.instance_data = list_

        self.loots = {
            'gold': 1,
            'soul': 1,
            'xp': 1
        }
        self.list_of_loots = []

        self._assign_attributes()
        self.assign_status_secondary()
        self.assign_current_status()
        self._assign_random_loots_()


    def _assign_attributes(self):

        list_keys = BASIC_ATTRIBUTES

        self.attributes['name'] = self.instance_data[1]
        self.attributes['level'] = int(self.instance_data[2])

        for attribute in list_keys:

            self.attributes[attribute] = self._random_attributes_per_level(self.attributes['level'])


    def _random_attributes_per_level(self, level: int) -> int:

        max = randint(level, level * 2)

        return randint(level, max)


    def _assign_random_loots_(self):

        self.loots['gold'] = randint(1, self.attributes['level'])
        self.loots['xp'] = randint(1, self.attributes['level'])


    def _check_if_the_object_is_dead(self):

        if self.current_status['hp'] <= 0.1:

            self.is_alive = False


    def _show_status(self, pos_mouse):

        if self.rect.collidepoint(pos_mouse):

            self.show_status = True
        else:
            self.show_status = False


    def events(self):

        pos_mouse = pg.mouse.get_pos()

        self._show_status(pos_mouse)


    def update(self):

        self._check_if_the_object_is_dead()

        self.check_current_status()

        self.level_progression_enemy(self.level_up())

        self._draw_name_and_level(self.attributes, self.show_status, self.rect)

        self._draw_status(self.attributes, self.status, self.show_status, self.rect)

        if self.is_alive:

            self.status_regen()
