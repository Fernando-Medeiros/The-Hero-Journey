from settings import *
from opponent import Enemy
from character import Character


class Game:

    class_game = True
    check = ''
    group_sprites_opponent = GROUPS['opponent']

    def __init__(self, *groups):

        self._bg = Obj(IMG_GAME['bg'], 0, 0, *groups)

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
            'chest': Obj(IMG_GAME['chest'],  227, 980, *groups),
            'save': Obj(IMG_GAME['save'], 354, 980, *groups),
            'next': Obj(IMG_GAME['next'], 712, 104, *groups),
            'previous': Obj(IMG_GAME['previous'], 404, 104, *groups),
        }

        self._list_enemies_in_area = []

        self._gps = 'Fields of Slimes'

        self.character = Character()

    def _select_land(self, pos_mouse):
        index = LIST_LANDS.index(self._gps)

        if self._icons['next'].rect.collidepoint(pos_mouse):

            index = index if index + 1 >= len(LIST_LANDS) else index + 1
            self._enemies_in_the_area(), click_sound.play()

        elif self._icons['previous'].rect.collidepoint(pos_mouse):

            index = 0 if index - 1 <= 0 else index - 1
            self._enemies_in_the_area(),  click_sound.play()

        self._tools['gps'].rect.topleft = (POS_GPS[index])
        self._gps = LIST_LANDS[index]

    def _lands(self):

        draw_texts(MAIN_SCREEN, f'{self._gps:^40}', 404, 104, size=25)

    def _enemies_in_the_area(self):

        del self._list_enemies_in_area[::]
        for sprite in self.group_sprites_opponent.sprites():
            self.group_sprites_opponent.remove(sprite)

        y = 430
        for n in range(6):

            enemies = choice(LIST_ENEMIES)

            self._list_enemies_in_area.append(
                Enemy(enemies, FOLDER['enemies'] + enemies[0] + '.png', 430, y, self.group_sprites_opponent))
            y += 95

    def _get_mouse_events(self, pos_mouse):

        mouse_collision_changing_image(
            self._icons['next'], pos_mouse, IMG_GAME['select_next'], IMG_GAME['next'])
        mouse_collision_changing_image(
            self._icons['previous'], pos_mouse, IMG_GAME['select_previous'], IMG_GAME['previous'])

        mouse_collision_changing_image(
            self._icons['save'], pos_mouse, IMG_GAME['select_save'], IMG_GAME['save'])
        mouse_collision_changing_image(
            self._icons['options'], pos_mouse, IMG_GAME['select_options'], IMG_GAME['options'])

        mouse_collision_changing_image(
            self._icons['skills'], pos_mouse, IMG_GAME['select_skills'], IMG_GAME['skills'])
        mouse_collision_changing_image(
            self._icons['marketplace'], pos_mouse, IMG_GAME['select_marketplace'], IMG_GAME['marketplace'])

        mouse_collision_changing_image(
            self._icons['proficiency'], pos_mouse, IMG_GAME['select_proficiency'], IMG_GAME['proficiency'])
        mouse_collision_changing_image(
            self._icons['chest'], pos_mouse, IMG_GAME['select_chest'], IMG_GAME['chest'])

    def _save_and_exit(self, pos_mouse):

        if self._icons['save'].rect.collidepoint(pos_mouse):
            self.character.save()
            save_log()

    def _return_menu(self, pos_mouse):

        if self._icons['options'].rect.collidepoint(pos_mouse):

            self.character.save()
            self.check = 'menu'
            self.class_game = False

    def events_game(self, event):

        pos_mouse = pg.mouse.get_pos()

        if event.type == pg.MOUSEBUTTONDOWN:
            self._save_and_exit(pos_mouse)
            self._return_menu(pos_mouse)
            self._select_land(pos_mouse)

        if event.type == pg.MOUSEMOTION:
            self._get_mouse_events(pos_mouse)

        self.character.events_character(event)

    def update(self, main_screen):

        self._lands()
        self.character.update()
        self.group_sprites_opponent.draw(main_screen)

        [obj.update() for obj in self._list_enemies_in_area]
