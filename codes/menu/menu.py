from settings import *

soundtrack[0].play()


class Menu:

    class_menu = True
    BLOCK = False
    check = ''

    def __init__(self, *groups):
        self._background = Obj(IMG_MENU['bg'], 0, 0, *groups)

        self._guides = []

        self._objects = {
            'select': Obj(IMG_MENU['select'], 0, LIMBO, *groups),
            'info_credit': Obj(IMG_MENU['info_c'], 0, LIMBO, *groups),
            'return': Obj(IMG_MENU['return'], 206, LIMBO, *groups)
        }
        self._draw_guides()

    def _draw_guides(self):

        pos_x, pos_y = 195, 317

        for item in list_guides_menu:

            draw_texts(MAIN_SCREEN, f'{item:^45}'.title().replace('_', ' '), pos_x, pos_y + 15, size=25)

            self._guides.append(DrawStatusBar(356, 65, 0, 356, rect=(pos_x, pos_y)))

            pos_y += 90

    def _guide_new_game(self, pos_mouse):
        if self._guides[0].rect.collidepoint(pos_mouse):
            self.check = 'new'
            self.class_menu = False
            click_sound.play()

    def _guide_load(self, pos_mouse):
        if self._guides[1].rect.collidepoint(pos_mouse):
            self.check = 'load'
            self.class_menu = False
            click_sound.play()

    def _guide_options(self, pos_mouse):
        if self._guides[3].rect.collidepoint(pos_mouse):
            self.check = 'options'
            self.class_menu = False
            click_sound.play()

    def _guide_credit(self, pos_mouse):
        """
        ACTIVATES THE CREDIT GUIDE BY SELECTING AND CLICKING ON THE OPTION
        RETURNS THE PROJECT CREDITS IMAGE
        """
        if self._guides[2].rect.collidepoint(pos_mouse):
            y, y_ = 0, 942
            self.BLOCK = True

        elif self._objects['return'].rect.collidepoint(pos_mouse):
            y, y_ = LIMBO, LIMBO
            self.BLOCK = False

        else:
            return 0

        self._objects['info_credit'].rect.y = y
        self._objects['return'].rect.y = y_
        click_sound.play()

    def _guide_quit(self, pos_mouse):
        """
        REGISTER LOG AND END THE GAME
        """
        if self._guides[4].rect.collidepoint(pos_mouse):
            save_log()

    def _select_guides(self, pos_mouse):
        """
        POINT COLLISION BETWEEN MOUSE -> (X, Y) <- OBJECT RECT.
        RETURNS SELECTED GUIDE EFFECT WHEN MOUSE OVER
        """
        mouse_collision_catching_x_y(LIMBO, self._guides, self._objects['select'], pos_mouse)

    def events_menu(self, event):
        pos_mouse = pg.mouse.get_pos()

        if event.type == pg.MOUSEBUTTONDOWN and not self.BLOCK:
            self._guide_new_game(pos_mouse)
            self._guide_load(pos_mouse)
            self._guide_options(pos_mouse)
            self._guide_quit(pos_mouse)

        if event.type == pg.MOUSEMOTION and not self.BLOCK:
            self._select_guides(pos_mouse)

        if event.type == pg.MOUSEBUTTONDOWN:
            self._guide_credit(pos_mouse)

    def update(self, *args, **kwargs) -> None:
        draw_texts(MAIN_SCREEN, NAME_OF_THE_GAME, MAIN_SCREEN.get_width() / 2 - len(NAME_OF_THE_GAME) * 6.5, 100, size=25)
        draw_texts(MAIN_SCREEN, VERSION, MAIN_SCREEN.get_width() / 2 - len(VERSION), 980)

        if not self.BLOCK:
            self._draw_guides()
