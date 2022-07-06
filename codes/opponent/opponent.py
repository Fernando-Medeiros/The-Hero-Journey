from settings import *


class Enemy(Obj):

    show_status_interface = False

    def __init__(self, list_, img, x_, y_, *groups):

        self.instance_data = list_

        self.attributes = {
            'name': '',
            'level': 1,
            'force': 1,
            'agility': 1,
            'vitality': 1,
            'intelligence': 1,
            'resistance': 1,
            'xp': 1
        }
        self.status_secondary = {
            'hp': 1,
            'mp': 1,
            'stamina': 1
        }
        self.current_status = {
            'hp': 1,
            'mp': 1,
            'stamina': 1
        }
        self.status = {
            'attack': 1,
            'defense': 1,
            'dodge': 1,
            'block': 1,
            'critical': 1,
            'luck': 1
        }
        self.loots = {
            'gold': 1,
            'soul': 1,
            'xp': 1
        }

        self.list_of_loots = []

        self._assign_attributes()
        self._assign_status()
        self._assign_current_status()

        super().__init__(img, x_, y_, *groups)

    def _assign_attributes(self):

        list_key = [key for key in self.attributes]

        for index, value in enumerate(self.instance_data[1:]):

            value = int(value) if str(value).isnumeric() else str(value)
            self.attributes[list_key[index]] = value

    def _assign_status(self):

        level, force, agility, vitality, intelligence, resistance = \
            list(self.attributes.values())[1:7]

        self.status_secondary['hp'] = level * vitality * force * 3.5
        self.status_secondary['mp'] = level * intelligence + resistance * 1.5
        self.status_secondary['stamina'] = level * resistance * 1.5

        self.status['attack'] = force * level + (agility / 2)
        self.status['defense'] = resistance * level + (agility / 2)
        self.status['dodge'] = (agility + level) / 4
        self.status['block'] = (agility + resistance) / 4
        self.status['critical'] = agility / 4
        self.status['luck'] = (level + agility) / 4

    def _assign_current_status(self):

        self.current_status['hp'] = self.status_secondary['hp']
        self.current_status['mp'] = self.status_secondary['mp']
        self.current_status['stamina'] = self.status_secondary['stamina']

    def _check_current_status(self):

        if self.current_status['hp'] <= 0:
            self.status_secondary['hp'] = 1

        if self.current_status['mp'] <= 0:
            self.status_secondary['mp'] = 1

        if self.current_status['stamina'] <= 0:
            self.status_secondary['stamina'] = 1

    def _draw_name_level(self):

        draw_texts(MAIN_SCREEN, f'{self.attributes["name"]}'.replace('_', ' ').title(), self.rect.x + 120, self.rect.y)
        draw_texts(MAIN_SCREEN, f'Lvl - {self.attributes["level"]}'.title(), self.rect.x + 120, self.rect.y + 17)

    def _level_up(self):

        next_level = self.attributes['level'] * 15

        if self.attributes['xp'] >= next_level:

            self.attributes['level'] += 1
            self.attributes['xp'] = 1
            self._level_progression()

    def _level_progression(self):

        keys = 'force', 'vitality', 'agility', 'intelligence', 'resistance'

        for index, key in enumerate(keys):
            self.attributes[key] += 1

    def _loot(self):
        pass

    def _draw_status(self):

        if self.show_status_interface:

            pos_x, pos_y = self.rect.topright

            DrawStatusBar(1, 1, 100, 240).draw(MAIN_SCREEN, COLORS['BLACK'], pos_x, pos_y, 100, 100)

            y = pos_y
            for key, value in self.attributes.items():
                if not key in 'name, level, rank, xp':
                    draw_texts(MAIN_SCREEN, f'{key.title():<} - {value:>}', pos_x + 5, y, size=13)
                    y += 20

            y = pos_y
            for key, value in self.status.items():
                draw_texts(MAIN_SCREEN, f'{key.title():<} - {value:>.1f}', pos_x + 125, y, size=13)
                y += 20

    def _show_status(self, pos_mouse):

        if self.rect.collidepoint(pos_mouse):
            self.show_status_interface = True
        else:
            self.show_status_interface = False

    def events(self, event):

        pos_mouse = pg.mouse.get_pos()

        if event.type == pg.MOUSEMOTION:
            self._show_status(pos_mouse)

    def update(self):

        self._check_current_status()
        self._draw_name_level()
        self._draw_status()
