from app.functiontools import Obj, draw_rect, draw_texts


class Views(Obj):
    
    show_status = False

    def __init__(self, main_screen, img, pos_x, pos_y, *groups):

        Obj.__init__(self, img, pos_x, pos_y, *groups)
        
        self.main_screen = main_screen


    def _draw_status(self, pos_mouse) -> None:

        if self.rect.collidepoint(pos_mouse):

            self.show_status = True
        else:
            self.show_status = False

    def _draw_name_and_level(self, attr: dict) -> None:
        
        if not self.show_status:
            name = attr['attributes']["name"].title()
            level = attr['attributes']["level"]

            draw_texts(
                screen=self.main_screen,
                text='{}'.format(name),
                pos_x=self.rect.x + 120, 
                pos_y=self.rect.y
                )
            draw_texts(
                screen=self.main_screen,
                text='Lvl - {}'.format(level),
                pos_x=self.rect.x + 120,
                pos_y=self.rect.y + 17
                )


    def _draw_status_on_hover(self, attr: dict) -> None:

        pos_x, pos_y = self.rect.topright
        exclude = 'name, level, rank, class, ethnicity, gold, soul, xp, sprite, luck'
        
        def draw_name_column():  
            pos_y_attr = pos_y - 5
            
            for key, value in attr['attributes'].items():
                if not key in exclude:
                    draw_texts(
                        screen=self.main_screen,
                        text='{:<} - {:>}'.format(key.title(), value),
                        pos_x=pos_x + 5,
                        pos_y=pos_y_attr,
                        size=13)
                    pos_y_attr += 20

        def draw_status_column():
            pos_y_status = pos_y - 5

            for key, value in attr['status'].items():
                if not key in exclude:
                    draw_texts(
                        screen=self.main_screen,
                        text='{:<} - {:>.1f}'.format(key.title(), value),
                        pos_x=pos_x + 125,
                        pos_y=pos_y_status,
                        size=13)
                        
                    pos_y_status += 20

        if self.show_status:
            draw_rect(self.main_screen, rect=[pos_x - 2, pos_y - 7, 240, 100])
            draw_name_column()
            draw_status_column()