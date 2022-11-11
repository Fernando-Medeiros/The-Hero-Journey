import pygame as pg
from app.functiontools import draw_texts, COLORS

class Views:

    def __init__(self, main_screen):
        self.main_screen = main_screen


    def _draw_name_and_level(self, attributes, show_status, rect):

        if not show_status:

            name = attributes["name"].replace('_', ' ').title()
            level = attributes["level"]

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


    def _draw_status(self, attributes, status, show_status, rect):

        if show_status:

            pos_x, pos_y = rect.topright

            __RECT = pg.draw.rect(
                self.main_screen, COLORS['WHITE'],
                (pos_x - 2, pos_y - 7, 240, 100), 1, 0, 7, 7, 7, 7)


            pos_y_attr = pos_y - 5
            
            for key, value in attributes.items():

                if not key in 'name, level, rank, xp, class, ethnicity':

                    draw_texts(
                        screen=self.main_screen,
                        text='{:<} - {:>}'.format(key.title(), value),
                        pos_x=pos_x + 5,
                        pos_y=pos_y_attr,
                        size=13)

                    pos_y_attr += 20


            pos_y_status = pos_y - 5

            for key, value in status.items():

                if not key in 'luck':

                    draw_texts(
                        screen=self.main_screen,
                        text='{:<} - {:>.1f}'.format(key.title(), value),
                        pos_x=pos_x + 125,
                        pos_y=pos_y_status,
                        size=13)
                        
                    pos_y_status += 20