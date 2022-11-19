from random import choice, randint

from .log import LogBattle
from .view import Views


class Battle(LogBattle, Views):

    
    def data_character(self, char) -> tuple:
        attribute = char.attributes
        status = char.status
        current = char.current_status
        others = char.others

        return attribute, status, current, others


    def data_enemy(self, enemy) -> tuple:
        attribute = enemy.entity['attributes']
        status = enemy.entity['status']
        current = enemy.entity['current']

        return attribute, status, current,

    

    def damage(self, hit, defense, block, dodge, critical) -> list:

        damage = hit - defense

        damage = 0 if damage <= 0 else damage

        if block:
            return [0, 'block']
        if dodge:
            return [0, 'dodge']
        if critical:
            return [damage * 2, 'critical']
        if damage == 0:
            return [damage, 'miss']
        
        return [damage, '']


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