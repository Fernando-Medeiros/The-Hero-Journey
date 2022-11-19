import json
from random import choice, randint
from typing import Optional


class EnemieDB:

    def write_json_db(self,
        json_name: str,
        dict_to_save: dict) -> None:

        if not open(json_name, mode='w'):
            with open(json_name, mode='x', encoding='utf-8') as jsonfile:
                json.dump(dict_to_save ,jsonfile)            
        
        with open(json_name, mode='w', encoding='utf-8') as jsonfile:
            json.dump(dict_to_save ,jsonfile)
        

    def read_json_db(self,
        json_name: str,
        tag: Optional[str] = None) -> dict:
        
        try:
            with open(json_name, mode='r+', encoding='utf-8') as jsonfile:
                if tag:
                    return json.load(jsonfile)[tag]           
                return json.load(jsonfile)
        except:
            raise FileNotFoundError('File not found')


    def create_enemy_model(self,
        name: str,
        level: int,
        img_name: str) -> dict:
        
        def attr(min: int, max: int) -> int:
            return randint(min, max)
        
        def clear_the_name(name: str, c=list("./_-(),^|<>;:`´")) -> str:
            for crt in list(name):
                if crt in c:
                    name = name.replace(crt, ' ')
            return name

        level = int(level)
        name = clear_the_name(name)
        entity = {name: {
                'level':level,
                'xp': attr(1, level + 3),
                'gold': attr(1, level + 3),
                'soul': attr(1, level + 3),
                'force': attr(level, level * 2),
                'agility': attr(level, level * 2),
                'vitality': attr(level, level * 2),
                'intelligence': attr(level, level * 2),
                'resistance': attr(level, level * 2),
                'sprite': '{}.png'.format(img_name)
                }}
        return entity


    def update_enemy(self,
        json_name: str,
        tag: str,
        name: str,
        data: dict) -> None:
    
        try:
            file = self.read_json_db(json_name)
            file[tag][name].update(data)
        except Exception as error:
            raise ValueError(error.args)
        else:
            self.write_json_db(json_name, file)
    

    def get_random_enemy_by_tag(self, json_name: str, tag: str) -> dict:
        try:
            collection: dict[str, dict] = self.read_json_db(json_name, tag=tag)
            one_entity: list = choice(list(collection.items()))  # type: ignore
            enemy: dict = one_entity[1]
            enemy['name'] = one_entity[0]

        except Exception as error:
            raise FileNotFoundError(f'{error.args}')
        else:
            return enemy