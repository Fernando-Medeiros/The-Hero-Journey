from settings import *


class Options:

    class_options = True
    FULL_SCREEN, DEFAULT = False, False

    mixer = 'mixer_active'
    pos_center = MAIN_SCREEN.get_width() / 2
    MAX_FRAMES = MAX_FRAMES

    def __init__(self, *groups):

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
                        self.MAX_FRAMES = 30

                    case '60fps':
                        self.MAX_FRAMES = 60

                    case 'on':
                        pg.mixer.unpause()
                        self.mixer = 'mixer_active'

                    case 'off':
                        pg.mixer.pause()
                        self.mixer = 'mixer_stop'


    def _check_options(self):

        active = pg.image.load(IMG_OPTIONS['active'])
        inactive = pg.image.load(IMG_OPTIONS['inactive'])
        frame = FRAMES.get_fps()

        for item in self.objects:

            match item:

                case 'full_screen':
                    self.FULL_SCREEN = True if pg.display.get_window_size()[0] >= 1920 else False
                    result = active if self.FULL_SCREEN else inactive

                case 'default':
                    self.DEFAULT = True if pg.display.get_window_size()[0] <= DISPLAY_DEFAULT_Y else False
                    result = active if self.DEFAULT else inactive

                case _:
                    result = inactive

            match item:

                case '30fps':
                    result = active if frame < 50 else inactive
                case '60fps':
                    result = active if frame > 50 else inactive

                case 'on':
                    result = active if 'mixer_active' in self.mixer else inactive
                case 'off':
                    result = active if 'mixer_stop' in self.mixer else inactive

            self.objects[item].image = result


    def _draw_options(self):
        """
        DRAW ICONS AND CONFIGURATION TEXTS
        """
        y = 240
        for item in self.objects:

            self.objects[item].rect.y = y
            y += 40

        self._help_draw_txt_in_options(self.caption[0], self.screen)
        self._help_draw_txt_in_options(self.caption[1], self.fps, pos=280)
        self._help_draw_txt_in_options(self.caption[2], self.sound, pos=360)


    def _return_menu(self, pos_mouse):

        if self.return_icon.rect.collidepoint(pos_mouse):

            self.class_options = False
            click_sound.play()


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
        """
        AUXILIARY FUNCTION TO RENDER THE TEXTS OF EACH OPTION
        """
        draw = [
            (FONT_SETTINGS.render(f'{self.title}', True, COLORS['WHITE']), (self.pos_center - len(self.title) * 9.5, 100)),
            (FONT_SETTINGS.render(f'{caption}', True, COLORS['WHITE']), (self.pos_center - 150, pos + tab * 2)),
            (FONT_SETTINGS.render(f'{args[0]}', True, COLORS['WHITE']), (self.pos_center + 30, pos + tab)),
            (FONT_SETTINGS.render(f'{args[1]}', True, COLORS['WHITE']), (self.pos_center + 30, pos + tab * 2)),
        ]

        MAIN_SCREEN.blits(draw)
