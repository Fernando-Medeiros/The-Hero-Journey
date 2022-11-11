import os
import pygame as pg

from datetime import datetime
from time import sleep
from os import listdir, remove


COLORS = {
    'WHITE': (255, 255, 255),
    'BLACK': (0, 0, 0),
    'RED': (176, 31, 31),
    'GREEN': (29, 161, 85),
    'BLUE': (67, 138, 167),
    'YELLOW': (235, 197, 70),
    'BLUE_2': (6, 0, 56),
    'WOOD': (210, 180, 140),
    'PURPLE': (38, 1, 36),
    'ACTIVE': 0
}

class Obj(pg.sprite.Sprite):

    def __init__(self, img, x, y, *groups):

        super().__init__(*groups)

        self.image = pg.image.load(img)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rect.width = self.image.get_width()
        self.rect.height = self.image.get_height()

        
def save_log_and_exit():

    datetime_app = os.environ.get('DATETIME_APP')
    
    now = datetime.today().strftime('%d/%m/%Y %H:%M:%S')

    with open('log', 'a') as register_log:

        register_log.write('{} < // > {} \n'.format(datetime_app, now))
        sleep(1)

    quit()


def check_records(FOLDER_: str) -> list:

    list_records = [save for save in listdir(FOLDER_)]
    records = []

    for save in list_records:
        if not open(FOLDER_ + save, mode='r+', encoding='utf-8').readlines():
            remove(FOLDER_ + save)

        with open(FOLDER_ + save, mode='r+', encoding='utf-8') as file:
            records.append(file.read().strip().split('\n'))

    return records


def draw_texts(
    screen,
    text: str,
    pos_x: int,
    pos_y: int,
    font='arial',
    size=15,
    color=COLORS['WHITE']):

    text_font = pg.font.SysFont(font, size, True)
    text_surface = text_font.render(str(text), True, color)

    screen.blit(text_surface, (pos_x, pos_y))


def draw_status_bar(
    screen,
    height,
    fixed_value,
    max_size,
    color,
    rect,
    current_value,
    color_bg=COLORS['WHITE']):
    
    size_max = max_size
    current_size = fixed_value / size_max

    border = 0, 7, 7, 7, 7

    pg.draw.rect(screen, color, (*rect, current_value / current_size, height), *border)
    pg.draw.rect(screen, color_bg, (*rect, size_max, height), 1, *border)
