from settings import *


class Game:

    class_game = True

    def __init__(self, *groups):
        self.bg = Obj(IMG_GAME['bg'], 0, 0, *groups)

        self.tools = {
            'map': Obj(IMG_GAME['map'], 432, 180, *groups),
            'gps': Obj(IMG_GAME['gps'], 494, 200, *groups)
        }
        self.loots = {
            'gold': Obj(IMG_GAME['gold'], 435, 6, *groups),
            'soul': Obj(IMG_GAME['soul'], 568, 6, *groups)
        }
        self._icons = {
            'options': Obj(IMG_GAME['options'], 15, 1027, *groups),
            'skills': Obj(IMG_GAME['skills'], 68, 1027, *groups),
            'marketplace': Obj(IMG_GAME['marketplace'], 121, 1027, *groups),
            'proficiency': Obj(IMG_GAME['proficiency'], 174, 1027, *groups),
            'save': Obj(IMG_GAME['save'], 354, 1027, *groups),
        }

    def save_and_exit(self, pos_mouse):
        if self._icons['save'].rect.collidepoint(pos_mouse):
            self.class_game = False

    def events_game(self, event):

        pos_mouse = pg.mouse.get_pos()

        if event.type == pg.MOUSEBUTTONDOWN:
            self.save_and_exit(pos_mouse)

    def update(self):
        pass
