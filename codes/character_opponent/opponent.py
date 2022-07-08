from codes.character_opponent.entity import *


class Enemy(Entity, Obj):

    show_status_interface = False

    def __init__(self, list_,  img, x, y, *groups):

        Obj.__init__(self, img, x, y, *groups)

        Entity.__init__(self)

        self.instance_data = list_

        self.loots = {
            'gold': 1,
            'soul': 1,
            'xp': 1
        }
        self.list_of_loots = []

        self._assign_attributes()
        self.assign_status_secondary()
        self.assign_current_status()

    def _assign_attributes(self):

        list_key = ['name', 'level', 'force', 'agility', 'vitality', 'intelligence', 'resistance']

        for index, value in enumerate(self.instance_data[1:]):
            value = int(value) if str(value).isnumeric() else str(value)

            self.attributes[list_key[index]] = value

    def _draw_name_and_level(self):

        self.draw_render_status(f'{self.attributes["name"]}'.replace('_', ' ').title(), self.rect.x + 120, self.rect.y)
        self.draw_render_status(f'Lvl - {self.attributes["level"]}'.title(), self.rect.x + 120, self.rect.y + 17)

    def _draw_status(self):

        if self.show_status_interface:

            pos_x, pos_y = self.rect.topright

            DrawStatusBar(1, 1, 100, 240).draw(MAIN_SCREEN, COLORS['PURPLE'], pos_x, pos_y, 100, 100)

            y = pos_y
            for key, value in self.attributes.items():

                if not key in 'name, level, rank, xp, class, ethnicity':
                    self.draw_render_status(f'{key.title():<} - {value:>}', pos_x + 5, y, size=13)
                    y += 20

            y = pos_y
            for key, value in self.status.items():

                if not key in 'luck':
                    self.draw_render_status(f'{key.title():<} - {value:>.1f}', pos_x + 125, y, size=13)
                    y += 20

    def _show_status(self, pos_mouse):

        if self.rect.collidepoint(pos_mouse):
            self.show_status_interface = True
        else:
            self.show_status_interface = False

    def events(self, event):

        pos_mouse = pg.mouse.get_pos()

        if event.type == pg.MOUSEMOTION:
            self._show_status(pos_mouse)

    def update(self):

        self.check_current_status()
        self.status_regen()
        self.level_progression_enemy(self.level_up())

        self._draw_name_and_level()
        self._draw_status()
