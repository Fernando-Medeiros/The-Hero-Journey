from settings import *


class Load:

    class_load = True
    check = ''
    name_for_loading = ''

    def __init__(self, *groups):

        pos_x_y = [
            (29, 74), (305, 74), (581, 74),
            (29, 389), (305, 389), (581, 389),
            (29, 703), (305, 703), (581, 703)
        ]

        self.bg = Obj(IMG_LOAD['bg'], 0, 0, *groups)

        self._box = []
        self._icon_del = []
        self._icon_add = []

        for records in range(MAX_RECORDS):

            self._box.append(Obj(IMG_LOAD['box'], pos_x_y[records][0], pos_x_y[records][1], *groups))
            self._icon_del.append(Obj(IMG_LOAD['del'], LIMBO, LIMBO, *groups))
            self._icon_add.append(Obj(IMG_NEW_GAME['add'], LIMBO, LIMBO, *groups))

        self._return_icon = Obj(IMG_MENU['return'], 100, 970, *groups)

    def _draw_records(self):
        """
        USES TWO AUXILIARY FUNCTIONS
        FOR EACH RECORD, DRAW CLASS IMAGE, STATUS AND ICON.
        CHECK ETHNICITY TO ASSIGN IMAGE, AND USE RECT TO SET POSITION
        """
        number_of_records = check_records(FOLDER['save'])

        for index in range(len(number_of_records)):

            name, ethnicity, class_, level = number_of_records[index][:4]
            idd = 'ed_' if 'dark' in ethnicity else 'ef_' if 'forest' in ethnicity else 'eg_'

            self._box[index].image = pg.image.load(IMG_CLASSES[idd + class_])

            pos_x, pos_y = self._box[index].rect.bottomleft

            self._icon_del[index].rect.topleft = (pos_x, pos_y + 90)
            self._icon_add[index].rect.topleft = (pos_x + 85, pos_y + 90)

            draw_texts(MAIN_SCREEN, f'> {name}'.title(), pos_x, pos_y + 10, color=COLORS['BLACK'])
            draw_texts(MAIN_SCREEN, f'> {ethnicity}'.title(), pos_x, pos_y + 30, color=COLORS['BLACK'])
            draw_texts(MAIN_SCREEN, f'> {class_}'.title(), pos_x, pos_y + 50, color=COLORS['BLACK'])
            draw_texts(MAIN_SCREEN, f'> lvl {level}', pos_x, pos_y + 70, color=COLORS['BLACK'])

    def _erase_record(self, pos_mouse):
        """
        FUNCTION TO CHECK THE OBJECT POSITION AND DELETE THE FILE
        """
        file = [x for x in listdir(FOLDER['save'])]

        for item in range(len(file)):

            if self._icon_del[item].rect.collidepoint(pos_mouse):

                self._icon_add[item].rect.y = LIMBO
                self._icon_del[item].rect.y = LIMBO
                self._box[item].image = pg.image.load(IMG_LOAD['box'])
                remove(FOLDER['save'] + file[item])
                click_sound.play()

    def _loading(self, pos_mouse):

        for icon in range(len(self._icon_add)):

            if self._icon_add[icon].rect.collidepoint(pos_mouse):
                self.check = 'loading'
                self.name_for_loading = check_records(FOLDER['save'])[icon][0].strip()

    def _return_menu(self, pos_mouse):

        if self._return_icon.rect.collidepoint(pos_mouse):
            self.class_load = False
            click_sound.play()

    def _interactive(self, pos_mouse):
        """
        RETURNS IMAGE SWITCH ON MOUSE COLLIDE
        """
        mouse_collision_changing_image(self._icon_del, pos_mouse, IMG_LOAD['select_del'], IMG_LOAD['del'])
        mouse_collision_changing_image(self._icon_add, pos_mouse, IMG_LOAD['select_add'], IMG_NEW_GAME['add'])
        mouse_collision_changing_image(self._return_icon, pos_mouse, IMG_MENU['select_return'], IMG_MENU['return'])

    def events_load(self, evento):
        pos_mouse = pg.mouse.get_pos()

        if evento.type == pg.MOUSEBUTTONDOWN:
            self._erase_record(pos_mouse)
            self._return_menu(pos_mouse)
            self._loading(pos_mouse)

        if evento.type == pg.MOUSEMOTION:
            self._interactive(pos_mouse)

    def update(self, *args, **kwargs):

        self._draw_records()
        draw_texts(MAIN_SCREEN, f'{title_load}', 300 + len(title_load), 15, size=27)
