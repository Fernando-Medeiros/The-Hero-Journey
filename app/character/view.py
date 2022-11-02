from settings import COLORS, IMG_CLASSES, MAIN_SCREEN, pg


class View:

    def _draw_bar_status(self):

        pos = [[173, 36], [180, 54], [183, 72], [185, 90]]
        max_size = [222, 215, 212, 210]

        colors = [COLORS['RED'], COLORS['BLUE'], COLORS['GREEN'], COLORS['YELLOW']]

        info_0 = [
            self.status_secondary['hp'], self.status_secondary['mp'],
            self.status_secondary['stamina'], self.attributes['level'] * 15
        ]
        info_1 = [
            self.current_status['hp'], self.current_status['mp'],
            self.current_status['stamina'], self.attributes['xp']
        ]

        for index in range(len(info_0)):

            self.draw_status_bar(
                15, info_0[index], max_size[index], colors[index], pos[index], info_1[index])


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
            '{:^21.1f}/{:^21.1f}'.format(self.current_status["hp"], self.status_secondary["hp"]),
            '{:^21.1f}/{:^21.1f}'.format(self.current_status["mp"], self.status_secondary["mp"]),
            '{:^21.1f}/{:^21.1f}'.format(self.current_status["stamina"], self.status_secondary["stamina"]),
            '{:^21.1f}/{:^21.1f}'.format(self.attributes["xp"], self.attributes["level"] * 15)
        ]

        x, y = 185, 36
        for item in info:

            self.draw_render_status(item, x, y, size=13)

            y += 18


    def _draw_status(self):

        pg.draw.rect(MAIN_SCREEN, COLORS['WHITE'], self._button_status, 1, 0, 7, 7, 7, 7)

        self.draw_render_status(f'{"Status"}', 170, 190, size=25)

        if self.show_status_interface:

            __RECT = pg.draw.rect(MAIN_SCREEN, COLORS['WHITE'], (15, 220, 373, 150), 1, 0, 7, 7, 7, 7)

            y = 230
            for key, value in self.attributes.items():

                if not key in 'name, level, rank, xp':
                    self.draw_render_status(f'{key.title():<} - {value:>}', 20, y)
                    y += 20

            y = 230
            for key, value in self.status.items():

                self.draw_render_status(f'{key.title():<} - {value:>.1f}', 206, y)
                y += 20
