import pygame as pg

from app.functiontools import COLORS, draw_status_bar, draw_texts
from paths import FOLDERS


class Views:
    
    def __init__(self, main_screen: pg.Surface):

        self.main_screen = main_screen
        
    def draw_loots(self, args) -> None:
        pos_x, pos_y = 25, 660
        
        for key, value in args.items():
            
            if key in 'xp gold soul':
                draw_texts(
                    screen=self.main_screen,
                    text='{} >>> {}'.format(key.title(), value),
                    pos_x=pos_x, pos_y=pos_y,
                    color=COLORS['GREEN'])

            pos_y += 15


    def draw_battle_info(self, log: list) -> None:

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


    def draw_enemy_sprite(self, enemy: list, index: int) -> None:

        name = enemy[index].entity['attributes']['name'].title()
        sprite_img = enemy[index].entity['attributes']['sprite']
        
        sprite = pg.image.load(FOLDERS['enemies'] + sprite_img)

        draw_texts(
            screen=self.main_screen,
            text=f'{name}',
            pos_x=30,
            pos_y=425,
            size=20
            )
        self.main_screen.blit(sprite, (171, 461))


    def draw_info_status_enemy(self, *args) -> None:

        pos_x, pos_y = 46, 375

        for items in args:

            info = [
                '{:^45_.2f}/{:^45_.2f}'.format(items.entity['current']["hp"], items.entity['secondary']["hp"]),
                '{:^45_.2f}/{:^45_.2f}'.format(items.entity['current']["mp"], items.entity['secondary']["mp"]),
                '{:^45_.2f}/{:^45_.2f}'.format(items.entity['current']["stamina"], items.entity['secondary']["stamina"])
            ]

            for index in range(len(info)):

                draw_texts(
                    screen=self.main_screen,
                    text=info[index],
                    pos_x=pos_x, pos_y=pos_y,
                    size=10)

                pos_y += 13
    

    def draw_bar_status(self, *args) -> None:

        pos_x, pos_y = 46, 375

        colors = [COLORS['RED'], COLORS['BLUE'], COLORS['GREEN']]

        for items in args:

            secondary = [
                items.entity['secondary']['hp'],
                items.entity['secondary']['mp'],
                items.entity['secondary']['stamina']
            ]
            current = [
                items.entity['current']['hp'],
                items.entity['current']['mp'],
                items.entity['current']['stamina']
            ]

            for index in range(len(secondary)):

                draw_status_bar(
                    screen=self.main_screen,
                    height=13,
                    fixed_value=secondary[index],
                    width=310,
                    color=colors[index],
                    rect=(pos_x, pos_y),
                    current_value=current[index],
                    color_bg=COLORS['BLACK'])

                pos_y += 13