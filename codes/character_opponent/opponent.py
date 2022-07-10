from codes.character_opponent.entity import *


class Enemy(Entity, Obj):

    show_status_interface = False
    alive = True

    def __init__(self, list_,  img, x, y, *groups):

        Obj.__init__(self, img, x, y, *groups)

        Entity.__init__(self)

        self.instance_data = list_

        self.loots = {
            'gold': 1,
            'soul': 1,
            'xp': 1
        }
        self.list_of_loots = []

        self._assign_attributes()
        self.assign_status_secondary()
        self.assign_current_status()

    def _assign_attributes(self):

        __list_key__ = ['force', 'agility', 'vitality', 'intelligence', 'resistance']

        self.attributes['name'] = self.instance_data[1]
        self.attributes['level'] = int(self.instance_data[2])

        for __key__ in __list_key__:

            self.attributes[__key__] = self._random_attributes_per_level(self.attributes['level'])

    @staticmethod
    def _random_attributes_per_level(level: int):

        __max__ = randint(level, level * 2)

        return randint(level, __max__)

    def _draw_name_and_level(self):

        if not self.show_status_interface:

            self.draw_render_status(f'{self.attributes["name"]}'.replace('_', ' ').title(), self.rect.x + 120, self.rect.y)
            self.draw_render_status(f'Lvl - {self.attributes["level"]}'.title(), self.rect.x + 120, self.rect.y + 17)

    def _draw_status(self):

        if self.show_status_interface:

            pos_x, pos_y = self.rect.topright

            __RECT = pg.draw.rect(MAIN_SCREEN, COLORS['WHITE'], (pos_x - 2, pos_y - 7, 240, 100), 1, 0, 7, 7, 7, 7)

            y = pos_y - 5
            for __key__, __value__ in self.attributes.items():

                if not __key__ in 'name, level, rank, xp, class, ethnicity':

                    self.draw_render_status(f'{__key__.title():<} - {__value__:>}', pos_x + 5, y, size=13)
                    y += 20

            y = pos_y - 5
            for __key__, __value__ in self.status.items():

                if not __key__ in 'luck':

                    self.draw_render_status(f'{__key__.title():<} - {__value__:>.1f}', pos_x + 125, y, size=13)
                    y += 20

    def _check_if_the_object_is_dead(self):

        if self.current_status['hp'] <= 0.1:

            self.alive = False

    def _show_status(self, pos_mouse):

        if self.rect.collidepoint(pos_mouse):

            self.show_status_interface = True
        else:
            self.show_status_interface = False

    def events(self):

        pos_mouse = pg.mouse.get_pos()

        self._show_status(pos_mouse)

    def update(self):

        self._check_if_the_object_is_dead()

        self.check_current_status()

        self.level_progression_enemy(self.level_up())

        self._draw_name_and_level()

        self._draw_status()

        if self.alive:

            self.status_regen()
