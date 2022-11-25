from random import choice, randint

from .log import Log
from .view import Views


class Battle(Log, Views):

    def __init__(self, main_screen):
        Views.__init__(self, main_screen)

    def data_character(self, char) -> tuple:
        attribute = char.attributes
        status = char.status
        current = char.current_status
        others = char.others

        return attribute, status, current, others
    

    def damage(self, hit:float, defense:float, block:float, dodge:float, critical:float) -> dict:

        damage = hit - defense

        damage = 0 if damage <= 0 else damage

        if self.block(block):
            return {'damage': 0, 'status': 'block'}
        if self.parry(dodge):
            return {'damage': 0, 'status': 'dodge'}
        if self.critical(critical):
            return {'damage': damage * 2, 'status': 'critical'}
        if damage == 0:
            return {'damage': damage, 'status': 'miss'}
        
        return {'damage': damage, 'status':''}


    def defense(self) -> bool:

        chance = 20     # 20/100

        return True if randint(0, 100) <= chance else False


    def flee(self) -> bool:

        return choice([True, False])

    
    def block(self, block: float) -> bool:

        return True if randint(0, 100) <= block else False

    
    def parry(self, dodge: float) -> bool:

        return True if randint(0, 100) <= dodge else False

    
    def critical(self, critical: float) -> bool:

        return True if randint(0, 100) <= critical else False

    
    def energy_used_in_battle(self, stamina) -> None:

        stamina['stamina'] -= 0.3

    
    def kill_sprite_enemy(self, enemy: list, index: int)  -> None:

        enemy[index].kill()
        enemy.pop(index)    


    def take_damage(self, health: dict, damage: dict, log: list)  -> None:

        log = [''] if len(log) == 0 else log

        if not 'defense' in log[-1]:

            health['hp'] -= damage['damage']

    
    def take_loots(self, char: dict, char_xp: dict, enemy: dict)  -> None:

        char['gold'] += enemy['gold']
        char['soul'] += enemy['soul']
        char_xp['xp'] += enemy['xp']


    def attack(self, att: dict, defe: dict) -> dict:

        return self.damage(
            hit=att['attack'],
            defense=defe['defense'],
            block=defe['block'],
            dodge=defe['dodge'],
            critical=att['critical'],
        )