from settings import *


def _help_check_pos_del(icon_del, box_sprite, icon_load, pos_mouse, file):
    """
    AUXILIARY FUNCTION TO DELETE SPECIFIC RECORD
    :param icon_del: BUTTON TO DELETE RECORD
    :param box_sprite: TEMPLATE BOX THAT RECEIVES THE CLASS SPRITE
    :param icon_load: BUTTON TO LOAD THE ITEM
    :param pos_mouse: MOUSE POSITION
    :param file: LIST CONTAINING REGISTRATION NAME
    :return: ''
    """

    if icon_del.rect.collidepoint(pos_mouse):
        icon_load.rect.y = LIMBO
        icon_del.rect.y = LIMBO
        box_sprite.image = pg.image.load(IMG_LOAD['box'])
        remove(FOLDER['save'] + file)
        click_sound.play()


class Load:
    class_load = True

    def __init__(self, *groups):
        pos_x_y = [
            (29, 84), (305, 84), (581, 84),
            (29, 409), (305, 409), (581, 409),
            (29, 733), (305, 733), (581, 733)
        ]

        self.bg = Obj(IMG_LOAD['bg'], 0, 0, *groups)

        self._box = []
        self._icon_del = []
        self._icon_add = []

        for records in range(MAX_RECORDS):
            self._box.append(Obj(IMG_LOAD['box'], pos_x_y[records][0], pos_x_y[records][1], *groups))
            self._icon_del.append(Obj(IMG_LOAD['del'], LIMBO, LIMBO, *groups))
            self._icon_add.append(Obj(IMG_NEW_GAME['add'], LIMBO, LIMBO, *groups))

        self._return_icon = Obj(IMG_MENU['return'], 100, 1000, *groups)

    def draw_records(self):
        """
        USES TWO AUXILIARY FUNCTIONS
        FOR EACH RECORD, DRAW CLASS IMAGE, STATUS AND ICON.
        CHECK ETHNICITY TO ASSIGN IMAGE, AND USE RECT TO SET POSITION
        """

        number_of_records = check_records(FOLDER['save'])

        for index in range(len(number_of_records)):
            name, ethnicity, class_, level = number_of_records[index]
            idd = 'ed_' if 'dark' in ethnicity.lower() else 'ef_' if 'forest' in ethnicity.lower() else 'eg_'

            self._box[index].image = pg.image.load(IMG_CLASSES[idd + class_.lower()])

            pos_x, pos_y = self._box[index].rect.bottomleft

            self._icon_del[index].rect.topleft = (pos_x, pos_y + 90)
            self._icon_add[index].rect.topleft = (pos_x + 85, pos_y + 90)

            draw_texts(MAIN_SCREEN, f'> {name}', pos_x, pos_y + 10, color=COLORS['BLACK'])
            draw_texts(MAIN_SCREEN, f'> {ethnicity}', pos_x, pos_y + 30, color=COLORS['BLACK'])
            draw_texts(MAIN_SCREEN, f'> {class_}', pos_x, pos_y + 50, color=COLORS['BLACK'])
            draw_texts(MAIN_SCREEN, f'> lvl {level}', pos_x, pos_y + 70, color=COLORS['BLACK'])

    def erase_record(self, pos_mouse):
        """
        USE AUXILIARY FUNCTION TO CHECK THE OBJECT POSITION AND DELETE THE FILE
        """
        file = [x for x in listdir(FOLDER['save'])]

        for item in range(len(file)):
            _help_check_pos_del(self._icon_del[item], self._box[item], self._icon_add[item], pos_mouse, file[item])

    def return_menu(self, pos_mouse):
        if self._return_icon.rect.collidepoint(pos_mouse):
            self.class_load = False
            click_sound.play()

    def interactive(self, pos_mouse):
        """
        RETURNS IMAGE SWITCH ON MOUSE COLLIDE
        """
        mouse_collision(True, self._icon_del, pos_mouse, IMG_LOAD['select_del'], IMG_LOAD['del'])
        mouse_collision(True, self._icon_add, pos_mouse, IMG_LOAD['select_add'], IMG_NEW_GAME['add'])
        mouse_collision(False, self._return_icon, pos_mouse, IMG_MENU['select_return'], IMG_MENU['return'])

    def events_load(self, evento):
        pos_mouse = pg.mouse.get_pos()

        if evento.type == pg.MOUSEBUTTONDOWN:
            self.erase_record(pos_mouse)
            self.return_menu(pos_mouse)

        if evento.type == pg.MOUSEMOTION:
            self.interactive(pos_mouse)

    def update(self, *args, **kwargs):
        self.draw_records()
