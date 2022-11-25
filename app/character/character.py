import os

import pygame as pg

from app.tools import check_records
from paths import FOLDERS

from .base import Entity
from .settings import DARK_ELF, FOREST_ELF, GREY_ELF, SKILLS
from .view import View


class Character(Entity, View):

    def __init__(self, main_screen):
        super().__init__()
        Entity.__init__(self)
        View.__init__(self, main_screen)
        
        self.index = 0
        self.location = 'Sea North'

    def _get_index_from_name(self):
        # LOAD THE CHARACTER NAME INTO THE ENV AND RETURN INDEX TO GET THE DATA LIST.
        for index, item in enumerate(check_records('save/')):
            if os.environ['CHARNAME'] == item[0]:
                self.index = index


    def _unpack_basic_status(self, index) -> tuple:

        name, ethnicity, class_, level = check_records(FOLDERS['save'])[index][:4]

        return name, ethnicity, class_, level


    def _assign_basic_attributes(self):

        list_keys = [key for key in self.attributes]

        list_values = check_records(FOLDERS['save'])[self.index]

        status = list_values + self._first_game() if len(list_values[:]) < 5 else list_values

        for index, key in enumerate(list_keys):

            item = int(status[index]) if str(status[index]).isnumeric() else status[index]

            self.attributes[key] = item


    def _assign_gold_soul(self):

        values = check_records(FOLDERS['save'])[self.index]

        if len(values) >= 14:

            self.others['gold'], self.others['soul'] = int(values[-3]), int(values[-2])


    def _assign_location(self):

        if len(check_records(FOLDERS['save'])[self.index]) >= 14:

            self.location = check_records(FOLDERS['save'])[self.index][-1]


    def _assign_others(self):

        name, ethnicity, class_, level = self._unpack_basic_status(self.index)

        self.others['skills'].append(SKILLS[ethnicity[0] + '_' + class_])


    def _first_game(self):

        name, ethnicity, class_, level = self._unpack_basic_status(self.index)

        folder = DARK_ELF if 'dark' in ethnicity else FOREST_ELF if 'forest' in ethnicity else GREY_ELF

        list_with_gold_soul_and_location = [0, 0, 'Sea North']

        if str(level) == '1':

            return folder[class_] + list_with_gold_soul_and_location


    def save(self):

        path = '{}{}'.format(
            FOLDERS['save'],
            str(self.attributes['name']).lower()
            )

        with open(path, mode='w+', encoding='utf-8') as file:

            for value in self.attributes.values():

                file.write('{}\n'.format(str(value).strip()))

            file.write('{}\n{}\n{}\n'.format(
                str(self.others['gold']),
                str(self.others['soul']),
                str(self.location).strip() 
                ))

        self.others['skills'].clear()

        self.others['gold'], self.others['soul'] = 0, 0


    def events(self, event, pos_mouse):
        if event.type == pg.MOUSEBUTTONDOWN:
            self._show_status(pos_mouse)


    def update(self):
        
        self._get_index_from_name()

        # AFTER LOAD CHARACTER
        if not self.others['skills']:

            self._assign_basic_attributes()
            self.assign_status_secondary()
            self.assign_current_status()
            self._assign_gold_soul()
            self._assign_location()
            self._assign_others()

        self.check_current_status()

        # VIEW
        self._draw_bar_status(self.current_status, self.status_secondary, self.attributes)
        self._draw_sprites(self.attributes)
        self._draw_info_status(self.current_status, self.status_secondary, self.attributes, self.others)
        self._draw_status(self.attributes, self.status)

        self.regenerate_status()
        self.level_progression()
