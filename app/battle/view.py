from settings import COLORS, FOLDER, MAIN_SCREEN, pg


class DrawViews:

    def draw_loots(self, args):

        pos_x, pos_y = 25, 820

        for item in args.items():
            key, value = item

            self.draw_render_status(
                TXT='{} >>> {:_}'.format(key.title(), value),
                X=pos_x, Y=pos_y,
                color=COLORS['GREEN'])

            pos_y += 20


    def draw_battle_info(self, log):

        pos_x, pos_y = 25, 540

        white, wood = COLORS['WHITE'], COLORS['WOOD']

        if len(log) >= 13:
            del log[:12]

        for index, info in enumerate(log):

            color = white if index % 2 == 0 else wood

            self.draw_render_status(
                TXT='{} - {}'.format(index, info),
                X=pos_x, Y=pos_y,
                color=color)

            pos_y += 30


    def draw_enemy_sprite(self, enemy, index):

        name = enemy[index].attributes['name']
        sprite = pg.image.load(FOLDER['enemies'] + name + '.png')

        self.draw_render_status(
            TXT='{}'.format(name).title().replace('_', ' '),
            X=30, Y=425,
            size=20)

        MAIN_SCREEN.blit(sprite, (171, 461))


    def draw_info_status_enemy(self, *args):

        pos_x, pos_y = 46, 375

        for items in args:

            info = [
                '{:^45_.2f}/{:^45_.2f}'.format(items.current_status["hp"], items.status_secondary["hp"]),
                '{:^45_.2f}/{:^45_.2f}'.format(items.current_status["mp"], items.status_secondary["mp"]),
                '{:^45_.2f}/{:^45_.2f}'.format(items.current_status["stamina"], items.status_secondary["stamina"])
            ]

            for index in range(len(info)):

                self.draw_render_status(
                    TXT=info[index],
                    X=pos_x, Y=pos_y,
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

                self.draw_status_bar(13, secondary[index], 310, colors[index], (pos_x, pos_y), current[index])

                pos_y += 13


    def draw_render_status(self, TXT: str, X, Y, size=15, color=(255, 255, 255)):

        font = pg.font.SysFont('arial', size, True)
        text = font.render(f'{TXT}', True, color)

        MAIN_SCREEN.blit(text, (X, Y))


    def draw_status_bar(self, height, fixed_value, max_size, color, rect, current_value):

        size_max = max_size
        current_size = fixed_value / size_max

        border = 0, 7, 7, 7, 7

        pg.draw.rect(MAIN_SCREEN, color, (*rect, current_value / current_size, height), *border)
        pg.draw.rect(MAIN_SCREEN, COLORS['BLACK'], (*rect, size_max, height), 1, *border)
