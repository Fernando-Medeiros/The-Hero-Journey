import pygame as pg

from paths import FOLDER
from app.functiontools import draw_texts, draw_status_bar, COLORS


class Views:
    
    def __init__(self, main_screen):
        self.main_screen = main_screen
        
    def draw_loots(self, args):

        pos_x, pos_y = 25, 820

        for item in args.items():
            key, value = item

            draw_texts(
                screen=self.main_screen,
                text='{} >>> {:_}'.format(key.title(), value),
                pos_x=pos_x, pos_y=pos_y,
                color=COLORS['GREEN'])

            pos_y += 20


    def draw_battle_info(self, log):

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
                pos_x=pos_x, pos_y=pos_y,
                color=color)

            pos_y += 30


    def draw_enemy_sprite(self, enemy, index):

        name = enemy[index].attributes['name']
        sprite = pg.image.load(FOLDER['enemies'] + name + '.png')

        draw_texts(
            screen=self.main_screen,
            text='{}'.format(name).title().replace('_', ' '),
            pos_x=30, pos_y=425,
            size=20)

        self.main_screen.blit(sprite, (171, 461))


    def draw_info_status_enemy(self, *args):

        pos_x, pos_y = 46, 375

        for items in args:

            info = [
                '{:^45_.2f}/{:^45_.2f}'.format(items.current_status["hp"], items.status_secondary["hp"]),
                '{:^45_.2f}/{:^45_.2f}'.format(items.current_status["mp"], items.status_secondary["mp"]),
                '{:^45_.2f}/{:^45_.2f}'.format(items.current_status["stamina"], items.status_secondary["stamina"])
            ]

            for index in range(len(info)):

                draw_texts(
                    screen=self.main_screen,
                    text=info[index],
                    pos_x=pos_x, pos_y=pos_y,
                    size=10)

                pos_y += 13
    

    def draw_bar_status(self, *args):

        pos_x, pos_y = 46, 375

        colors = [COLORS['RED'], COLORS['BLUE'], COLORS['GREEN']]

        for items in args:

            secondary = [
                items.status_secondary['hp'],
                items.status_secondary['mp'],
                items.status_secondary['stamina']
            ]
            current = [
                items.current_status['hp'],
                items.current_status['mp'],
                items.current_status['stamina']
            ]

            for index in range(len(secondary)):

                draw_status_bar(
                    screen=self.main_screen,
                    height=13,
                    fixed_value=secondary[index],
                    max_size=310,
                    color=colors[index],
                    rect=(pos_x, pos_y),
                    current_value=current[index],
                    color_bg=COLORS['BLACK'])

                pos_y += 13