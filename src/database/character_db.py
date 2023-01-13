from .base import Base


class CharacterDB(Base):
    classes = "src/character/settings/classes.json"
    path = "src/database/db/characters.json"

    def create_model(self, name: str, ethnicity: str, classe: str) -> dict:
        model = {
            name.strip().casefold(): {
                "name": name,
                "classe": classe,
                "ethnicity": ethnicity,
                "level": 1,
                "location": "Sea North",
                "sprite": "{}-{}.png".format(ethnicity, classe),
                "xp": 1,
                "gold": 1,
                "soul": 1,
            }
        }

        status = self.read_json(self.classes)
        model[name].update(status[ethnicity][classe])
        return model

    def create(self, name: str, ethnicity: str, classe: str) -> None:
        collection = self.read_json(self.path)
        collection.update(self.create_model(name, ethnicity, classe))
        self.write_json(self.path, collection)

    def read(self, name: str) -> dict:
        return self.read_json(self.path)[name]

    def save(self, name: str, save: dict) -> None:
        collection = self.read_json(self.path)
        collection[name].update(save)
        self.write_json(self.path, collection)

    def delete(self, name: str) -> None:
        collection = self.read_json(self.path)
        collection.pop(name)
        self.write_json(self.path, collection)

    def get_all(self) -> dict:
        return self.read_json(self.path)
