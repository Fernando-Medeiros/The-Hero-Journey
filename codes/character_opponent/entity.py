from settings import *
from paths import *


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

            for index, key in enumerate(keys):
                self.attributes[key] += data_progression[index]

            self.attributes['level'] += 1
            self.attributes['xp'] = 1

            self.assign_status_secondary()

    def level_progression_enemy(self, level_up):

        if level_up:
            keys = 'force', 'vitality', 'agility', 'intelligence', 'resistance'

            for index, key in enumerate(keys):
                self.attributes[key] += 1

            self.attributes['level'] += 1
            self.attributes['xp'] = 1

            self.assign_status_secondary()

    def assign_status_secondary(self):

        level, force, agility, vitality, intelligence, resistance = \
            list(self.attributes.values())[3:9]

        self.status_secondary['hp'] = level * vitality * force * 3.5
        self.status_secondary['mp'] = level * intelligence + resistance * 1.5
        self.status_secondary['stamina'] = level * resistance * 1.5

        self.status['attack'] = force * level + (agility / 2)
        self.status['defense'] = resistance * level + (agility / 2)
        self.status['dodge'] = (agility + level) / 4
        self.status['block'] = (agility + resistance) / 4
        self.status['critical'] = agility / 4
        self.status['luck'] = (level + agility) / 4

    def assign_current_status(self):

        self.current_status['hp'] = self.status_secondary['hp']
        self.current_status['mp'] = self.status_secondary['mp']
        self.current_status['stamina'] = self.status_secondary['stamina']

    def check_current_status(self):

        self.current_status['hp'] = 0 if self.current_status['hp'] <= 0 else self.current_status['hp']

        self.current_status['mp'] = 0 if self.current_status['mp'] <= 0 else self.current_status['mp']

        self.current_status['stamina'] = 0 if self.current_status['stamina'] <= 0 else self.current_status['stamina']

    def status_regen(self):

        time = datetime.today().second

        if time % 2 == 0:

            current_, secondary_ = self.current_status,  self.status_secondary

            if current_['hp'] < secondary_['hp']:
                self.current_status['hp'] += secondary_['regen_hp']

            if current_['mp'] < secondary_['mp']:
                self.current_status['mp'] += secondary_['regen_mp']

            if current_['stamina'] < secondary_['stamina']:
                self.current_status['stamina'] += secondary_['regen_stamina']

    @staticmethod
    def draw_render_status(TXT: str, X, Y, size=15, color=(255, 255, 255)):

        font = pg.font.SysFont('arial', size, True)
        text = font.render(f'{TXT}', True, color)

        MAIN_SCREEN.blit(text, (X, Y))
