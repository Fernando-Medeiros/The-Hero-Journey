from datetime import datetime
from os import getenv
from time import sleep

import pygame as pg

COLORS = {
    "WHITE": (255, 255, 255),
    "BLACK": (0, 0, 0),
    "RED": (176, 31, 31),
    "GREEN": (29, 161, 85),
    "BLUE": (67, 138, 167),
    "YELLOW": (235, 197, 70),
    "BLUE_2": (6, 0, 56),
    "WOOD": (210, 180, 140),
    "PURPLE": (38, 1, 36),
    "ACTIVE": 0,
}


class Obj(pg.sprite.Sprite):
    def __init__(self, img, pos_x, pos_y, *groups, **kwargs):
        super().__init__(*groups)

        self.image = pg.image.load(img)
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y
        self.rect.width = self.image.get_width()
        self.rect.height = self.image.get_height()


def save_log_and_exit():
    datetime_app = getenv("DATETIME_APP")

    now = datetime.today().strftime("%d/%m/%Y %H:%M:%S")

    with open("docs/log.txt", "a") as register_log:
        register_log.write("{} < // > {} \n".format(datetime_app, now))
        sleep(1)
    quit()


def draw_texts(
    screen: pg.surface.Surface,
    text: str,
    pos_x: int,
    pos_y: int,
    font: str = "arial",
    size: int = 15,
    color=COLORS["WHITE"],
) -> None:
    txt_font = pg.font.SysFont(font, size, True)
    txt_surface = txt_font.render(str(text), True, color)

    screen.blit(txt_surface, (pos_x, pos_y))


def draw_status_bar(
    screen: pg.surface.Surface,
    height: int,
    fixed_value: float,
    width: int,
    color: tuple[int, int, int],
    rect: tuple[int, int],
    current_value: int,
    color_bg=COLORS["WHITE"],
    border: tuple = (0, 7, 7, 7, 7),
) -> None:
    # BORDER: rounded -> radius, T-left, T-right, B-left, B-right

    fixed_width = width
    current_size = fixed_value / fixed_width

    pg.draw.rect(
        screen, color, (*rect, round(current_value / current_size), height), 0, *border
    )

    pg.draw.rect(screen, color_bg, (*rect, fixed_width, height), 1, *border)


def draw_rect(
    screen: pg.surface.Surface,
    color: tuple[int, int, int] = COLORS["WHITE"],
    rect: list | tuple | pg.Rect = (0, 0, 0, 0),
    width: int = 1,
    border: tuple = (0, 7, 7, 7, 7),
) -> None:

    pg.draw.rect(screen, color, rect, width, *border)
