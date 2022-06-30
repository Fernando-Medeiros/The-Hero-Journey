from time import sleep
from os import listdir, remove
from datetime import datetime
from random import choice
from paths import *


# ################################################################
pg.display.set_caption(NAME_OF_THE_GAME)
VERSION = '1.2'
LOG = datetime.today().strftime('%d/%m/%Y %H:%M:%S')
FRAMES = pg.time.Clock()
MAX_FRAMES = 30
DISPLAY_DEFAULT = 747

MAIN_SCREEN = pg.display.set_mode((DISPLAY_DEFAULT, 1050), pg.SCALED | pg.RESIZABLE)

FONT_SETTINGS = pg.font.SysFont('arial', 25, True)
LIMBO = -1080
MAX_RECORDS = 9
MIN_CHARACTERS_NAME, MAX_CHARACTERS_NAME = 3, 20
# ################################################################

soundtrack = [SONGS['orpheus']]
click_sound = SOUNDS['click']


class Obj(pg.sprite.Sprite):
    """
    Primary class to add any object

    image = (str) -- folder/imagename/type(.png or .jpg)
    rect_x = (int) -- horizontal position
    rect_y = (int) -- vertical position
    width and height -- get the width and height of the current image

    This class has methods inherited from pygame's Sprite class.
    So any object must be assigned to a group of "pygame.sprite.Group()"
    example:

    #################################################################################
    screen = pygame.display.set_mode((500, 500), pygame.SCALED | pygame.FULLSCREEN)
    group_1 = pygame.sprite.Group()

    x = Obj(img='folder/imagename.png', x=0, y=100, group_1)

    Method to design group sprites:
    
    group_1.draw(screen)
    """

    def __init__(self, img, x, y, *groups):
        super().__init__(*groups)
        self.image = pg.image.load(img)
        self.rect = self.image.get_rect()
        self.rect[0] = x
        self.rect[1] = y
        self.rect.width = self.image.get_width()
        self.rect.height = self.image.get_height()


class DrawStatusBar:
    """
    Helper function to draw rectangle with health bar, mana and stamina.
    surface = (int) -- Creates a surface with width and height.
    rect = (int) -- Assign rectangle to surface.
    size_max (int) -- Pass the fixed value to the boundary of the rectangle.
    current_size = (int) -- The variable that will constantly change value.
    """

    def __init__(self, width, height, fixed_value, max_size, rect=(0, 0)):

        self.surface = pg.surface.Surface((width, height))
        self.rect = self.surface.get_rect(topleft=rect)
        self.size_max = max_size
        self.current_size = fixed_value / self.size_max

    def draw(self, screen, color, x, y, height, current_value, color_bg=COLORS['WHITE']):
        border = 0, 7, 7, 7, 7

        current = pg.draw.rect(screen, color, (x, y, current_value / self.current_size, height), *border)
        front = pg.draw.rect(screen, color_bg, (x, y, self.size_max, height), 1, *border)


def save_log():
    """
    AUXILIARY FUNCTION TO SAVE LOG AND QUIT THE GAME
    """
    with open('log', 'a') as up_log:
        up_log.write(LOG + ' < // > ' + date_time() + '\n'), up_log.close()
    click_sound.play()
    sleep(1), pg.quit(), quit()


def date_time():
    return datetime.today().strftime('%d/%m/%Y %H:%M:%S')


def draw_texts(screen, TXT: str, X: int, Y: int, font='arial', size=15, color=(255, 255, 255)):
    """
    AUXILIARY FUNCTION TO REDUCE CODE LINES / RENDER TEXTS
    """
    txt = pg.font.SysFont(font, size, True)
    t = txt.render(f'{TXT}', True, color)

    screen.blit(t, (X, Y))


def check_records(FOLDER_: str):
    """
    CHECKS AND TREAT THE FILES IN THE SAVED FOLDER
    :type FOLDER_: SAVE FOLDER NAME -> STR
    :return: RETURNS LIST WITH VALID SAVED
    """
    list_records = [x for x in listdir(FOLDER_)]
    records = []

    for save in list_records:

        if not open(FOLDER_ + save, mode='r+', encoding='utf-8').readlines():
            remove(FOLDER_ + save)

        with open(FOLDER_ + save, mode='r+', encoding='utf-8') as file:
            records.append(file.read().strip().split('\n'))

    return records


def mouse_collision_changing_image(list_objects, pos_mouse, select_item: str, item_default: str, check=True):
    """
    AUXILIARY FUNCTION TO DETECT MOUSE COLLISION WHEN PASSING OVER THE SPECIFIED OBJECT
    :param check: CHECK THE RETURN OF THE ORIGINAL IMAGE
    :param list_objects: AN OBJECT OR A LIST
    :param pos_mouse: MOUSE POSITION
    :param select_item: PICTURE WHEN PASSING THE MOUSE
    :param item_default: ORIGINAL IMAGE
    :return: RETURNS IMAGE SWITCH ON MOUSE COLLIDE
    """
    if type(list_objects) is list:
        for item in range(len(list_objects)):
            if list_objects[item].rect.collidepoint(pos_mouse):
                list_objects[item].image = pg.image.load(select_item)
            else:
                list_objects[item].image = pg.image.load(item_default)

    else:
        if list_objects.rect.collidepoint(pos_mouse):
            list_objects.image = pg.image.load(select_item)
        else:
            if check:
                list_objects.image = pg.image.load(item_default)


def mouse_collision_catching_x_y(limbo: int, iterable, object_get_img, pos_mouse):
    topleft = (limbo, limbo)

    if type(iterable) is dict:
        for item in iterable:
            if iterable[item].rect.collidepoint(pos_mouse):
                topleft = iterable[item].rect.topleft

        object_get_img.rect.topleft = topleft

    elif type(iterable) is list:
        for item in range(len(iterable)):
            if iterable[item].rect.collidepoint(pos_mouse):
                topleft = iterable[item].rect.topleft

        object_get_img.rect.topleft = topleft
