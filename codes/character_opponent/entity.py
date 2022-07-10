from settings import *


class Entity:

    show_status_interface = False

    def __init__(self):

        self.attributes = {
            'name': '',
            'ethnicity': '',
            'class': '',
            'level': 1,
            'force': 1,
            'agility': 1,
            'vitality': 1,
            'intelligence': 1,
            'resistance': 1,
            'rank': 1,
            'xp': 1
        }
        self.status_secondary = {
            'hp': 1,
            'mp': 1,
            'stamina': 1,
            'regen_hp': 0.002,
            'regen_mp': 0.002,
            'regen_stamina': 0.002
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

    def level_up(self):

        next_level = self.attributes['level'] * 15

        if self.attributes['xp'] >= next_level:

            return True
        else:
            return False

    def level_progression(self, level_up):

        if level_up:

            keys = 'force', 'vitality', 'agility', 'intelligence', 'resistance'

            data_progression = CLASS_PROGRESSION_MAGE if self.attributes['class'] == 'mage' else CLASS_PROGRESSION_MELEE

            for __index__, __key__ in enumerate(keys):
                self.attributes[__key__] += data_progression[__index__]

            self.attributes['level'] += 1
            self.attributes['xp'] = 1

            self.assign_status_secondary()

    def level_progression_enemy(self, level_up):

        if level_up:

            keys = 'force', 'vitality', 'agility', 'intelligence', 'resistance'

            for __key__ in keys:

                self.attributes[__key__] += 1

            self.attributes['level'] += 1
            self.attributes['xp'] = 1

            self.assign_status_secondary()

    def assign_status_secondary(self):

        level, force, agility, vitality, intelligence, resistance = \
            list(self.attributes.values())[3:9]

        self.status_secondary['hp'] = (vitality / 2) * force
        self.status_secondary['mp'] = (intelligence / 2) * resistance
        self.status_secondary['stamina'] = (resistance / 2) + vitality

        self.status['attack'] = force + (agility / 2)
        self.status['defense'] = resistance + (agility / 2)
        self.status['dodge'] = agility / 3
        self.status['block'] = resistance / 3
        self.status['critical'] = agility / 5
        self.status['luck'] = level / 8

    def assign_current_status(self):

        self.current_status['hp'] = self.status_secondary['hp']
        self.current_status['mp'] = self.status_secondary['mp']
        self.current_status['stamina'] = self.status_secondary['stamina']

    def check_current_status(self):

        for __key__, __value__ in self.current_status.items():

            if __value__ <= 0:

                self.current_status[__key__] = 0

    def status_regen(self):

        time = datetime.today().second

        if time % 2 == 0:

            for __key__, __value__ in self.current_status.items():

                if __value__ < self.status_secondary[__key__]:

                    self.current_status[__key__] += self.status_secondary['regen_' + __key__]

    @staticmethod
    def draw_render_status(TXT: str, X, Y, size=15, color=(255, 255, 255)):

        font = pg.font.SysFont('arial', size, True)
        text = font.render(f'{TXT}', True, color)

        MAIN_SCREEN.blit(text, (X, Y))

    @staticmethod
    def draw_status_bar(height, fixed_value, max_size, color, rect: (int, int), current_value):

        __size_max = max_size
        __current_size = fixed_value / __size_max

        border = 0, 7, 7, 7, 7

        pg.draw.rect(MAIN_SCREEN, color, (*rect, current_value / __current_size, height), *border)
        pg.draw.rect(MAIN_SCREEN, COLORS['WHITE'], (*rect, __size_max, height), 1, *border)
