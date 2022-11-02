
class LogBattle:

    def log_attack(self, char_name, enemy_name, damage):

        charName = char_name['name'].replace('_', ' ').title()
        enemyName = enemy_name['name'].replace('_', ' ').title()

        match damage[1]:

            case 'block':
                return f'{enemyName} BLOCKED the damage!'
            case 'dodge':
                return f'{enemyName} DODGED the damage!'
            case 'critical':
                return f'{charName} inflicted {damage[0]:.1f} CRITICAL damage!!!'
            case 'miss':
                return f'{charName} missed attack!'
            case '':
                return f'{charName} inflicts {damage[0]:.1f} damage!'

    
    def log_defense(self, name, defense) -> str:

        name_ = name['name'].replace('_', ' ').title()

        if defense:
            return f'{name_} activate defense mode.'
        
        return f"{name_} couldn't defend itself"

    
    def log_flee(self, name, flee) -> str:

        name = name['name'].replace('_', ' ').title()

        if not flee:
            return f'{name} fled the battle.'
        
        return f'{name} failed to flee from battle '

    
    def erase_log(self, *args):

        [item.clear() for item in args]