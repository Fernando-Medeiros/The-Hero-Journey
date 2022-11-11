from random import randint, choice

from .view import Views
from .log import LogBattle


class Battle(LogBattle, Views):

    
    def data_character(self, char) -> tuple:
        char_attribute = char.attributes
        char_status = char.status
        char_current = char.current_status
        char_others = char.others

        return char_attribute, char_status, char_current, char_others


    def data_enemy(self, enemy) -> tuple:
        enemy_attribute = enemy.attributes
        enemy_status = enemy.status
        enemy_current = enemy.current_status
        enemy_loots = enemy.loots

        return enemy_attribute, enemy_status, enemy_current, enemy_loots

    

    def damage(self, hit, defense, block, dodge, critical) -> list:

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
        
        return [dano, '']


    def defense(self,) -> bool:

        chance = 20

        return True if randint(0, 100) <= chance else False


    def flee(self) -> bool:

        return choice([True, False])

    
    def block(self, block) -> bool:

        return True if randint(0, 100) <= block else False

    
    def parry(self, dodge) -> bool:

        return True if randint(0, 100) <= dodge else False

    
    def critical(self, critical) -> bool:

        return True if randint(0, 100) <= critical else False

    

    def energy_used_in_battle(self, stamina):

        stamina['stamina'] -= 0.3

    
    def kill_sprite_enemy(self, enemy, index):

        enemy[index].kill()
        enemy.pop(index)    


    def take_damage(self, hp, damage, log):

        log = [''] if len(log) == 0 else log

        if not 'defense' in log[-1]:

            hp['hp'] -= damage[0]

    
    def take_loots(self, gold_soul, xp, enemy_loot):

        gold_soul['gold'] += enemy_loot['gold']
        gold_soul['soul'] += enemy_loot['soul']
        xp['xp'] += enemy_loot['xp']


    def ATTACK(self, status_att, status_def):

        hit = status_att['attack']
        critical = self.critical(status_att['critical'])

        defense = status_def['defense']
        block = self.block(status_def['block'])
        dodge = self.parry(status_def['dodge'])

        return self.damage(hit, defense, block, dodge, critical)