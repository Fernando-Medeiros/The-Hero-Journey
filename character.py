from settings import *


class Character(pg.sprite.Sprite):

    @staticmethod
    def _unpack_four_basic_status(index):
        name, ethnicity, class_, level = check_records(FOLDER['save'])[index][:4]
        ethnicity, class_ = ethnicity.lower(), class_.lower()

        return name, ethnicity, class_, level

    def __init__(self, *groups):
        super().__init__(*groups)

        self.index = 0

        self.status = {
            'name': str,
            'ethnicity': str,
            'class': str,
            'level': int,
            'force': int,
            'agility': int,
            'vitality': int,
            'intelligence': int,
            'resistance': int,
            'rank': int,
            'xp': int
        }

        self.status_secondary = {
            'hp': int,
            'mp': int,
            'stamina': int
        }

        self.others = {
            'gold': 0,
            'soul': 0,
            'skills': [],
            'proficiency': [],
            'inventory': [],
            'equips': []
        }

        self.current_status = {
            'hp': int,
            'mp': int,
            'stamina': int,
            'xp': int
        }

        self._assign_status()

    def _assign_status(self):
        """
        Load data from specific file, and assign status values.
        """
        list_keys = [key for key in self.status]

        list_values = check_records(FOLDER['save'])[self.index]
        status = list_values + self._first_game() if len(list_values[:]) < 4 else list_values

        for _index, item in enumerate(status):
            if str(item).isnumeric():
                item = int(item)

            self.status[list_keys[_index]] = item

    def _assign_secondary(self):
        """
        Assigns secondary status based on instance attributes.
        """
        self.status_secondary['hp'] = self.status['level'] * self.status['vitality'] * self.status['force']
        self.status_secondary['mp'] = self.status['level'] * self.status['intelligence'] + self.status['resistance']
        self.status_secondary['stamina'] = self.status['level'] * self.status['resistance']

    def _assign_others(self):
        name, ethnicity, class_, level = self._unpack_four_basic_status(self.index)

        self.others['skills'].append(SKILLS[ethnicity[0] + '_' + class_][LANGUAGE])

    def _update_status(self):

        update =\
            [self.status_secondary['hp'], self.status_secondary['mp'], self.status_secondary['stamina'], self.status['xp']]

        for index, key in enumerate(self.current_status):
            self.current_status[key] = update[index]

    def _first_game(self):
        """
        Checks if it's the first time in the game, if so, returns the base status of the class and skills
        """
        name, ethnicity, class_, level = self._unpack_four_basic_status(self.index)

        if str(level) == '1':
            rank, experience = 1, 1

            folder = \
                DARK_ELF[class_] if 'dark' in ethnicity else FOREST_ELF[class_] if 'forest' in ethnicity else GREY_ELF[class_]

            folder.append(rank), folder.append(experience)

            return folder

    def _level_up(self):
        next_level = self.status['level'] * 15
        if self.status['xp'] >= next_level:
            self.status['level'] += 1
            self.status['xp'] = 0
            self._level_progression()

    def _level_progression(self):
        keys = 'force', 'vitality', 'agility', 'intelligence', 'resistance'

        upgrade_status = \
            class_progression_mage if str(self.status['class']).lower() == 'mage' else class_progression_melee

        for index, key in enumerate(keys):
            self.status[key] += upgrade_status[index]

    def save(self):
        with open(FOLDER['save'] + str(self.status['name']).lower(), mode='w+', encoding='utf-8') as file:

            for x in self.status.values():
                file.write(str(x).strip() + '\n')

    def _draw_bar_status(self):

        hp = DrawStatusBar(233, 30, self.status_secondary['hp'], 210)
        mp = DrawStatusBar(233, 30, self.status_secondary['mp'], 210)
        stamina = DrawStatusBar(233, 30, self.status_secondary['stamina'], 210)
        xp = DrawStatusBar(233, 30, self.status['xp'] + 1, 210)

        hp.draw(MAIN_SCREEN, COLORS['RED'], 173, 36, 15, self.current_status['hp'])
        mp.draw(MAIN_SCREEN, COLORS['BLUE'], 180, 54, 15, self.current_status['mp'])
        stamina.draw(MAIN_SCREEN, COLORS['GREEN'], 183, 72, 15, self.current_status['stamina'])
        xp.draw(MAIN_SCREEN, COLORS['YELLOW'], 185, 94, 15, self.current_status['xp'])

    def _draw_sprites_text(self):

        name, ethnicity, class_, level = self._unpack_four_basic_status(self.index)

        idd = 'ed_' if 'dark' in ethnicity.lower() else 'ef_' if 'forest' in ethnicity.lower() else 'eg_'

        # TEXT
        draw_texts(MAIN_SCREEN, name, 189, 8, size=20)
        draw_texts(MAIN_SCREEN, str(self.others['gold']), 477, 28, size=25)
        draw_texts(MAIN_SCREEN, str(self.others['soul']), 610, 28, size=25)

        # SPRITES
        background = pg.image.load(IMG_GAME['bg_char'])
        sprite = pg.image.load(IMG_CLASSES[idd + class_.lower()])

        drawing = [(background, (2, 1)), (sprite, (20, 18))]

        MAIN_SCREEN.blits(drawing)

    def events_character(self):
        pass

    def update(self, *args, **kwargs) -> None:

        if not self.others['skills']:
            self._assign_others()
            self._assign_status()

        self._level_up()
        self._assign_secondary()
        self._update_status()
        self._draw_bar_status()
        self._draw_sprites_text()
