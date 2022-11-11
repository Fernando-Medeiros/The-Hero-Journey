from datetime import datetime
from ..character.settings import BASIC_ATTRIBUTES

class BaseEntity:

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
            'regen_hp': 0.005,
            'regen_mp': 0.005,
            'regen_stamina': 0.009
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


    def level_up(self) -> bool:

        next_level = self.attributes['level'] * 15

        if self.attributes['xp'] >= next_level:
            return True
        
        return False


    def level_progression_enemy(self, level_up):

        if level_up:

            list_attributes = BASIC_ATTRIBUTES

            for attribute in list_attributes:

                self.attributes[attribute] += 1

            self.attributes['level'] += 1
            self.attributes['xp'] = 1

            self.assign_status_secondary()


    def assign_status_secondary(self):

        level, force, agility, vitality, intelligence, resistance = \
            list(self.attributes.values())[3:9]

        self.status_secondary['hp'] = (vitality / 2) * force + (level / 3)
        self.status_secondary['mp'] = (intelligence / 2) * resistance + (level / 3)
        self.status_secondary['stamina'] = (resistance / 2) + vitality

        self.status['attack'] = force + (agility / 3)
        self.status['defense'] = resistance + (agility / 3)
        self.status['dodge'] = agility / 10
        self.status['block'] = resistance / 10
        self.status['critical'] = agility / 20
        self.status['luck'] = level / 10


    def assign_current_status(self):

        self.current_status['hp'] = self.status_secondary['hp']
        self.current_status['mp'] = self.status_secondary['mp']
        self.current_status['stamina'] = self.status_secondary['stamina']


    def check_current_status(self):

        for key, value in self.current_status.items():

            if value <= 0:

                self.current_status[key] = 0


    def status_regen(self):

        time = datetime.today().second

        if time % 2 == 0:

            for status, value in self.current_status.items():

                if value < self.status_secondary[status]:

                    self.current_status[status] += self.status_secondary['regen_' + status]
