import os
from datetime import datetime

from pygame import image

from paths import FOLDERS

from ..database.character_db import CharacterDB
from .model import CharacterModel
from .view import Views

database = CharacterDB()


class Character(CharacterModel, Views):
    alive_ = True

    def __init__(self, *groups):

        CharacterModel.__init__(self)

        Views.__init__(self, *groups)

        self._assign_status_secondary()

    def _assign_status_secondary(self) -> None:

        self.health = (self.vitality / 2) * self.force + (self.level / 3)
        self.energy = (self.intelligence / 2) * self.resistance + (self.level / 3)
        self.stamina = (self.resistance / 2) + self.vitality

        self.attack = self.force + (self.agility / 3)
        self.defense = self.resistance + (self.agility / 3)
        self.dodge = self.agility / 10
        self.block = self.resistance / 10
        self.critical = self.agility / 20
        self.luck = self.level / 10

    def _check_current_status(self) -> None:
        check = ["c_health", "c_energy", "c_stamina"]

        for c_status in check:
            attr = getattr(self, c_status)
            if attr <= 0:
                setattr(self, c_status, 0)

    def _regenerate_status(self) -> None:
        time = datetime.today().second

        if time % 2 == 0:
            if self.c_health < self.health:
                self.c_health += self.r_health
            if self.c_energy < self.energy:
                self.c_energy += self.r_energy
            if self.c_stamina < self.stamina:
                self.c_stamina += self.r_stamina

    def _is_alive(self) -> None:
        self.alive_ = True if self.c_health >= 0.1 else False

    def _level_progression(self) -> None:
        def update_attr(classe: str):
            db = database.read_json("src/character/settings/classe_progression.json")

            for attr, value in db[classe].items():
                setattr(self, attr, getattr(self, attr) + value)

        if self.xp >= self.level * 15:  # next_level

            match self.classe:
                case "duelist":
                    update_attr(self.classe)
                case "mage":
                    update_attr(self.classe)
                case "warrior":
                    update_attr(self.classe)
                case "warden":
                    update_attr(self.classe)

            self.level += 1
            self.xp = 1
            self._assign_status_secondary()

    def save(self) -> None:
        exclude_attrs = [
            "_Sprite__g",
            "image",
            "rect",
            "button_status",
            "name",
            "show_status",
            "alive_",
        ]

        attrs: dict = self.__dict__.copy()

        for key in exclude_attrs:
            attrs.pop(key)

        database.save(self.name, attrs)

    def load(self) -> None:
        c_name = os.environ["CHAR_NAME"]

        if c_name:
            for key, value in database.read(c_name).items():
                setattr(self, key, value)

            self.name = c_name
            self.image = image.load("./{}{}".format(FOLDERS["classes"], self.sprite))
            self._assign_status_secondary()

            os.environ["CHAR_NAME"] = ""

    def events(self, event, pos_mouse):
        return super().events(event, pos_mouse)

    def update(self, *args, **kwargs) -> None:
        super().update(*args, **kwargs)
        self.load()
        self._is_alive()
        self._regenerate_status()
        self._check_current_status()
        self._level_progression()

    def __str__(self) -> str:
        return self.name
