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
    def damage(char, enemy, block, dodge, critical):

        dano = char - enemy

        dano = 0 if dano <= 0 else dano

        if block == 'block':
            return 0
        if dodge == 'dodge':
            return 0
        if critical == 'critical':
            return dano * 2

        return dano

    @staticmethod
    def defense():

        chance = 15
        reduces_damage_by_two = 'success' if randint(0, 100) <= chance else 'fail'

        return reduces_damage_by_two

    @staticmethod
    def block(block):

        result = 'block' if randint(0, 100) <= block else 'fail'

        return result

    @staticmethod
    def parry(dodge):

        result = 'dodge' if randint(0, 100) <= dodge else 'fail'

        return result

    @staticmethod
    def critical(critical):

        result = 'critical' if randint(0, 100) <= critical else 'fail'

        return result

    @staticmethod
    def kill_sprite_enemy(enemy, index):

        if enemy[index].current_status['hp'] <= 0:
            enemy[index].kill()
            del enemy[index]

    @staticmethod
    def log_attack(name, damage):

        name = name['name'].replace('_', ' ').title()
        damage = f'{damage:.1f}' if damage > 0 else 'Miss'

        log = f'{name} inflicts {damage} damage!'

        return log

    @staticmethod
    def log_defense(name):

        name = name['name'].replace('_', ' ').title()

        log = f'{name} activate defense mode.'

        return log

    @staticmethod
    def log_flee(name):

        name = name['name'].replace('_', ' ').title()

        log = f'{name} fled the battle.'

        return log

    @staticmethod
    def erase_log(log):

        del log[::]

    @staticmethod
    def erase_loots(loots):

        loots.clear()

    @staticmethod
    def take_damage(obj, damage):

        obj['hp'] -= damage

        return obj

    @staticmethod
    def take_loots(gold_soul, xp, enemy_loot):

        gold_soul['gold'] += enemy_loot['gold']
        gold_soul['soul'] += enemy_loot['soul']
        xp['xp'] += enemy_loot['xp']

    @staticmethod
    def draw_loots(args):

        pos_x, pos_y = 25, 830

        for index, item in enumerate(args.items()):
            key, value = item

            draw_texts(MAIN_SCREEN, f'{key:^10} - {value:^10}', pos_x, pos_y, color=COLORS['GREEN'])

            pos_y += 15

    @staticmethod
    def draw_battle_info(log, pos_x, pos_y):

        yellow, blue = COLORS['YELLOW'], COLORS['BLUE']

        if len(log) >= 12:
            del log[:11]

        for index, info in enumerate(log):

            c_ = yellow if index % 2 == 0 else blue

            draw_texts(MAIN_SCREEN, f'{index} - {info}', pos_x, pos_y, color=c_)

            pos_y += 30

    @staticmethod
    def draw_sprite_enemy(enemy, index):

        name = enemy[index].attributes['name']
        sprite = pg.image.load(FOLDER['enemies'] + name + '.png')

        draw_texts(MAIN_SCREEN, f'{name}'.title().replace('_', ' '), 30, 420, size=20)
        MAIN_SCREEN.blit(sprite, (171, 461))

    @staticmethod
    def draw_bar_status(enemy, index):
        pos_x, pos_y = 46, 375
        black, red, green, blue, yellow = list(COLORS.values())[1:6]

        DrawStatusBar(100, 8, enemy[index].status_secondary['hp'], 310) \
            .draw(MAIN_SCREEN, red, pos_x, pos_y, 7, enemy[index].current_status['hp'], color_bg=black)

        DrawStatusBar(100, 8, enemy[index].status_secondary['mp'], 310) \
            .draw(MAIN_SCREEN, blue, pos_x, pos_y + 7, 7, enemy[index].current_status['mp'], color_bg=black)

        DrawStatusBar(100, 8, enemy[index].status_secondary['stamina'], 310) \
            .draw(MAIN_SCREEN, green, pos_x, pos_y + 14, 7, enemy[index].current_status['stamina'], color_bg=black)

        DrawStatusBar(100, 8, enemy[index].attributes['level'] * 15, 310) \
            .draw(MAIN_SCREEN, yellow, pos_x, pos_y + 21, 7, enemy[index].attributes['xp'], color_bg=black)


def attack_(status_att, status_def):
    battle = Battle()

    hit = status_att['attack']
    defense = status_def['defense']

    block = battle.block(status_att['block'])
    dodge = battle.parry(status_att['dodge'])
    critical = battle.critical(status_att['critical'])

    return battle.damage(hit, defense, block, dodge, critical)


def defense_(defense):
    battle = Battle()

    if battle.defense() == 'success':

        defense['defense'] += (defense['defense'] * 0.15)

    return defense
