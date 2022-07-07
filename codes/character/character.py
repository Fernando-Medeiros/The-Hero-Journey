from settings import *


class Character:

    @staticmethod
    def _unpack_basic_status(index):
        name, ethnicity, class_, level = check_records(FOLDER['save'])[index][:4]

        return name, ethnicity, class_, level

    show_status_interface = False
    load_char = False

    def __init__(self):

        self.index = 0

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
            'regen_hp': 0.001,
            'regen_mp': 0.001,
            'regen_stamina': 0.001
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

        self._button_status = DrawStatusBar(373, 30, 100, 373, rect=(15, 190))

    def _assign_basic_attributes(self):

        list_keys = [key for key in self.attributes]

        list_values = check_records(FOLDER['save'])[self.index]

        status = list_values + self._first_game() if len(list_values[:]) < 5 else list_values

        for _index, item in enumerate(status):

            item = int(item) if str(item).isnumeric() else item

            self.attributes[list_keys[_index]] = item

    def _assign_status_secondary(self):

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

    def _assign_others(self):
        name, ethnicity, class_, level = self._unpack_basic_status(self.index)

        self.others['skills'].append(SKILLS[ethnicity[0] + '_' + class_][LANGUAGE])

    def _assign_current_status(self):

        self.current_status['hp'] = self.status_secondary['hp']
        self.current_status['mp'] = self.status_secondary['mp']
        self.current_status['stamina'] = self.status_secondary['stamina']

    def _check_current_status(self):

        self.current_status['hp'] = 0 if self.current_status['hp'] <= 0 else self.current_status['hp']

        self.current_status['mp'] = 0 if self.current_status['mp'] <= 0 else self.current_status['mp']

        self.current_status['stamina'] = 0 if self.current_status['stamina'] <= 0 else self.current_status['stamina']

    def _first_game(self):

        name, ethnicity, class_, level = self._unpack_basic_status(self.index)

        if str(level) == '1':
            folder = \
                DARK_ELF[class_] if 'dark' in ethnicity else FOREST_ELF[class_] if 'forest' in ethnicity else GREY_ELF[
                    class_]

            return folder

    def _regen(self):

        time = datetime.today().second
        if time % 2 == 0:

            if self.current_status['hp'] < self.status_secondary['hp']:
                self.current_status['hp'] += self.status_secondary['regen_hp']

            if self.current_status['mp'] < self.status_secondary['mp']:
                self.current_status['mp'] += self.status_secondary['regen_mp']

            if self.current_status['stamina'] < self.status_secondary['stamina']:
                self.current_status['stamina'] += self.status_secondary['regen_stamina']

    def _level_up(self):

        next_level = self.attributes['level'] * 15

        if self.attributes['xp'] >= next_level:

            self.attributes['level'] += 1
            self.attributes['xp'] = 1
            self._level_progression()
            self._assign_status_secondary()

    def _level_progression(self):

        keys = 'force', 'vitality', 'agility', 'intelligence', 'resistance'

        upgrade_status = \
            CLASS_PROGRESSION_MAGE if str(self.attributes['class']) == 'mage' else CLASS_PROGRESSION_MELEE

        for index, key in enumerate(keys):
            self.attributes[key] += upgrade_status[index]

    def _draw_bar_status(self):

        DrawStatusBar(233, 15, self.status_secondary['hp'], 222) \
            .draw(MAIN_SCREEN, COLORS['RED'], 173, 36, 15, self.current_status['hp'])

        DrawStatusBar(233, 15, self.status_secondary['mp'], 215) \
            .draw(MAIN_SCREEN, COLORS['BLUE'], 180, 54, 15, self.current_status['mp'])

        DrawStatusBar(233, 15, self.status_secondary['stamina'], 212) \
            .draw(MAIN_SCREEN, COLORS['GREEN'], 183, 72, 15, self.current_status['stamina'])

        DrawStatusBar(233, 15, self.attributes['level'] * 15, 210) \
            .draw(MAIN_SCREEN, COLORS['YELLOW'], 185, 90, 15, self.attributes['xp'])

    def _draw_sprites(self):

        ethnicity, class_ = self.attributes['ethnicity'], self.attributes['class']

        idd = 'ed_' if 'dark' in ethnicity else 'ef_' if 'forest' in ethnicity else 'eg_'

        sprite = pg.image.load(IMG_CLASSES[idd + class_])

        MAIN_SCREEN.blit(sprite, (20, 18))

    def _draw_text(self):

        draw_texts(MAIN_SCREEN, f'Lvl - {self.attributes["level"]}', 189, 110)
        draw_texts(MAIN_SCREEN, str(self.attributes['name']).title(), 189, 8, size=20)
        draw_texts(MAIN_SCREEN, str(self.others['gold']), 477, 28, size=25)
        draw_texts(MAIN_SCREEN, str(self.others['soul']), 610, 28, size=25)

        draw_texts(
            MAIN_SCREEN, f'{self.current_status["hp"]:^21.1f}/{self.status_secondary["hp"]:^21.1f}', 185, 36, size=13)
        draw_texts(
            MAIN_SCREEN, f'{self.current_status["mp"]:^21.1f}/{self.status_secondary["mp"]:^21.1f}', 185, 54, size=13)
        draw_texts(
            MAIN_SCREEN, f'{self.current_status["stamina"]:^21.1f}/{self.status_secondary["stamina"]:^21.1f}', 185, 72,
            size=13)
        draw_texts(
            MAIN_SCREEN, f'{self.attributes["xp"]:^21.1f}/{self.attributes["level"] * 15:^21.1f}', 185, 90, size=13)

    def _draw_status(self):

        self._button_status.draw(MAIN_SCREEN, COLORS['BLACK'], 15, 190, 30, 0)
        draw_texts(MAIN_SCREEN, f'{"Status"}', 170, 190, size=25)

        if self.show_status_interface:
            DrawStatusBar(1, 1, 100, 373).draw(MAIN_SCREEN, COLORS['BLACK'], 15, 220, 150, 0)

            y = 230
            for key, value in self.attributes.items():
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

        with open(FOLDER['save'] + str(self.attributes['name']).lower(), mode='w+', encoding='utf-8') as file:

            for x in self.attributes.values():

                file.write(str(x).strip() + '\n')

        self.others['skills'].clear()

    def events_character(self, event):

        pos_mouse = pg.mouse.get_pos()

        if event.type == pg.MOUSEBUTTONDOWN:
            self._get_mouse_events(pos_mouse)

    def update(self, *args, **kwargs):

        if not self.others['skills']:

            self._assign_basic_attributes()
            self._assign_status_secondary()
            self._assign_current_status()
            self._assign_others()

        self._check_current_status()
        self._draw_bar_status()
        self._draw_sprites()
        self._draw_text()
        self._draw_status()
        self._level_up()
        self._regen()
