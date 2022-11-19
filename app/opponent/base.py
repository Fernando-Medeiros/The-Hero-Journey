from datetime import datetime

from ..character.settings import BASIC_ATTRIBUTES


class BaseEntity:
    def __init__(self):
        
        self.entity = {
            'attributes': {
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
                'xp': 1,
                'sprite': '',
                },
            'secondary': {
                'hp': 1,
                'mp': 1,
                'stamina': 1,
                'regen_hp': 0.005,
                'regen_mp': 0.005,
                'regen_stamina': 0.009
            },
            'current': {
                'hp': 1,
                'mp': 1,
                'stamina': 1    
            },
            'status': {
                'attack': 1,
                'defense': 1,
                'dodge': 1,
                'block': 1,
                'critical': 1,
                'luck': 1    
            },
        }

    def level_up(self) -> bool:

        next_level = self.entity['attributes']['level'] * 15

        if self.entity['attributes']['xp'] >= next_level:
            return True
        return False


    def level_progression_enemy(self, level_up):

        if level_up:

            list_attributes = BASIC_ATTRIBUTES

            for attribute in list_attributes:

                self.entity['attributes'][attribute] += 1

            self.entity['attributes']['level'] += 1
            self.entity['attributes']['xp'] = 1

            self.assign_status_secondary()


    def assign_status_secondary(self):

        level, force, agility, vitality, intelligence, resistance = \
            list(self.entity['attributes'].values())[3:9]

        self.entity['secondary']['hp'] = (vitality / 2) * force + (level / 3)
        self.entity['secondary']['mp'] = (intelligence / 2) * resistance + (level / 3)
        self.entity['secondary']['stamina'] = (resistance / 2) + vitality

        self.entity['status']['attack'] = force + (agility / 3)
        self.entity['status']['defense'] = resistance + (agility / 3)
        self.entity['status']['dodge'] = agility / 10
        self.entity['status']['block'] = resistance / 10
        self.entity['status']['critical'] = agility / 20
        self.entity['status']['luck'] = level / 10


    def assign_current_status(self):

        self.entity['current']['hp'] = self.entity['secondary']['hp']
        self.entity['current']['mp'] = self.entity['secondary']['mp']
        self.entity['current']['stamina'] = self.entity['secondary']['stamina']


    def check_current_status(self):

        for key, value in self.entity['current'].items():

            if value <= 0:
                self.entity['current'][key] = 0


    def status_regen(self):

        time = datetime.today().second

        if time % 2 == 0:
            for status, value in self.entity['current'].items():

                if value < self.entity['secondary'][status]:

                    self.entity['current'][status] += self.entity['secondary']['regen_' + status]
