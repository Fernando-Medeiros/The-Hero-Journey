from settings import *

soundtrack[0].play()


class Menu:
    class_menu = True
    BLOCK = False
    check = ''

    def __init__(self, *groups):
        self.bg = Obj(IMG_MENU['bg'], 0, 0, *groups)

        self.objects_1 = {
            'new_game': Obj(IMG_MENU['new'], 0, 0, *groups),
            'load': Obj(IMG_MENU['load'], 0, 0, *groups),
            'credit': Obj(IMG_MENU['credit'], 0, 0, *groups),
            'options': Obj(IMG_MENU['options'], 0, 0, *groups),
            'quit': Obj(IMG_MENU['quit'], 0, 0, *groups),
        }

        self.objects_2 = {
            'select': Obj(IMG_MENU['select'], 0, LIMBO, *groups),
            'info_credit': Obj(IMG_MENU['info_c'], 0, LIMBO, *groups),
            'return': Obj(IMG_MENU['return'], 206, LIMBO, *groups)
        }

        self.pos_x, self.pos_y = 195, 317
        for item in self.objects_1:
            self.objects_1[item].rect.topleft = (self.pos_x, self.pos_y)
            self.pos_y += 90

    def guide_new_game(self, pos_mouse):
        if self.objects_1['new_game'].rect.collidepoint(pos_mouse):
            self.check = 'new'
            self.class_menu = False
            click_sound.play()

    def guide_load(self, pos_mouse):
        if self.objects_1['load'].rect.collidepoint(pos_mouse):
            self.check = 'load'
            self.class_menu = False
            click_sound.play()

    def guide_options(self, pos_mouse):
        if self.objects_1['options'].rect.collidepoint(pos_mouse):
            self.check = 'options'
            self.class_menu = False
            click_sound.play()

    def guide_credit(self, pos_mouse):
        """
        ACTIVATES THE CREDIT GUIDE BY SELECTING AND CLICKING ON THE OPTION
        RETURNS THE PROJECT CREDITS IMAGE
        """
        if self.objects_1['credit'].rect.collidepoint(pos_mouse):
            y, y_ = 0, 942
            self.BLOCK = True

        elif self.objects_2['return'].rect.collidepoint(pos_mouse):
            y, y_ = LIMBO, LIMBO
            self.BLOCK = False

        else:
            return 0

        self.objects_2['info_credit'].rect.y = y
        self.objects_2['return'].rect.y = y_
        click_sound.play()

    def guide_quit(self, pos_mouse):
        """
        REGISTER LOG AND END THE GAME
        """
        if self.objects_1['quit'].rect.collidepoint(pos_mouse):
            save_log()

    def select_guides(self, pos_mouse):
        """
        POINT COLLISION BETWEEN MOUSE -> (X, Y) <- OBJECT RECT.
        RETURNS SELECTED GUIDE EFFECT WHEN MOUSE OVER
        """
        mouse_collision_catching_x_y(LIMBO, self.objects_1, self.objects_2['select'], pos_mouse)

    def events_menu(self, evento):
        pos_mouse = pg.mouse.get_pos()

        if evento.type == pg.MOUSEBUTTONDOWN and not self.BLOCK:
            self.guide_new_game(pos_mouse)
            self.guide_load(pos_mouse)
            self.guide_options(pos_mouse)
            self.guide_quit(pos_mouse)

        if evento.type == pg.MOUSEMOTION and not self.BLOCK:
            self.select_guides(pos_mouse)

        if evento.type == pg.MOUSEBUTTONDOWN:
            self.guide_credit(pos_mouse)

    def update(self, *args, **kwargs) -> None:
        draw_texts(MAIN_SCREEN, NAME_OF_THE_GAME, MAIN_SCREEN.get_width() / 2 - len(NAME_OF_THE_GAME) * 6.5, 100, size=25)
        draw_texts(MAIN_SCREEN, VERSION, MAIN_SCREEN.get_width() / 2 - len(VERSION) * 6.5, MAIN_SCREEN.get_height() - 100)
