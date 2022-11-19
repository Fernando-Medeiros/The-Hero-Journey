import pygame as pg

from app.functiontools import draw_rect, draw_texts


class Views:

    def __init__(self, main_screen):

        self.main_screen = main_screen

    def _draw_name_and_level(self, attr:dict, show_status:bool, rect:pg.Rect):

        if not show_status:
            name = attr["name"].title()
            level = attr["level"]

            draw_texts(
                screen=self.main_screen,
                text='{}'.format(name),
                pos_x=rect.x + 120, 
                pos_y=rect.y
                )
            draw_texts(
                screen=self.main_screen,
                text='Lvl - {}'.format(level),
                pos_x=rect.x + 120,
                pos_y=rect.y + 17
                )


    def draw_status_on_hover(self, attr:dict, status:dict, show_status:bool, rect:pg.Rect):

        pos_x, pos_y = rect.topright
        excludes = 'name, level, rank, class, ethnicity, gold, soul, xp, sprite, luck'
        
        def draw_name_column():  
            pos_y_attr = pos_y - 5
            
            for key, value in attr.items():
                if not key in excludes:
                    draw_texts(
                        screen=self.main_screen,
                        text='{:<} - {:>}'.format(key.title(), value),
                        pos_x=pos_x + 5,
                        pos_y=pos_y_attr,
                        size=13)
                    pos_y_attr += 20

        def draw_status_column():
            pos_y_status = pos_y - 5

            for key, value in status.items():
                if not key in excludes:
                    draw_texts(
                        screen=self.main_screen,
                        text='{:<} - {:>.1f}'.format(key.title(), value),
                        pos_x=pos_x + 125,
                        pos_y=pos_y_status,
                        size=13)
                        
                    pos_y_status += 20

        if show_status:
            draw_rect(self.main_screen, rect=[pos_x - 2, pos_y - 7, 240, 100])
            draw_name_column()
            draw_status_column()