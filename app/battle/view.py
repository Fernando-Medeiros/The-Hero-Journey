import pygame as pg

from app.tools import COLORS, draw_status_bar, draw_texts
from paths import FOLDERS


class DrawLog:
    main_screen = pg.Surface

    def draw_log(self ,log: list) -> None:

        pos_x, pos_y = 25, 540

        white = COLORS['WHITE']
        wood = COLORS['WOOD']

        if len(log) >= 13:
            del log[:12]

        for index, info in enumerate(log):
            color = white if index % 2 == 0 else wood

            draw_texts(
                screen=self.main_screen,
                text='{} - {}'.format(index, info),
                pos_x=pos_x,
                pos_y=pos_y,
                color=color)

            pos_y += 30


class DrawLoots:
    main_screen = pg.Surface
    
    def draw_loots(self, loots: dict) -> None:

        pos_x, pos_y = 25, 800

        for key, value in loots.items():
            draw_texts(
                screen=self.main_screen,
                text='{} -> {}'.format(key.title(), value),
                pos_x=pos_x,
                pos_y=pos_y,
                color=COLORS['GREEN'])

            pos_y += 15


class DrawEnemy:
    main_screen = pg.Surface

    def draw_enemy(self, enemy: object) -> None:

        sprite = pg.image.load(FOLDERS['enemies'] + enemy.sprite)

        draw_texts(
            screen=self.main_screen,
            text='{}'.format(enemy.name.title()),
            pos_x=30,
            pos_y=425,
            size=20)

        self.main_screen.blit(sprite, (171, 461))



class DrawEnemyStatus:
    main_screen = pg.Surface

    def draw_enemy_info_status(self, enemy: object) -> None:

        pos_x, pos_y = 46, 375

        info = [
            '{:^45_.2f}/{:^45_.2f}'.format(enemy.c_health, enemy.health),
            '{:^45_.2f}/{:^45_.2f}'.format(enemy.c_energy, enemy.energy),
            '{:^45_.2f}/{:^45_.2f}'.format(enemy.c_stamina, enemy.stamina)
        ]
        for text in info:
            draw_texts(
                screen=self.main_screen,
                text=text,
                pos_x=pos_x,
                pos_y=pos_y,
                size=10)

            pos_y += 13
            

class DrawEnemyBarStatus:
    main_screen = pg.Surface

    def draw_enemy_bar_status(self, enemy: object) -> None:
        status = [
            [enemy.health, enemy.c_health, COLORS['RED']],
            [enemy.energy, enemy.c_energy, COLORS['BLUE']],
            [enemy.stamina, enemy.c_stamina, COLORS['GREEN']],
        ]
        pos_x, pos_y = 46, 375

        for bar in status:
            draw_status_bar(
                screen=self.main_screen,
                height=13,
                fixed_value=bar[0],
                width=310,
                color=bar[2],
                rect=(pos_x, pos_y),
                current_value=bar[1],
                color_bg=COLORS['BLACK']
                )
            pos_y += 13


class Views(DrawLog, DrawLoots, DrawEnemy, DrawEnemyStatus, DrawEnemyBarStatus):

    def __init__(self, main_screen: pg.Surface):
        self.main_screen = main_screen
