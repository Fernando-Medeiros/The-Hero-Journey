import pygame as pg

from .base import Entity
from .view import Views


class Enemy(Entity, Views):

    def __init__(self, data: dict, img: str, pos_x: int, pos_y: int, main_screen: pg.Surface, *groups):

        Entity.__init__(self)
        
        self.entity['attributes'].update(data)

        Views.__init__(self, main_screen,  img, pos_x, pos_y, *groups)
        
        self.assign_status_secondary()
        self.assign_current_status()    

    def events(self, pos_mouse):
        self._draw_status(pos_mouse)

    def update(self):

        self._is_alive()

        self._check_current_status()

        self._draw_name_and_level(self.entity)

        self._draw_status_on_hover(self.entity)

    