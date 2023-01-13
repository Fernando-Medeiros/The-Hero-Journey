from random import choice, randint

from .base import Base


def attr(min_: int, max_: int) -> int:
    return randint(min_, max_)


def replace(n: str, c=list("./_-(),^|<>;:`´")) -> str:
    for crt in list(n):
        if crt in c:
            n = n.replace(crt, " ")
    return n


class EnemyDB(Base):
    db = "src/database/db/enemies.json"

    def create_model(self, name: str, level: int, img_name: str) -> dict:
        level = int(level)
        model = {
            replace(name): {
                "level": level,
                "xp": attr(1, level + 3),
                "gold": attr(1, level + 3),
                "soul": attr(1, level + 3),
                "force": attr(level, level * 2),
                "agility": attr(level, level * 2),
                "vitality": attr(level, level * 2),
                "intelligence": attr(level, level * 2),
                "resistance": attr(level, level * 2),
                "sprite": "{}.png".format(img_name),
            }
        }
        return model

    def get_random_enemy_by_tag(self, tag: str, json_name: str = db) -> dict:
        try:
            collection: dict[str, dict] = self.read_json(json_name, tag=tag)
            one_entity = choice(list(collection.items()))
            enemy: dict = one_entity[1]
            enemy["name"] = one_entity[0]

        except Exception as error:
            raise FileNotFoundError(f"{error.args}")
        else:
            return enemy
