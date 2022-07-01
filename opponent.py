from settings import *


class Enemy(Obj):

    alive = True

    def __init__(self, list_, img, x_, y_, *groups):

        self.instance_data = list_

        self._attributes = {
            'name': '',
            'level': 1,
            'force': 1,
            'agility': 1,
            'vitality': 1,
            'intelligence': 1,
            'resistance': 1,
            'xp': 1
        }
        self._status_secondary = {
            'hp': 1,
            'mp': 1,
            'stamina': 1
        }
        self._current_status = {
            'hp': 1,
            'mp': 1,
            'stamina': 1
        }
        self._status = {
            'attack': 1,
            'defense': 1,
            'dodge': 1,
            'critical': 1,
            'luck': 1
        }

        self._list_of_loots = []

        self._assign_attributes()
        self._assign_status()
        self._assign_current_status()

        super().__init__(img, x_, y_, *groups)

    def _assign_attributes(self):

        list_key = [key for key in self._attributes]

        for index, value in enumerate(self.instance_data[1:]):

            value = int(value) if str(value).isnumeric() else str(value)
            self._attributes[list_key[index]] = value

    def _assign_status(self):

        level, force, agility, vitality, intelligence, resistance = \
            list(self._attributes.values())[1:7]

        self._status_secondary['hp'] = level * vitality * force * 3.5
        self._status_secondary['mp'] = level * intelligence + resistance * 1.5
        self._status_secondary['stamina'] = level * resistance * 1.5

        self._status['attack'] = force * level + (agility / 2)
        self._status['defense'] = resistance * level + (agility / 2)
        self._status['dodge'] = (agility + level) / 2
        self._status['critical'] = agility / 2
        self._status['luck'] = (level + agility) / 1.5

    def _assign_current_status(self):

        update = \
            [self._status_secondary['hp'], self._status_secondary['mp'], self._status_secondary['stamina']]

        for index, key in enumerate(self._current_status):
            self._current_status[key] = update[index]

    def _check_alive(self):

        if self._current_status['hp'] <= 0:
            self.alive = False
            self.kill()

    def _draw_name_level(self):

        draw_texts(MAIN_SCREEN, f'{self._attributes["name"]}'.replace('_', ' ').title(), self.rect.x + 120, self.rect.y)
        draw_texts(MAIN_SCREEN, f'Lvl - {self._attributes["level"]}'.title(), self.rect.x + 120, self.rect.y + 17)

    def _draw_bar_status(self):

        DrawStatusBar(100, 8, self._status_secondary['hp'], 100) \
            .draw(MAIN_SCREEN, COLORS['RED'], self.rect.x + 120, self.rect.y + 40, 8, self._current_status['hp'], color_bg=COLORS['BLACK'])

        DrawStatusBar(100, 8, self._status_secondary['mp'], 100) \
            .draw(MAIN_SCREEN, COLORS['BLUE'], self.rect.x + 120, self.rect.y + 48, 8, self._current_status['mp'], color_bg=COLORS['BLACK'])

        DrawStatusBar(100, 8, self._status_secondary['stamina'], 100) \
            .draw(MAIN_SCREEN, COLORS['GREEN'], self.rect.x + 120, self.rect.y + 54, 8, self._current_status['stamina'], color_bg=COLORS['BLACK'])

        DrawStatusBar(100, 8, self._attributes['level'] * 15, 100) \
            .draw(MAIN_SCREEN, COLORS['YELLOW'], self.rect.x + 120, self.rect.y + 62, 8, self._attributes['xp'], color_bg=COLORS['BLACK'])

    def _level_up(self):

        next_level = self._attributes['level'] * 15

        if self._attributes['xp'] >= next_level:

            self._attributes['level'] += 1
            self._attributes['xp'] = 1
            self._level_progression()

    def _level_progression(self):

        keys = 'force', 'vitality', 'agility', 'intelligence', 'resistance'

        for index, key in enumerate(keys):
            self._attributes[key] += 1

    def _loot(self):
        pass

    def events(self, event):

        pos_mouse = pg.mouse.get_pos()

        if event.type == pg.MOUSEBUTTONDOWN:
            pass

    def update(self):

        self._check_alive()
        self._assign_current_status()
        self._draw_bar_status()
        self._draw_name_level()
