from settings import COLORS, MAIN_SCREEN, pg


class DrawViews:

    def _draw_name_and_level(self):

        if not self.show_status_interface:

            name = self.attributes["name"].replace('_', ' ').title()
            level = self.attributes["level"]

            self.draw_render_status('{}'.format(name), self.rect.x + 120, self.rect.y)
            
            self.draw_render_status('Lvl - {}'.format(level), self.rect.x + 120, self.rect.y + 17)


    def _draw_status(self):

        if self.show_status_interface:

            pos_x, pos_y = self.rect.topright

            __RECT = pg.draw.rect(MAIN_SCREEN, COLORS['WHITE'], (pos_x - 2, pos_y - 7, 240, 100), 1, 0, 7, 7, 7, 7)

            y = pos_y - 5
            for key, value in self.attributes.items():

                if not key in 'name, level, rank, xp, class, ethnicity':

                    self.draw_render_status(f'{key.title():<} - {value:>}', pos_x + 5, y, size=13)
                    y += 20

            y = pos_y - 5
            for key, value in self.status.items():

                if not key in 'luck':

                    self.draw_render_status(f'{key.title():<} - {value:>.1f}', pos_x + 125, y, size=13)
                    y += 20