import pygame as pg

from app.tools import COLORS, draw_rect, draw_status_bar, draw_texts
from paths import IMG_CLASSES


class View:
    
    show_status = False

    def __init__(self, main_screen: pg.Surface):
        self.main_screen = main_screen

        self.button_status = pg.rect.Rect(15, 190, 373, 30)
    
    
    def _show_status(self, pos_mouse) -> None:

        if self.button_status.collidepoint(pos_mouse):
            self.show_status = True
        else:
            self.show_status = False

    def _draw_bar_status(self, current_status, status_secondary, attributes) -> None:

        bar = [
            [status_secondary['hp'], current_status['hp'], COLORS['RED'], [173, 36], 222],
            [status_secondary['mp'], current_status['mp'], COLORS['BLUE'], [180, 54], 215],
            [status_secondary['stamina'], current_status['stamina'], COLORS['GREEN'], [183, 72], 212],
            [attributes['level'] * 15, attributes['xp'], COLORS['YELLOW'],  [185, 90], 210]
            ]

        for bar_status in bar:

            draw_status_bar(
                screen=self.main_screen,
                height=15,
                fixed_value=bar_status[0],
                width=bar_status[4],
                color=bar_status[2],
                rect=bar_status[3],
                current_value=bar_status[1])


    def _draw_sprites(self, attributes) -> None:

        ethnicity = attributes['ethnicity']
        class_ = attributes['class']

        idd = 'ed_' if 'dark' in ethnicity else 'ef_' if 'forest' in ethnicity else 'eg_'

        sprite = pg.image.load(IMG_CLASSES[idd + class_])

        self.main_screen.blit(sprite, (20, 18))


    def _draw_info_status(self,current_status, status_secondary, attributes, others) -> None:

        draw_texts(self.main_screen, f'Lvl - {attributes["level"]}', 189, 110)
        draw_texts(self.main_screen, str(attributes['name']).title(), 189, 8, size=20)
        draw_texts(self.main_screen, str(others['gold']), 477, 28, size=25)
        draw_texts(self.main_screen, str(others['soul']), 610, 28, size=25)

        info = [
            '{:^21.1f}/{:^21.1f}'.format(current_status["hp"], status_secondary["hp"]),
            '{:^21.1f}/{:^21.1f}'.format(current_status["mp"], status_secondary["mp"]),
            '{:^21.1f}/{:^21.1f}'.format(current_status["stamina"], status_secondary["stamina"]),
            '{:^21.1f}/{:^21.1f}'.format(attributes["xp"], attributes["level"] * 15)
        ]

        x, y = 185, 36
        for item in info:

            draw_texts(
                screen=self.main_screen,
                text=item,
                pos_x=x, pos_y=y,
                size=13)

            y += 18


    def _draw_status(self, attributes, status):
        
        draw_rect(
           screen=self.main_screen, 
           rect=self.button_status[::])

        draw_texts(
            screen=self.main_screen,
            text="Status",
            pos_x=170,pos_y=190,
            size=25)

        if self.show_status:            
            draw_rect(
                screen=self.main_screen,
                rect=[15, 220, 373, 150])

            pos_y = 230
            for key, value in attributes.items():

                if not key in 'name, level, rank, xp':
                    draw_texts(
                        screen=self.main_screen,
                        text='{:<} - {:>}'.format(key.title(), value),
                        pos_x=20, pos_y=pos_y)
                    
                    pos_y += 20

            pos_y = 230
            for key, value in status.items():

                draw_texts(
                    screen=self.main_screen,
                    text='{:<} - {:>.1f}'.format(key.title(), value),
                    pos_x=206, pos_y=pos_y)
                
                pos_y += 20
