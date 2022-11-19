import json
from typing import Optional


class Base:
    
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