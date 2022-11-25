from datetime import datetime


class Entity:

    alive = True
    
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
                'gold': 1,
                'soul': 1,
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


    def assign_status_secondary(self) -> None:

        level = self.entity['attributes']['level']
        force = self.entity['attributes']['force']
        agility = self.entity['attributes']['agility']
        vitality = self.entity['attributes']['vitality']
        intelligence = self.entity['attributes']['intelligence']
        resistance = self.entity['attributes']['resistance']

        self.entity['secondary']['hp'] = (vitality / 2) * force + (level / 3)
        self.entity['secondary']['mp'] = (intelligence / 2) * resistance + (level / 3)
        self.entity['secondary']['stamina'] = (resistance / 2) + vitality

        self.entity['status']['attack'] = force + (agility / 3)
        self.entity['status']['defense'] = resistance + (agility / 3)
        self.entity['status']['dodge'] = agility / 10
        self.entity['status']['block'] = resistance / 10
        self.entity['status']['critical'] = agility / 20
        self.entity['status']['luck'] = level / 10


    def assign_current_status(self) -> None:

        self.entity['current']['hp'] = self.entity['secondary']['hp']
        self.entity['current']['mp'] = self.entity['secondary']['mp']
        self.entity['current']['stamina'] = self.entity['secondary']['stamina']


    def _check_current_status(self) -> None:

        for key, value in self.entity['current'].items():

            if value <= 0:
                self.entity['current'][key] = 0


    def regenerate_status(self) -> None:

        time = datetime.today().second

        if time % 2 == 0:
            for status, value in self.entity['current'].items():

                if value < self.entity['secondary'][status]:

                    self.entity['current'][status] += self.entity['secondary']['regen_' + status]


    def _is_alive(self) -> None:
        
        self.regenerate_status()

        if self.entity['current']['hp'] <= 0.1:

            self.alive = False
    
    
    def __str__(self) -> str:
        return self.entity['attributes']['name']