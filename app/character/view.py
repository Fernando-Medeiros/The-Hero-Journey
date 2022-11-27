import pygame as pg

from app.tools import COLORS, Obj, draw_rect, draw_status_bar, draw_texts
from paths import FOLDERS


class Views(Obj):
       
    def __init__(self, main_screen, *groups):

        self.show_status = False    
        
        img = './{}{}'.format(FOLDERS['classes'], 'dark-elf-assassin.png')
        pos_x: int = 20
        pos_y: int = 18
        
        Obj.__init__(self, img, pos_x, pos_y, *groups)

        self.main_screen = main_screen

        self.button_status = pg.rect.Rect(15, 190, 373, 30)
    
    
    def _show_status(self, pos_mouse) -> None:
        if self.button_status.collidepoint(pos_mouse):
            self.show_status = True
        else:
            self.show_status = False

    def _draw_bar_status(self) -> None:
        status = [
            [self.health, self.c_health, COLORS['RED'], [173, 36], 222],
            [self.energy, self.c_energy, COLORS['BLUE'], [180, 54], 215],
            [self.stamina, self.c_stamina, COLORS['GREEN'], [183, 72], 212],
            [self.level * 15, self.xp, COLORS['YELLOW'],  [185, 90], 210]
            ]
        for bar in status:
            draw_status_bar(
                screen=self.main_screen,
                height=15,
                fixed_value=bar[0],
                width=bar[4],
                color=bar[2],
                rect=bar[3],
                current_value=bar[1])

    def _draw_info_status(self) -> None:

        draw_texts(self.main_screen, f'Lvl - {self.level}', 189, 110)
        draw_texts(self.main_screen, str(self.name).title(), 189, 8, size=20)
        draw_texts(self.main_screen, str(self.gold), 477, 28, size=25)
        draw_texts(self.main_screen, str(self.soul), 610, 28, size=25)

        texts = [
            '{:^21.1f}/{:^21.1f}'.format(self.c_health, self.health),
            '{:^21.1f}/{:^21.1f}'.format(self.c_energy, self.energy),
            '{:^21.1f}/{:^21.1f}'.format(self.c_stamina, self.stamina),
            '{:^21.1f}/{:^21.1f}'.format(self.xp, self.level * 15)
        ]

        x, y = 185, 36
        for text in texts:
            draw_texts(
                screen=self.main_screen,
                text=text,
                pos_x=x,
                pos_y=y,
                size=13)
            y += 18

    def _draw_status(self) -> None:
        
        draw_rect(screen=self.main_screen, rect=self.button_status[::])

        draw_texts(
            screen=self.main_screen,
            text="Status",
            pos_x=170,
            pos_y=190,
            size=25)
        
        include_attr = ['ethnicity', 'classe', 'force', 'agility', 'vitality', 'intelligence', 'resistance']
        include_status = ['attack', 'defense', 'dodge', 'block', 'critical', 'luck']    

        def draw_attr_column():
            pos_y = 230
            for attr in include_attr:              
                draw_texts(
                    screen=self.main_screen,
                    text='{:<} - {:>}'.format(attr.title(), getattr(self, attr)),
                    pos_x=20, pos_y=pos_y)
                
                pos_y += 20

        def draw_status_column():
            pos_y = 230
            for attr in include_status:
                draw_texts(
                    screen=self.main_screen,
                    text='{:<} - {:>.1f}'.format(attr.title(), getattr(self, attr)),
                    pos_x=206, pos_y=pos_y)
                
                pos_y += 20
        
        if self.show_status:
            draw_rect(screen=self.main_screen, rect=[15, 220, 373, 150])
            draw_attr_column()
            draw_status_column()