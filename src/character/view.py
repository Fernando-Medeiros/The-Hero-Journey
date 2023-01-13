import pygame as pg

from paths import FOLDERS
from src.tools import COLORS, Obj, draw_rect, draw_status_bar, draw_texts


class DrawBarStatus:
    def _draw_bar_status(self) -> None:
        status = [
            [self.health, self.c_health, COLORS["RED"], [173, 36], 222],
            [self.energy, self.c_energy, COLORS["BLUE"], [180, 54], 215],
            [self.stamina, self.c_stamina, COLORS["GREEN"], [183, 72], 212],
            [self.level * 15, self.xp, COLORS["YELLOW"], [185, 90], 210],
        ]
        for bar in status:
            fixed, current, color, rect, width = bar
            draw_status_bar(
                screen=pg.display.get_surface(),
                height=15,
                fixed_value=fixed,
                width=width,
                color=color,
                rect=rect,
                current_value=current,
            )


class DrawStatus:
    def _draw_gold_and_soul(self) -> None:
        draw_texts(pg.display.get_surface(), str(self.gold), 477, 28, size=25)
        draw_texts(pg.display.get_surface(), str(self.soul), 610, 28, size=25)

    def _draw_name_and_level(self) -> None:
        draw_texts(pg.display.get_surface(), f"Lvl - {self.level}", 189, 110)
        draw_texts(pg.display.get_surface(), str(self.name).title(), 189, 8, size=20)

    def _draw_status_secondary(self) -> None:
        texts = [
            "{:^21.1f}/{:^21.1f}".format(self.c_health, self.health),
            "{:^21.1f}/{:^21.1f}".format(self.c_energy, self.energy),
            "{:^21.1f}/{:^21.1f}".format(self.c_stamina, self.stamina),
            "{:^21.1f}/{:^21.1f}".format(self.xp, self.level * 15),
        ]
        x, y = 185, 36
        for text in texts:
            draw_texts(
                screen=pg.display.get_surface(), text=text, pos_x=x, pos_y=y, size=13
            )
            y += 18


class DrawButton:
    def _draw_button_status(self) -> None:

        draw_rect(screen=pg.display.get_surface(), rect=self.button_status[::])

        draw_texts(
            screen=pg.display.get_surface(),
            text="Status",
            pos_x=170,
            pos_y=190,
            size=25,
        )

        if self.show_status:
            draw_rect(screen=pg.display.get_surface(), rect=[15, 220, 373, 150])
            self.draw_attr_column()
            self.draw_status_column()

    def draw_attr_column(self) -> None:
        include_attr = [
            "ethnicity",
            "classe",
            "force",
            "agility",
            "vitality",
            "intelligence",
            "resistance",
        ]
        pos_y = 230
        for attr in include_attr:
            draw_texts(
                screen=pg.display.get_surface(),
                text="{:<} - {:>}".format(attr.title(), getattr(self, attr)),
                pos_x=20,
                pos_y=pos_y,
            )
            pos_y += 20

    def draw_status_column(self) -> None:
        include_status = ["attack", "defense", "dodge", "block", "critical", "luck"]
        pos_y = 230
        for attr in include_status:
            draw_texts(
                screen=pg.display.get_surface(),
                text="{:<} - {:>.1f}".format(attr.title(), getattr(self, attr)),
                pos_x=206,
                pos_y=pos_y,
            )
            pos_y += 20


class Views(Obj, DrawBarStatus, DrawStatus, DrawButton):
    def __init__(self, *groups):

        self.show_status = True

        img = "./{}{}".format(FOLDERS["classes"], "dark-elf-assassin.png")
        pos_x: int = 20
        pos_y: int = 18

        Obj.__init__(self, img, pos_x, pos_y, *groups)

        self.button_status = pg.rect.Rect(15, 190, 373, 30)

    def _show_status(self, pos_mouse) -> None:
        if self.button_status.collidepoint(pos_mouse):
            self.show_status = True if not self.show_status else False

    def events(self, event, pos_mouse):
        if event.type == pg.MOUSEBUTTONDOWN:
            self._show_status(pos_mouse)

    def update(self, *args, **kwargs) -> None:
        super().update(*args, **kwargs)
        self._draw_bar_status()
        self._draw_status_secondary()
        self._draw_button_status()
        self._draw_gold_and_soul()
        self._draw_name_and_level()
