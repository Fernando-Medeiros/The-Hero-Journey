from codes.character_opponent.entity import *


class Character(Entity):

    @staticmethod
    def _unpack_basic_status(index):
        name, ethnicity, class_, level = check_records(FOLDER['save'])[index][:4]

        return name, ethnicity, class_, level

    def __init__(self):

        super().__init__()

        self.index = 0

        self.others = {
            'gold': 0,
            'soul': 0,
            'skills': [],
            'proficiency': [],
            'inventory': [],
            'equips': []
        }

        self._button_status = pg.rect.Rect(15, 190, 373, 30)

    def _assign_basic_attributes(self):

        __list_keys__ = [key for key in self.attributes]

        list_values = check_records(FOLDER['save'])[self.index]

        status = list_values + self._first_game() if len(list_values[:]) < 5 else list_values

        for __index__, __item__ in enumerate(status):

            __item__ = int(__item__) if str(__item__).isnumeric() else __item__

            self.attributes[__list_keys__[__index__]] = __item__

    def _assign_others(self):

        name, ethnicity, class_, level = self._unpack_basic_status(self.index)

        self.others['skills'].append(SKILLS[ethnicity[0] + '_' + class_][LANGUAGE])

    def _first_game(self):

        name, ethnicity, class_, level = self._unpack_basic_status(self.index)

        folder = DARK_ELF if 'dark' in ethnicity else FOREST_ELF if 'forest' in ethnicity else GREY_ELF

        if str(level) == '1':

            return folder[class_]

    def _draw_bar_status(self):

        __pos = [[173, 36], [180, 54], [183, 72], [185, 90]]
        __max_size = [222, 215, 212, 210]

        colors = [COLORS['RED'], COLORS['BLUE'], COLORS['GREEN'], COLORS['YELLOW']]

        info_0 = [
            self.status_secondary['hp'], self.status_secondary['mp'],
            self.status_secondary['stamina'], self.attributes['level'] * 15
        ]
        info_1 = [
            self.current_status['hp'], self.current_status['mp'],
            self.current_status['stamina'], self.attributes['xp']
        ]

        for __index__ in range(len(info_0)):

            self.draw_status_bar(
                15, info_0[__index__], __max_size[__index__], colors[__index__], __pos[__index__], info_1[__index__])

    def _draw_sprites(self):

        ethnicity, class_ = self.attributes['ethnicity'], self.attributes['class']

        idd = 'ed_' if 'dark' in ethnicity else 'ef_' if 'forest' in ethnicity else 'eg_'

        sprite = pg.image.load(IMG_CLASSES[idd + class_])

        MAIN_SCREEN.blit(sprite, (20, 18))

    def _draw_info_status(self):

        self.draw_render_status(f'Lvl - {self.attributes["level"]}', 189, 110)
        self.draw_render_status(str(self.attributes['name']).title(), 189, 8, size=20)
        self.draw_render_status(str(self.others['gold']), 477, 28, size=25)
        self.draw_render_status(str(self.others['soul']), 610, 28, size=25)

        info = [
            f'{self.current_status["hp"]:^21.1f}/{self.status_secondary["hp"]:^21.1f}',
            f'{self.current_status["mp"]:^21.1f}/{self.status_secondary["mp"]:^21.1f}',
            f'{self.current_status["stamina"]:^21.1f}/{self.status_secondary["stamina"]:^21.1f}',
            f'{self.attributes["xp"]:^21.1f}/{self.attributes["level"] * 15:^21.1f}'
        ]

        __x, __y = 185, 36
        for __item__ in info:

            self.draw_render_status(__item__, __x, __y, size=13)

            __y += 18

    def _draw_status(self):

        pg.draw.rect(MAIN_SCREEN, COLORS['WHITE'], self._button_status, 1, 0, 7, 7, 7, 7)

        self.draw_render_status(f'{"Status"}', 170, 190, size=25)

        if self.show_status_interface:

            __RECT = pg.draw.rect(MAIN_SCREEN, COLORS['WHITE'], (15, 220, 373, 150), 1, 0, 7, 7, 7, 7)

            y = 230
            for __key__, __value__ in self.attributes.items():

                if not __key__ in 'name, level, rank, xp':
                    self.draw_render_status(f'{__key__.title():<} - {__value__:>}', 20, y)
                    y += 20

            y = 230
            for __key__, __value__ in self.status.items():

                self.draw_render_status(f'{__key__.title():<} - {__value__:>.1f}', 206, y)
                y += 20

    def _show_status(self, pos_mouse):

        if self._button_status.collidepoint(pos_mouse):
            self.show_status_interface = True
        else:
            self.show_status_interface = False

    def save(self):

        with open(FOLDER['save'] + str(self.attributes['name']).lower(), mode='w+', encoding='utf-8') as __file__:

            for __x__ in self.attributes.values():

                __file__.write(str(__x__).strip() + '\n')

        self.others['skills'].clear()

    def events_character(self, event):

        pos_mouse = pg.mouse.get_pos()

        if event.type == pg.MOUSEBUTTONDOWN:

            self._show_status(pos_mouse)

    def update(self):

        if not self.others['skills']:

            self._assign_basic_attributes()

            self.assign_status_secondary()

            self.assign_current_status()

            self._assign_others()

        self.check_current_status()
        self._draw_bar_status()
        self._draw_sprites()
        self._draw_info_status()
        self._draw_status()
        self.status_regen()

        self.level_progression(self.level_up())
