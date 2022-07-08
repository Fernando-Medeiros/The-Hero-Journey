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

        self._button_status = DrawStatusBar(373, 30, 100, 373, rect=(15, 190))

    def _assign_basic_attributes(self):

        list_keys = [key for key in self.attributes]

        list_values = check_records(FOLDER['save'])[self.index]

        status = list_values + self._first_game() if len(list_values[:]) < 5 else list_values

        for _index, item in enumerate(status):

            item = int(item) if str(item).isnumeric() else item

            self.attributes[list_keys[_index]] = item

    def _assign_others(self):
        name, ethnicity, class_, level = self._unpack_basic_status(self.index)

        self.others['skills'].append(SKILLS[ethnicity[0] + '_' + class_][LANGUAGE])

    def _first_game(self):

        name, ethnicity, class_, level = self._unpack_basic_status(self.index)

        folder =\
            DARK_ELF[class_] if 'dark' in ethnicity else FOREST_ELF[class_] if 'forest' in ethnicity else GREY_ELF[class_]

        if str(level) == '1':

            return folder

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

            draw = DrawStatusBar(233, 15, info_0[__index__], __max_size[__index__])
            draw.draw(MAIN_SCREEN, colors[__index__], *__pos[__index__], 15, info_1[__index__])

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
        for item in info:

            self.draw_render_status(item, __x, __y, size=13)

            __y += 18

    def _draw_status(self):

        self._button_status.draw(MAIN_SCREEN, COLORS['BLACK'], 15, 190, 30, 0)
        self.draw_render_status(f'{"Status"}', 170, 190, size=25)

        if self.show_status_interface:
            DrawStatusBar(1, 1, 100, 373).draw(MAIN_SCREEN, COLORS['BLACK'], 15, 220, 150, 0)

            y = 230
            for key, value in self.attributes.items():

                if not key in 'name, level, rank, xp':
                    self.draw_render_status(f'{key.title():<} - {value:>}', 20, y)
                    y += 20

            y = 230
            for key, value in self.status.items():

                self.draw_render_status(f'{key.title():<} - {value:>.1f}', 206, y)
                y += 20

    def _show_status(self, pos_mouse):

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
            self._show_status(pos_mouse)

    def update(self, *args, **kwargs):

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
