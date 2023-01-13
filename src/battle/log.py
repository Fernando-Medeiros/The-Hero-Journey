def replace(str_: str) -> str:
    return str_.replace("_", " ").title()


class Log:
    def log_attack(self, c_name: str, e_name: str, damage: dict) -> str:
        char_name = replace(c_name)
        enemy_name = replace(e_name)

        match damage["status"]:

            case "block":
                return f"{enemy_name} BLOCKED the damage!"
            case "dodge":
                return f"{enemy_name} DODGED the damage!"
            case "critical":
                return (
                    f'{char_name} inflicted {damage["damage"]:.1f} CRITICAL damage!!!'
                )
            case "miss":
                return f"{char_name} missed attack!"

        return f'{char_name} inflicts {damage["damage"]:.1f} damage!'

    def log_defense(self, name: str, defense: bool) -> str:
        n = replace(name)

        if defense:
            return f"{n} activate defense mode."

        return f"{n} couldn't defend itself"

    def log_flee(self, name: str, flee: bool) -> str:
        n = replace(name)

        if not flee:
            return f"{n} fled the battle"

        return f"{n} failed to flee from battle"

    def erase_log(self, *args) -> None:
        [item.clear() for item in args]
