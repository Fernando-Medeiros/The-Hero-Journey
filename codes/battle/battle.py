from settings import *


class Battle:

    @staticmethod
    def data_character(char):
        char_attribute = char.attributes
        char_status = char.status
        char_current = char.current_status
        char_others = char.others

        return char_attribute, char_status, char_current, char_others

    @staticmethod
    def data_enemy(enemy):
        enemy_attribute = enemy.attributes
        enemy_status = enemy.status
        enemy_current = enemy.current_status
        enemy_loots = enemy.loots

        return enemy_attribute, enemy_status, enemy_current, enemy_loots

    @staticmethod
    def damage(hit, defense, block, dodge, critical):

        dano = hit - defense

        dano = 0 if dano <= 0 else dano

        if block:
            return [0, 'block']
        if dodge:
            return [0, 'dodge']
        if critical:
            return [dano * 2, 'critical']
        if dano == 0:
            return [dano, 'miss']
        else:
            return [dano, '']

    @staticmethod
    def defense():

        chance = 20

        return True if randint(0, 100) <= chance else False

    @staticmethod
    def flee():

        return choice([True, False])

    @staticmethod
    def block(block):

        return True if randint(0, 100) <= block else False

    @staticmethod
    def parry(dodge):

        return True if randint(0, 100) <= dodge else False

    @staticmethod
    def critical(critical):

        return True if randint(0, 100) <= critical else False

    @staticmethod
    def energy_used_in_battle(stamina):

        stamina['stamina'] -= 0.3

    @staticmethod
    def kill_sprite_enemy(enemy, index):

        enemy[index].kill()
        enemy.pop(index)

    @staticmethod
    def log_attack(char_name, enemy_name, damage):

        char__name = char_name['name'].replace('_', ' ').title()
        enemy__name = enemy_name['name'].replace('_', ' ').title()

        match damage[1]:

            case 'block':
                return f'{enemy__name} BLOCKED the damage!'
            case 'dodge':
                return f'{enemy__name} DODGED the damage!'
            case 'critical':
                return f'{char__name} inflicted {damage[0]:.1f} CRITICAL damage!!!'
            case 'miss':
                return f'{char__name} missed attack!'
            case '':
                return f'{char__name} inflicts {damage[0]:.1f} damage!'

    @staticmethod
    def log_defense(name, defense):

        name_ = name['name'].replace('_', ' ').title()

        if defense:
            return f'{name_} activate defense mode.'
        else:
            return f"{name_} couldn't defend itself"

    @staticmethod
    def log_flee(name, flee):

        name = name['name'].replace('_', ' ').title()

        if not flee:
            return f'{name} fled the battle.'
        else:
            return f'{name} failed to flee from battle '

    @staticmethod
    def erase_log(*args):

        [item.clear() for item in args]

    @staticmethod
    def take_damage(hp, damage, log):

        log = [''] if len(log) == 0 else log

        if not 'defense' in log[-1]:

            hp['hp'] -= damage[0]

    @staticmethod
    def take_loots(gold_soul, xp, enemy_loot):

        gold_soul['gold'] += enemy_loot['gold']
        gold_soul['soul'] += enemy_loot['soul']
        xp['xp'] += enemy_loot['xp']

    def draw_loots(self, args):

        pos_x, pos_y = 25, 820

        for __item__ in args.items():
            __key__, __value__ = __item__

            self.draw_render_status(f'{__key__.title()} >>> {__value__:_}', pos_x, pos_y, color=COLORS['GREEN'])

            pos_y += 20

    def draw_battle_info(self, log):

        pos_x, pos_y = 25, 540

        white, wood = COLORS['WHITE'], COLORS['WOOD']

        if len(log) >= 13:
            del log[:12]

        for __index__, __info__ in enumerate(log):

            _color_ = white if __index__ % 2 == 0 else wood

            self.draw_render_status(f'{__index__} - {__info__}', pos_x, pos_y, color=_color_)

            pos_y += 30

    def draw_enemy_sprite(self, enemy, index):

        name = enemy[index].attributes['name']
        sprite = pg.image.load(FOLDER['enemies'] + name + '.png')

        self.draw_render_status(f'{name}'.title().replace('_', ' '), 30, 425, size=20)

        MAIN_SCREEN.blit(sprite, (171, 461))

    def draw_info_status_enemy(self, *args):

        pos_x, pos_y = 46, 375

        for __items__ in args:

            info = [
                f'{__items__.current_status["hp"]:^45_.2f}/{__items__.status_secondary["hp"]:^45_.2f}',
                f'{__items__.current_status["mp"]:^45_.2f}/{__items__.status_secondary["mp"]:^45_.2f}',
                f'{__items__.current_status["stamina"]:^45_.2f}/{__items__.status_secondary["stamina"]:^45_.2f}'
            ]

            for __index__ in range(len(info)):

                self.draw_render_status(info[__index__], pos_x, pos_y, size=10)

                pos_y += 13

    def ATTACK(self, status_att, status_def):

        hit = status_att['attack']
        critical = self.critical(status_att['critical'])

        defense = status_def['defense']
        block = self.block(status_def['block'])
        dodge = self.parry(status_def['dodge'])

        return self.damage(hit, defense, block, dodge, critical)

    def draw_bar_status(self, *args):

        pos_x, pos_y = 46, 375

        colors = [COLORS['RED'], COLORS['BLUE'], COLORS['GREEN']]

        for __items__ in args:

            secondary = [
                __items__.status_secondary['hp'],
                __items__.status_secondary['mp'],
                __items__.status_secondary['stamina']
            ]
            current = [
                __items__.current_status['hp'],
                __items__.current_status['mp'],
                __items__.current_status['stamina']
            ]

            for __index__ in range(len(secondary)):

                self.draw_status_bar(13, secondary[__index__], 310, colors[__index__], (pos_x, pos_y), current[__index__])

                pos_y += 13

    @staticmethod
    def draw_render_status(TXT: str, X, Y, size=15, color=(255, 255, 255)):

        font = pg.font.SysFont('arial', size, True)
        text = font.render(f'{TXT}', True, color)

        MAIN_SCREEN.blit(text, (X, Y))

    @staticmethod
    def draw_status_bar(height, fixed_value, max_size, color, rect: (int, int), current_value):

        __size_max = max_size
        __current_size = fixed_value / __size_max

        border = 0, 7, 7, 7, 7

        pg.draw.rect(MAIN_SCREEN, color, (*rect, current_value / __current_size, height), *border)
        pg.draw.rect(MAIN_SCREEN, COLORS['BLACK'], (*rect, __size_max, height), 1, *border)
