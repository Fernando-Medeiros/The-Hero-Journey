from paths import FOLDERS

from ..tools import COLORS, Obj, draw_rect, draw_texts


class Views(Obj):
    show_status = False

    def __init__(self, main_screen, pos_x, pos_y, *groups):

        img = "./{}{}".format(FOLDERS["enemies"], self.sprite)

        Obj.__init__(self, img, pos_x, pos_y, *groups)

        self.main_screen = main_screen

    def _draw_status(self, pos_mouse) -> None:
        if self.rect.collidepoint(pos_mouse):
            self.show_status = True
        else:
            self.show_status = False

    def _draw_name_and_level(self) -> None:

        if not self.show_status:
            draw_texts(
                screen=self.main_screen,
                text="{}".format(getattr(self, "name")),
                pos_x=self.rect.x + 120,
                pos_y=self.rect.y,
            )
            draw_texts(
                screen=self.main_screen,
                text="Lvl - {}".format(getattr(self, "level")),
                pos_x=self.rect.x + 120,
                pos_y=self.rect.y + 17,
            )

    def _draw_status_on_hover(self) -> None:

        include_attr = ["force", "agility", "vitality", "intelligence", "resistance"]
        include_status = ["attack", "defense", "dodge", "block", "critical"]

        def __draw_attr_column():
            pos_y_attr = self.rect.y - 5

            for attr in include_attr:
                draw_texts(
                    screen=self.main_screen,
                    text="{:<} - {:>}".format(attr.title(), getattr(self, attr)),
                    pos_x=self.rect.x + 5,
                    pos_y=pos_y_attr,
                    size=13,
                )
                pos_y_attr += 20

        def __draw_status_column():
            pos_y_status = self.rect.y - 5

            for attr in include_status:
                draw_texts(
                    screen=self.main_screen,
                    text="{:<} - {:>.1f}".format(attr.title(), getattr(self, attr)),
                    pos_x=self.rect.x + 125,
                    pos_y=pos_y_status,
                    size=13,
                )
                pos_y_status += 20

        if self.show_status:
            draw_rect(
                self.main_screen,
                COLORS["BLACK"],
                [self.rect.x - 2, self.rect.y - 7, 240, 100],
                50,
            )
            draw_rect(
                self.main_screen, rect=[self.rect.x - 2, self.rect.y - 7, 240, 100]
            )
            __draw_attr_column()
            __draw_status_column()

    def events(self, pos_mouse):
        self._draw_status(pos_mouse)

    def update(self, *args, **kwargs):
        super().update(*args, **kwargs)
        self._draw_name_and_level()
        self._draw_status_on_hover()
