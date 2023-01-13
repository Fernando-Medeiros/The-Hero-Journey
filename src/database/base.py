import json
from typing import Optional


class Base:
    def write_json(self, json_name: str, dict_to_save: dict, mode: str = "w") -> None:

        if not open(json_name, mode="w"):
            with open(json_name, mode="x", encoding="utf-8") as jsonfile:
                json.dump(dict_to_save, jsonfile)

        with open(json_name, mode=mode, encoding="utf-8") as jsonfile:
            json.dump(dict_to_save, jsonfile)

    def read_json(self, json_name: str, tag: Optional[str] = None) -> dict:
        try:
            with open(json_name, mode="r+", encoding="utf-8") as jsonfile:
                if tag:
                    return json.load(jsonfile)[tag]
                return json.load(jsonfile)
        except FileNotFoundError:
            raise FileNotFoundError

    def update(self, tag: str, name: str, data: dict, json_name: str) -> None:
        try:
            file = self.read_json(json_name)
            file[tag][name].update(data)
        except Exception as error:
            raise ValueError(error.args)
        else:
            self.write_json(json_name, file)
