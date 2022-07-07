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
            return 0
        if dodge:
            return 0
        if critical:
            return dano * 2

        return dano

    @staticmethod
    def defense():

        chance = 20
        reduces_damage_by_two = True if randint(0, 100) <= chance else False

        return reduces_damage_by_two

    @staticmethod
    def flee():

        result = choice([True, False])

        return result

    @staticmethod
    def block(block):

        result = True if randint(0, 100) <= block else False

        return result

    @staticmethod
    def parry(dodge):

        result = True if randint(0, 100) <= dodge else False

        return result

    @staticmethod
    def critical(critical):

        result = True if randint(0, 100) <= critical else False

        return result

    @staticmethod
    def energy_used_in_battle(stamina):

        stamina['stamina'] -= 0.1

        return stamina

    @staticmethod
    def kill_sprite_enemy(enemy, index):

        enemy[index].kill()
        enemy.pop(index)

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
    def log_flee(name, flee):

        name = name['name'].replace('_', ' ').title()

        if flee:
            log = f'{name} failed to flee from battle '
        else:
            log = f'{name} fled the battle.'

        return log

    @staticmethod
    def erase_log(*args):

        [item.clear() for item in args]

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

            draw_texts(MAIN_SCREEN, f'{key.title()} + {value:<10}', pos_x, pos_y, color=COLORS['GREEN'])

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

        draw_texts(MAIN_SCREEN, f'{name}'.title().replace('_', ' '), 30, 425, size=20)
        MAIN_SCREEN.blit(sprite, (171, 461))

    @staticmethod
    def draw_bar_status(*args):

        pos_x, pos_y = 46, 375

        colors = [COLORS['RED'], COLORS['BLUE'], COLORS['GREEN']]

        for items in args:

            info_0 = [items.status_secondary['hp'], items.status_secondary['mp'], items.status_secondary['stamina']]
            info_1 = [items.current_status['hp'], items.current_status['mp'],  items.current_status['stamina']]

            for index in range(len(info_0)):

                draw = DrawStatusBar(100, 8, info_0[index], 310)
                draw.draw(MAIN_SCREEN, colors[index], pos_x, pos_y, 13, info_1[index], color_bg=COLORS['BLACK'])

                pos_y += 13

    @staticmethod
    def draw_text(*args):

        pos_x, pos_y = 46, 375

        for items in args:

            info = [
                f'{items.current_status["hp"]:^45.1f}/{items.status_secondary["hp"]:^45.1f}',
                f'{items.current_status["mp"]:^45.1f}/{items.status_secondary["mp"]:^45.1f}',
                f'{items.current_status["stamina"]:^45.1f}/{items.status_secondary["stamina"]:^45.1f}'
            ]

            for index in range(len(info)):

                draw_texts(MAIN_SCREEN, info[index], pos_x, pos_y, size=10)
                pos_y += 13

    def ATTACK(self, status_att, status_def, stamina):

        hit = status_att['attack']
        critical = self.critical(status_att['critical'])

        defense = status_def['defense']
        block = self.block(status_def['block'])
        dodge = self.parry(status_def['dodge'])

        self.energy_used_in_battle(stamina)

        return self.damage(hit, defense, block, dodge, critical)

    def DEFENSE(self, defense, stamina):

        if self.defense():

            defense['defense'] += (defense['defense'] * 0.15)

        self.energy_used_in_battle(stamina)

        return defense

    def FLEE(self, stamina):

        self.energy_used_in_battle(stamina)

        return self.flee()
