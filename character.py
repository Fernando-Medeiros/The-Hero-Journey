from settings import *


class Character:

    @staticmethod
    def _unpack_basic_status(index):
        name, ethnicity, class_, level = check_records(FOLDER['save'])[index][:4]
        ethnicity, class_ = ethnicity.lower(), class_.lower()

        return name, ethnicity, class_, level

    show_status_interface = False

    def __init__(self):

        self.index = 0

        self._attributes = {
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

        self._button_status = DrawStatusBar(373, 30, 100, 373, rect=(15, 190))

    def _assign_basic_attributes(self):
        """
        Load data from specific file, and assign status values.
        """
        list_keys = [key for key in self._attributes]

        list_values = check_records(FOLDER['save'])[self.index]
        status = list_values + self._first_game() if len(list_values[:]) < 5 else list_values

        for _index, item in enumerate(status):
            if str(item).isnumeric():
                item = int(item)

            self._attributes[list_keys[_index]] = item

    def _assign_status_secondary(self):
        """
        Assigns secondary status based on instance attributes.
        """
        level, force, agility, vitality, intelligence, resistance = \
            list(self._attributes.values())[3:9]

        self.status_secondary['hp'] = level * vitality * force * 3.5
        self.status_secondary['mp'] = level * intelligence + resistance * 1.5
        self.status_secondary['stamina'] = level * resistance * 1.5

        self.status['attack'] = force * level + (agility / 2)
        self.status['defense'] = resistance * level + (agility / 2)
        self.status['dodge'] = (agility + level) / 2
        self.status['critical'] = agility / 2
        self.status['luck'] = (level + agility) / 1.5

    def _assign_others(self):
        name, ethnicity, class_, level = self._unpack_basic_status(self.index)

        self.others['skills'].append(SKILLS[ethnicity[0] + '_' + class_][LANGUAGE])

    def _update_status(self):

        update = \
            [self.status_secondary['hp'], self.status_secondary['mp'], self.status_secondary['stamina']]

        for index, key in enumerate(self.current_status):
            self.current_status[key] = update[index]

    def _first_game(self):
        """
        Checks if it's the first time in the game, if so, returns the base status of the class and skills
        """
        name, ethnicity, class_, level = self._unpack_basic_status(self.index)

        if str(level) == '1':
            folder = \
                DARK_ELF[class_] if 'dark' in ethnicity else FOREST_ELF[class_] if 'forest' in ethnicity else GREY_ELF[
                    class_]

            return folder

    def _level_up(self):

        next_level = self._attributes['level'] * 15

        if self._attributes['xp'] >= next_level:
            self._attributes['level'] += 1
            self._attributes['xp'] = 1
            self._level_progression()

    def _level_progression(self):
        keys = 'force', 'vitality', 'agility', 'intelligence', 'resistance'

        upgrade_status = \
            CLASS_PROGRESSION_MAGE if str(self._attributes['class']) == 'mage' else CLASS_PROGRESSION_MELEE

        for index, key in enumerate(keys):
            self._attributes[key] += upgrade_status[index]

    def _draw_bar_status(self):

        DrawStatusBar(233, 15, self.status_secondary['hp'], 222) \
            .draw(MAIN_SCREEN, COLORS['RED'], 173, 36, 15, self.current_status['hp'])

        DrawStatusBar(233, 15, self.status_secondary['mp'], 215) \
            .draw(MAIN_SCREEN, COLORS['BLUE'], 180, 54, 15, self.current_status['mp'])

        DrawStatusBar(233, 15, self.status_secondary['stamina'], 212) \
            .draw(MAIN_SCREEN, COLORS['GREEN'], 183, 72, 15, self.current_status['stamina'])

        DrawStatusBar(233, 15, self._attributes['level'] * 15, 210) \
            .draw(MAIN_SCREEN, COLORS['YELLOW'], 185, 90, 15, self._attributes['xp'])

    def _draw_sprites(self):

        ethnicity, class_ = self._attributes['ethnicity'], self._attributes['class']

        idd = 'ed_' if 'dark' in ethnicity else 'ef_' if 'forest' in ethnicity else 'eg_'

        background = pg.image.load(IMG_GAME['bg_char'])
        sprite = pg.image.load(IMG_CLASSES[idd + class_])

        drawing = [(background, (2, 1)), (sprite, (20, 18))]

        MAIN_SCREEN.blits(drawing)

    def _draw_text(self):

        draw_texts(MAIN_SCREEN, f'Lvl - {self._attributes["level"]}', 189, 110)
        draw_texts(MAIN_SCREEN, self._attributes['name'].title(), 189, 8, size=20)
        draw_texts(MAIN_SCREEN, str(self.others['gold']), 477, 28, size=25)
        draw_texts(MAIN_SCREEN, str(self.others['soul']), 610, 28, size=25)

        draw_texts(
            MAIN_SCREEN, f'{self.current_status["hp"]:^25.1f}/{self.status_secondary["hp"]:^25.1f}', 185, 36, size=13)
        draw_texts(
            MAIN_SCREEN, f'{self.current_status["mp"]:^25.1f}/{self.status_secondary["mp"]:^25.1f}', 185, 54, size=13)
        draw_texts(
            MAIN_SCREEN, f'{self.current_status["stamina"]:^25.1f}/{self.status_secondary["stamina"]:^25.1f}', 185, 72,
            size=13)
        draw_texts(
            MAIN_SCREEN, f'{self._attributes["xp"]:^25.1f}/{self._attributes["level"] * 15:^25.1f}', 185, 90, size=13)

    def _draw_status(self):

        self._button_status.draw(MAIN_SCREEN, COLORS['BLUE_2'], 15, 190, 30, 100)
        draw_texts(MAIN_SCREEN, f'{"Status"}', 170, 190, size=25)

        if self.show_status_interface:
            DrawStatusBar(1, 1, 100, 373).draw(MAIN_SCREEN, COLORS['BLACK'], 15, 220, 150, 0)

            y = 230
            for key, value in self._attributes.items():
                if not key in 'name, level, rank, xp':
                    draw_texts(MAIN_SCREEN, f'{key.title():<} - {value:>}', 20, y)
                    y += 20

            y = 230
            for key, value in self.status.items():
                draw_texts(MAIN_SCREEN, f'{key.title():<} - {value:>.1f}', 206, y)
                y += 20

    def _get_mouse_events(self, pos_mouse):

        if self._button_status.rect.collidepoint(pos_mouse):
            self.show_status_interface = True
        else:
            self.show_status_interface = False

    def save(self):

        with open(FOLDER['save'] + str(self._attributes['name']).lower(), mode='w+', encoding='utf-8') as file:
            for x in self._attributes.values():
                file.write(str(x).strip() + '\n')

        self.others['skills'].clear()

    def events_character(self, event):

        pos_mouse = pg.mouse.get_pos()

        if event.type == pg.MOUSEBUTTONDOWN:
            self._get_mouse_events(pos_mouse)

    def update(self, *args, **kwargs):

        if not self.others['skills']:
            self._assign_basic_attributes()
            self._assign_others()

        self._assign_status_secondary()
        self._update_status()
        self._draw_bar_status()
        self._draw_sprites()
        self._draw_text()
        self._draw_status()
        self._level_up()
