import pygame as pg
from time import sleep
from os import listdir, remove
from datetime import datetime


class Obj(pg.sprite.Sprite):

    def __init__(self, img, x, y, *groups):

        super().__init__(*groups)

        self.image = pg.image.load(img)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.rect.width = self.image.get_width()
        self.rect.height = self.image.get_height()

        
def save_log_and_exit(DATETIME_APP):
    
    now = datetime.today().strftime('%d/%m/%Y %H:%M:%S')

    with open('log', 'a') as register_log:

        register_log.write('{} < // > {} \n'.format(DATETIME_APP, now))
        
        sleep(1)

    quit()


def check_records(FOLDER_: str) -> list:
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


def draw_texts(screen, TXT: str, X: int, Y: int, font='arial', size=15, color=(255, 255, 255)):

    text = pg.font.SysFont(font, size, True)
    text_surface = text.render(f'{TXT}', True, color)

    screen.blit(text_surface, (X, Y))