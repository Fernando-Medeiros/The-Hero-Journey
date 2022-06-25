from settings import *


class Character(pg.sprite.Sprite):

    def __init__(self, *groups):
        super().__init__(*groups)

        self.status = {
            'name': None,
            'ethnicity': None,
            'class': None,
            'level': None,
            'force': None,
            'agility': None,
            'vitality': None,
            'intelligence': None,
            'resistance': None,
            'rank': None,
            'hp': None,
            'mp': None,
            'stamina': None
        }

        self.others = {
            'gold': None,
            'soul': None,
            'skills': [],
            'proficiency': [],
            'inventory': [],
            'equips': []
        }

    def assign_status(self, index=0):
        """
        Load data from specific file, and assign status values.
        """
        list_keys = [key for key in self.status]

        status = check_records(FOLDER['save'])[index] + self.first_game(index)

        for index, item in enumerate(status):
            self.status[list_keys[index]] = item

    def first_game(self, index):
        """
        Checks if it's the first time in the game, if so, returns the base status of the class and skills
        """

        name, ethnicity, class_, level = check_records(FOLDER['save'])[index][:4]
        ethnicity, class_ = ethnicity.lower(), class_.lower()

        self.others['skills'].append(SKILLS[ethnicity[0] + '_' + class_][LANGUAGE])

        if str(level) == '1' and len(check_records(FOLDER['save'])) < 5:
            rank = 1

            folder = DARK_ELF[class_] if 'dark' in ethnicity else FOREST_ELF[class_] \
                if 'forest' in ethnicity else GREY_ELF[class_]

            folder.append(rank)

            return folder

    def assign_secondaries(self):
        """
        Assigns secondary status based on instance attributes.
        """
        self.status['hp'] = int(self.status['level']) * int(self.status['vitality']) * int(self.status['force'])
        self.status['mp'] = int(self.status['level']) * int(self.status['intelligence']) + int(self.status['resistance'])
        self.status['stamina'] = int(self.status['level']) * int(self.status['resistance'])

