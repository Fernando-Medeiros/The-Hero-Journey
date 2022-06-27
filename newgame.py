from settings import *


class NewGame:

    ETHNICITY, CLASS_, NAME = '', '', ''
    check, name_for_loading = '', ''

    class_new_game = True
    BLOCK, INBOX = False, False

    def __init__(self, *groups):
        self.pos_y_e, self.pos_y_c = 70, 560

        self.bg = Obj(IMG_NEW_GAME['bg'], 0, 0, *groups)

        self.ethnicity = []
        self.class_ = []

        self.boxes = [
            Obj(IMG_NEW_GAME['HERALDRY_BOX'], 0, 111, *groups),
            Obj(IMG_NEW_GAME['BOX_STATUS'], 8, 632, *groups),
            pg.Rect(183, 942, 376, 35)
        ]

        self.interactive_ = [
            Obj(IMG_NEW_GAME['select'], LIMBO, self.pos_y_e, *groups),
            Obj(IMG_NEW_GAME['select'], LIMBO, self.pos_y_c, *groups),
            Obj(IMG_NEW_GAME['interactive'], LIMBO, LIMBO, *groups),
        ]

        self.max_records = Obj(IMG_NEW_GAME['max_records'], 0, LIMBO, *groups)
        self.add_icon = Obj(IMG_NEW_GAME['add'], 559, 942, *groups)
        self.return_icon = Obj(IMG_MENU['return'], 100, 942, *groups)

    def _select_guides(self, pos_mouse):
        """
        RETURNS ETHNICITY AND CLASS SELECTION AND ADD NEW REGISTRATION
        """
        self._add_information_ethnicity_class(
            'dark-elf', self.ethnicity[0], 'info_dark', ['info_ed_duelist', 'info_ed_mage', 'info_ed_assassin'], pos_mouse)

        self._add_information_ethnicity_class(
            'forest-elf', self.ethnicity[1], 'info_forest', ['info_ef_warrior', 'info_ef_mage', 'info_ef_warden'], pos_mouse)

        self._add_information_ethnicity_class(
            'grey-elf', self.ethnicity[2], 'info_grey', ['info_eg_warrior', 'info_eg_mage', 'info_eg_warden'], pos_mouse)

    def _return_menu(self, pos_mouse):

        if self.return_icon.rect.collidepoint(pos_mouse):
            self.class_new_game = False
            self._helper_clear_data()

    def _add_record(self, event, pos_mouse):
        """
        SELECT NAME AND ADD BOX
        RETURN THE REGISTRATION TO ADD NAME AND CLICK ON ICON
        """
        if event.type == pg.MOUSEBUTTONDOWN:
            if self.add_icon.rect.collidepoint(pos_mouse) and (len(self.NAME) >= MIN_CHARACTERS_NAME):

                features = self.NAME.strip().title() + '\n' + self.ETHNICITY + '\n' + self.CLASS_ + '\n' + '1'

                with open(FOLDER['save'] + self.NAME.casefold(), 'w') as new_record:
                    new_record.write(features)
                click_sound.play()

                sleep(1)

                self.check = 'loading'
                self.name_for_loading = self.NAME.strip().casefold()

    def _active_input_box(self, event, pos_mouse):

        if event.type == pg.MOUSEBUTTONDOWN:

            if self.boxes[2].collidepoint(pos_mouse):
                self.INBOX = True, click_sound.play()
            else:
                self.INBOX = False

            COLORS['ACTIVE'] = COLORS['WHITE'] if self.INBOX else COLORS['BLACK']

    def _receives_character_name(self, event):
        """
        NAME RECEIVES THE PRESSED CHARACTERS, REMOVED FROM THE KEY/EVENT.UNICODE
        PREVENTS TEXT FROM BEING GREATER THAN MAX_C CHARACTERS
        """
        if event.type == pg.KEYDOWN and self.INBOX:

            if len(self.ETHNICITY) > 2 < len(self.CLASS_):
                if event.key == pg.KSCAN_UNKNOWN:
                    self.NAME = ''
                if event.key == pg.K_BACKSPACE:
                    self.NAME = self.NAME[:-1]
                else:
                    self.NAME += str(event.unicode).replace('\r', '').replace('\t', '')

        self.NAME = self.NAME[:-1] if len(self.NAME) >= MAX_CHARACTERS_NAME else self.NAME

    def _interactive(self, pos_mouse):
        """
        RETURNS IMAGE SWITCH ON MOUSE COLLIDE
        """
        mouse_collision_catching_x_y(
            LIMBO, self.ethnicity + self.class_, self.interactive_[2], pos_mouse)

        mouse_collision_changing_image(
            self.return_icon, pos_mouse, IMG_MENU['select_return'], IMG_MENU['return'])

        mouse_collision_changing_image(
            self.add_icon, pos_mouse, IMG_LOAD['select_add'], IMG_NEW_GAME['add'], check=False)

    def _draw_box(self):
        """
        BOX DRAWING TO ADD NAME
        DRAW THE TEXT, BOX -> INSIDE THE SCREEN_MAIN
        """
        if self.INBOX and len(self.NAME) >= MIN_CHARACTERS_NAME:
            self.add_icon.image = pg.image.load(IMG_LOAD['select_add'])
        else:
            self.add_icon.image = pg.image.load(IMG_NEW_GAME['add'])

        # DRAW USER TEXT INPUT
        draw_texts(
            MAIN_SCREEN, self.NAME.title(), X=self.boxes[2].x + 5, Y=self.boxes[2].y + 5, size=25,
            color=COLORS['BLACK'])

        # DRAW THE BOX FOR TEXT INPUT
        pg.draw.rect(MAIN_SCREEN, COLORS['ACTIVE'], self.boxes[2], 2)

    def _check_max_records(self):
        """
        CHECK LIMIT OF RECORDS AND RETURN LOCK FOLLOWED BY INSTRUCTIONS
        """
        if self.class_new_game and len([x for x in listdir(FOLDER['save'])]) >= MAX_RECORDS:
            self.BLOCK = True
            self.max_records.rect.y = 0

        else:
            self.BLOCK = False
            self.max_records.rect.y = LIMBO

    def _draw_titles(self):

        draw_texts(MAIN_SCREEN, f'{title_new_game[0]}', 300 + len(title_new_game[0]), 15, size=27)
        draw_texts(MAIN_SCREEN, f'{title_new_game[1]}', 300 + len(title_new_game[1]), 510, size=27)

    def _draw_subtitles(self):

        pos_x_txt = [75, 324, 573]
        pos_x_rect = [0, 249, 498]
        pos_y_etn, pos_y_clas = 70, 560

        for item in range(3):

            draw_texts(
                MAIN_SCREEN, f'{list_ethnicities[item]}'.title(), pos_x_txt[item], pos_y_etn + 10, size=20)

            self.ethnicity.append(DrawStatusBar(249, 41, 0, 249, rect=(pos_x_rect[item], pos_y_etn)))

        for item in range(3):

            draw_texts(
                MAIN_SCREEN, f'{list_class[0][item]}'.title(), pos_x_txt[item] + 20, pos_y_clas + 10, size=20)

            self.class_.append(DrawStatusBar(249, 41, 0, 249, rect=(pos_x_rect[item], pos_y_clas)))

    def events_new_game(self, event):

        pos_mouse = pg.mouse.get_pos()

        if event.type == pg.MOUSEBUTTONDOWN:
            self._return_menu(pos_mouse)
            self._select_guides(pos_mouse)

        if event.type == pg.MOUSEMOTION:
            self._interactive(pos_mouse)

        if not self.BLOCK:
            self._add_record(event, pos_mouse)
            self._receives_character_name(event)
            self._active_input_box(event, pos_mouse)

    def update(self, *args, **kwargs):

        self._check_max_records()
        self._draw_box()
        self._draw_titles()
        self._draw_subtitles()

    #######

    def _add_information_ethnicity_class(self, ethnicity_name, object_ethnicity, heraldry,
                                         info_status: list[str, str, str], pos_mouse):
        """
        USES TWO AUXILIARY FUNCTIONS:
        1 - CLEAR DATA WHENEVER YOU CLICK ON THE ETHNICITY BUTTON
        2 - HELP ADD AND POSITION CLASS INFORMATION
        FUNCTION TO RETURN ETHNICITY AND CLASS CHOICE SYSTEM
        :param ethnicity_name: STR
        :param object_ethnicity: OBJECT TO BE PRESSED: VAR
        :param heraldry: HERALDRY IMAGE (STR)
        :param info_status: STR LIST WITH 3 NAMES, CLASS: [1, 2, 3]
        :param pos_mouse: MOUSE POSITION IN EVENTS (tuple)
        :return: RETURNS CHOSEN ETHNICITY AND CLASS.
        """

        # BY CLICKING ON THE ETHNICITY TAB
        classes = list_class[0] if 'dark' in ethnicity_name else list_class[1]

        if object_ethnicity.rect.collidepoint(pos_mouse):
            self._helper_clear_data(heraldry, object_ethnicity.rect.x)

            for index, item in enumerate(classes):
                self.class_[index].image = pg.image.load(IMG_NEW_GAME[item])

        if self.interactive_[0].rect.x == object_ethnicity.rect.x:

            for item in range(len(classes)):
                self._position_classes(self.class_[item], pos_mouse, info_status[item])

            self.ETHNICITY = ethnicity_name.title()

    def _position_classes(self, object_class, pos_mouse, info_status):
        """
        AUXILIARY FUNCTION
        UPDATE AND POSITION CLASS INFORMATION
        """
        if object_class.rect.collidepoint(pos_mouse):
            self.interactive_[1].rect.x = object_class.rect.x
            self.boxes[1].image = pg.image.load(IMG_NEW_GAME[info_status])
            self.CLASS_ = info_status[8:].title()
            click_sound.play()

    def _helper_clear_data(self, heraldry='HERALDRY_BOX', interactive_ethnicity=LIMBO):
        """
        AUXILIARY FUNCTION TO CLEAR DATA ON RETURN menu;
        OR POSITION HERALDRY AND INTERACTIVE OF ETHNICITY
        """
        self.NAME, self.ETHNICITY, self.CLASS_ = '', '', ''
        self.interactive_[0].rect.x = interactive_ethnicity
        self.interactive_[1].rect.x = LIMBO
        self.boxes[0].image = pg.image.load(IMG_NEW_GAME[heraldry])
        self.boxes[1].image = pg.image.load(IMG_NEW_GAME['BOX_STATUS'])
        click_sound.play()
