from datetime import datetime

from pygame import Surface

from ..database.enemy_db import EnemieDB
from .model import EnemyModel
from .view import Views


class Enemy(EnemyModel, Views):

    alive_ = True
    
    db = EnemieDB()

    def __init__(self, tag: str, pos_x: int, pos_y: int, main_screen: Surface, *groups):

        self._update_entity(tag)

        EnemyModel.__init__(self)   

        Views.__init__(self, main_screen, pos_x, pos_y, *groups)
        
        self._assign_status_secondary_and_current()       


    def _update_entity(self, tag: str) -> None:
        self.classe = tag
        entity: dict = self.db.get_random_enemy_by_tag(tag)

        for key, value in entity.items():
            setattr(self, key, value)


    def _assign_status_secondary_and_current(self) -> None:

        self.health = (self.vitality / 2) * self.force + (self.level / 3)
        self.energy = (self.intelligence / 2) * self.resistance + (self.level / 3)
        self.stamina = (self.resistance / 2) + self.vitality

        self.attack = self.force + (self.agility / 3)
        self.defense = self.resistance + (self.agility / 3)
        self.dodge = self.agility / 10
        self.block = self.resistance / 10
        self.critical = self.agility / 20
        self.luck = self.level / 10

        self.c_health = self.health
        self.c_energy = self.energy
        self.c_stamina = self.stamina      


    def _check_current_status(self) -> None:
        check = ['c_health', 'c_energy', 'c_stamina']

        for c_status in check:
            attr = getattr(self, c_status)
            if attr <= 0:
                setattr(self, c_status, 0)


    def _regenerate_status(self) -> None:       
        time = datetime.today().second

        if time % 2 == 0:            
            if self.c_health < self.health: self.c_health += self.r_health 
            if self.c_energy < self.energy: self.c_energy += self.r_energy 
            if self.c_stamina < self.stamina: self.c_stamina += self.r_stamina


    def _is_alive(self) -> None:     
        
        if self.c_health >= 0.1:
            self._regenerate_status()
        else:
            self.alive_ = False 
    

    def events(self, pos_mouse):
        self._draw_status(pos_mouse)


    def update(self):
        self._is_alive()
        self._check_current_status()
        self._draw_name_and_level()
        self._draw_status_on_hover()
    
    
    def __str__(self) -> str:
        return self.name