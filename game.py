from settings import *


class Game:

    class_game = True

    def __init__(self, *groups):
        self.bg = Obj(IMG_GAME['bg'], 0, 0, *groups)

        self._tools = {
            'map': Obj(IMG_GAME['map'], 432, 180, *groups),
            'gps': Obj(IMG_GAME['gps'], 494, 200, *groups)
        }
        self._loots = {
            'gold': Obj(IMG_GAME['gold'], 435, 6, *groups),
            'soul': Obj(IMG_GAME['soul'], 568, 6, *groups)
        }
        self._icons = {
            'options': Obj(IMG_GAME['options'], 15, 980, *groups),
            'skills': Obj(IMG_GAME['skills'], 68, 980, *groups),
            'marketplace': Obj(IMG_GAME['marketplace'], 121, 980, *groups),
            'proficiency': Obj(IMG_GAME['proficiency'], 174, 980, *groups),
            'save': Obj(IMG_GAME['save'], 354, 980, *groups),
            'next': Obj(IMG_GAME['next'], 712, 104, *groups),
            'previous': Obj(IMG_GAME['previous'], 404, 104, *groups),
        }

        self.gps = 'Fields of Slimes'

    def _select_land(self, pos_mouse):
        index = LIST_LANDS.index(self.gps)

        if self._icons['next'].rect.collidepoint(pos_mouse):

            index = index if index + 1 >= len(LIST_LANDS) else index + 1
            click_sound.play()

        elif self._icons['previous'].rect.collidepoint(pos_mouse):

            index = 0 if index - 1 <= 0 else index - 1
            click_sound.play()

        self._tools['gps'].rect.topleft = (POS_GPS[index])
        self.gps = LIST_LANDS[index]

    def _lands(self):

        draw_texts(MAIN_SCREEN, f'{self.gps:^40}', 404, 104, size=25)

    def _get_mouse_events(self, pos_mouse):

        mouse_collision_changing_image(self._icons['next'], pos_mouse, IMG_GAME['next'], IMG_GAME['select_next'])
        mouse_collision_changing_image(self._icons['previous'], pos_mouse, IMG_GAME['previous'], IMG_GAME['select_previous'])

    def _save_and_exit(self, pos_mouse):
        if self._icons['save'].rect.collidepoint(pos_mouse):
            self.class_game = False

    def events_game(self, event):

        pos_mouse = pg.mouse.get_pos()

        if event.type == pg.MOUSEBUTTONDOWN:
            self._save_and_exit(pos_mouse)
            self._select_land(pos_mouse)

        if event.type == pg.MOUSEMOTION:
            self._get_mouse_events(pos_mouse)

    def update(self):
        self._lands()
