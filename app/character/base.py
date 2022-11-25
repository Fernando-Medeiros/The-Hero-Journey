from datetime import datetime

from .settings import *


class Entity:

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
        self.others = {
            'gold': 0,
            'soul': 0,
            'skills': [],
            'proficiency': [],
            'inventory': [],
            'equips': []
        }

    def level_progression(self) -> None:
        
        next_level = self.attributes['level'] * 15

        if self.attributes['xp'] >= next_level:
            
            if self.attributes['class'] == 'mage':
                data_progression = CLASS_PROGRESSION_MAGE
            else:
                data_progression = CLASS_PROGRESSION_MELEE

            for index, attribute in enumerate(BASIC_ATTRIBUTES):
                
                self.attributes[attribute] += data_progression[index]

            self.attributes['level'] += 1
            self.attributes['xp'] = 1

            self.assign_status_secondary()
            

    def assign_status_secondary(self) -> None:

        level = self.attributes['level']
        force = self.attributes['force']
        agility = self.attributes['agility']
        vitality = self.attributes['vitality']
        intelligence = self.attributes['intelligence']
        resistance = self.attributes['resistance']

        self.status_secondary['hp'] = (vitality / 2) * force + (level / 3)
        self.status_secondary['mp'] = (intelligence / 2) * resistance + (level / 3)
        self.status_secondary['stamina'] = (resistance / 2) + vitality

        self.status['attack'] = force + (agility / 3)
        self.status['defense'] = resistance + (agility / 3)
        self.status['dodge'] = agility / 10
        self.status['block'] = resistance / 10
        self.status['critical'] = agility / 20
        self.status['luck'] = level / 10


    def assign_current_status(self) -> None:

        self.current_status['hp'] = self.status_secondary['hp']
        self.current_status['mp'] = self.status_secondary['mp']
        self.current_status['stamina'] = self.status_secondary['stamina']


    def check_current_status(self) -> None:
        
        for key, value in self.current_status.items():
             if value <= 0: self.current_status.update({key: 0})

    def regenerate_status(self) -> None:
        time = datetime.today().second
        
        if time % 2 == 0:
        
            for status, value in self.current_status.items():
                if value < self.status_secondary[status]:
                    self.current_status[status] += self.status_secondary['regen_' + status]

    def __str__(self) -> str:
        return self.attributes['name']