from settings import (
    FOLDER, DARK_ELF, FOREST_ELF, SKILLS, GREY_ELF,
    check_records, pg)

from .base import BaseEntity
from .view import View



class Character(BaseEntity, View):

    def __init__(self):

        super().__init__()
        View.__init__(self)
        
        self.index = 0

        self.location = 'Sea North'

        self.others = {
            'gold': 0,
            'soul': 0,
            'skills': [],
            'proficiency': [],
            'inventory': [],
            'equips': []
        }

        self._button_status = pg.rect.Rect(15, 190, 373, 30)


    def _unpack_basic_status(self, index) -> tuple:

        name, ethnicity, class_, level = check_records(FOLDER['save'])[index][:4]

        return name, ethnicity, class_, level


    def _assign_basic_attributes(self):

        list_keys = [key for key in self.attributes]

        list_values = check_records(FOLDER['save'])[self.index]

        status = list_values + self._first_game() if len(list_values[:]) < 5 else list_values

        for index, key in enumerate(list_keys):

            item = int(status[index]) if str(status[index]).isnumeric() else status[index]

            self.attributes[key] = item


    def _assign_gold_soul(self):

        values = check_records(FOLDER['save'])[self.index]

        if len(values) >= 14:

            self.others['gold'], self.others['soul'] = int(values[-3]), int(values[-2])


    def _assign_location(self):

        if len(check_records(FOLDER['save'])[self.index]) >= 14:

            self.location = check_records(FOLDER['save'])[self.index][-1]


    def _assign_others(self):

        name, ethnicity, class_, level = self._unpack_basic_status(self.index)

        self.others['skills'].append(SKILLS[ethnicity[0] + '_' + class_])


    def _first_game(self):

        name, ethnicity, class_, level = self._unpack_basic_status(self.index)

        folder = DARK_ELF if 'dark' in ethnicity else FOREST_ELF if 'forest' in ethnicity else GREY_ELF

        list_with_gold_soul_and_location = [0, 0, 'Sea North']

        if str(level) == '1':

            return folder[class_] + list_with_gold_soul_and_location


    def _show_status(self, pos_mouse):

        if self._button_status.collidepoint(pos_mouse):
            self.show_status_interface = True
            return

        self.show_status_interface = False


    def save(self, location):

        with open(FOLDER['save'] + str(self.attributes['name']).lower(), mode='w+', encoding='utf-8') as file:

            for value in self.attributes.values():

                file.write(str(value).strip() + '\n')

            file.write(str(self.others['gold']) + '\n')
            file.write(str(self.others['soul']) + '\n')
            file.write(str(location).strip() + '\n')

        self.others['skills'].clear()

        self.others['gold'], self.others['soul'] = 0, 0


    def events_character(self, event):

        pos_mouse = pg.mouse.get_pos()

        if event.type == pg.MOUSEBUTTONDOWN:

            self._show_status(pos_mouse)


    def update(self):

        if not self.others['skills']:

            self._assign_basic_attributes()

            self.assign_status_secondary()

            self.assign_current_status()

            self._assign_gold_soul()

            self._assign_location()

            self._assign_others()

        self.check_current_status()

        self._draw_bar_status()
        self._draw_sprites()
        self._draw_info_status()
        self._draw_status()

        self.status_regen()

        self.level_progression(self.level_up())
