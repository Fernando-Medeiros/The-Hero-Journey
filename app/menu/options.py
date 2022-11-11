import os
import pygame as pg

from app.functiontools import Obj, COLORS
from paths import *
from .settings import txt_options


DISPLAY_NONE = int(os.environ.get('DISPLAY_NONE'))
DISPLAY_DEFAULT_Y = int(os.environ.get('DISPLAY_DEFAULT_Y'))
MAX_FRAMES = os.environ.get('MAX_FRAMES')
MIN_FRAMES = os.environ.get('MIN_FRAMES')
MAX_RECORDS = int(os.environ.get('MAX_RECORDS'))
MIN_CHARACTERS_NAME = int(os.environ.get('MIN_CHARACTERS_NAME'))
MAX_CHARACTERS_NAME = int(os.environ.get('MAX_CHARACTERS_NAME'))


class Options:

    is_active = True
 
    def __init__(self, main_screen, *groups):

        self.main_screen = main_screen

        self.pos_center = self.main_screen.get_width() / 2

        self.title = txt_options['title']
        self.caption = txt_options['caption']
        self.screen = txt_options['screen']
        self.fps = txt_options['fps']
        self.sound = txt_options['sound']

        self.bg = Obj(IMG_OPTIONS['bg'], 0, 0, *groups)

        self.objects = {
            'full_screen': Obj(IMG_OPTIONS['inactive'], self.pos_center, 0, *groups),
            'default': Obj(IMG_OPTIONS['inactive'], self.pos_center, 0, *groups),
            '30fps': Obj(IMG_OPTIONS['inactive'], self.pos_center, 0, *groups),
            '60fps': Obj(IMG_OPTIONS['inactive'], self.pos_center, 0, *groups),
            'on': Obj(IMG_OPTIONS['inactive'], self.pos_center, 0, *groups),
            'off': Obj(IMG_OPTIONS['inactive'], self.pos_center, 0, *groups),
        }

        self.active = pg.image.load(IMG_OPTIONS['active'])
        self.inactive = pg.image.load(IMG_OPTIONS['inactive'])

        self.return_icon = Obj(IMG_MENU['return'], 206, 942, *groups)


    def _select_options(self, pos_mouse):

        for key, value in self.objects.items():

            if value.rect.collidepoint(pos_mouse):

                match key:

                    case 'full_screen':
                        pg.display.set_mode((DISPLAY_DEFAULT_Y, 1080), pg.SCALED | pg.FULLSCREEN)

                    case 'default':
                        pg.display.set_mode((DISPLAY_DEFAULT_Y, 1050), pg.SCALED | pg.RESIZABLE)

                    case '30fps':
                        os.environ['FRAMES'] = str(MIN_FRAMES)

                    case '60fps':
                        os.environ['FRAMES'] = str(MAX_FRAMES)

                    case 'on':
                        pg.mixer.unpause()
                        os.environ['MIXER'] = str('mixer_is_active')
                        
                    case 'off':
                        pg.mixer.pause()
                        os.environ['MIXER'] = str('mixer_is_stopped')


    def _check_options(self):
        
        for item in self.objects:

            match item:

                case 'full_screen':
                    result = self.active if pg.display.get_window_size()[0] >= 1920 else self.inactive

                case 'default':
                    result = self.active if pg.display.get_window_size()[0] <= DISPLAY_DEFAULT_Y else self.inactive
                
                case '30fps':
                    result = self.active if int(os.environ['FRAMES']) <= 30 else self.inactive

                case '60fps':
                    result = self.active if int(os.environ['FRAMES']) > 30 else self.inactive

                case 'on':
                    result = self.active if 'active' in os.environ['MIXER'] else self.inactive

                case 'off':
                    result = self.active if 'stopped' in os.environ['MIXER'] else self.inactive

                case _:
                    result = self.inactive

            self.objects[item].image = result


    def _draw_options(self):
        """
        DRAW ICONS AND CONFIGURATION TEXTS
        """
        pos_y = 240
        for item in self.objects:

            self.objects[item].rect.y = pos_y
            pos_y += 40

        self._help_draw_txt_in_options(self.caption[0], self.screen)
        self._help_draw_txt_in_options(self.caption[1], self.fps, pos=280)
        self._help_draw_txt_in_options(self.caption[2], self.sound, pos=360)


    def _return_menu(self, pos_mouse):

        if self.return_icon.rect.collidepoint(pos_mouse):

            self.is_active = False
          

    def _get_mouse_events_to_show_interactive(self, pos_mouse):

        img_return = 'return'

        if self.return_icon.rect.collidepoint(pos_mouse):
            img_return = 'select_return'

        self.return_icon.image = pg.image.load(IMG_MENU[img_return])


    def events_options(self, evento):

        pos_mouse = pg.mouse.get_pos()

        self._check_options()

        if evento.type == pg.MOUSEBUTTONDOWN:

            self._return_menu(pos_mouse)
            self._select_options(pos_mouse)

        self._get_mouse_events_to_show_interactive(pos_mouse)


    def update(self):
        self._draw_options()


    def _help_draw_txt_in_options(self, caption, args, tab=40, pos=200):
        
        FONT = pg.font.SysFont('arial', 15, True)

        draw = [
            (FONT.render(f'{self.title}', True, COLORS['WHITE']), (self.pos_center - len(self.title) * 9.5, 100)),
            (FONT.render(f'{caption}', True, COLORS['WHITE']), (self.pos_center - 150, pos + tab * 2)),
            (FONT.render(f'{args[0]}', True, COLORS['WHITE']), (self.pos_center + 30, pos + tab)),
            (FONT.render(f'{args[1]}', True, COLORS['WHITE']), (self.pos_center + 30, pos + tab * 2)),
        ]

        self.main_screen.blits(draw)
