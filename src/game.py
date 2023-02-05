from random import choice

import pygame as pg

from paths import *

from .battle.battle import Battle
from .character.character import Character
from .database.map_db import MapDB
from .opponent.enemy import Enemy
from .sound import SONGS
from .tools import COLORS, Obj, draw_rect, draw_texts, save_log_and_exit

SONGS["orpheus"].play()


class View:
    def __init__(self, *groups):

        self.bg = Obj(IMG_GAME["bg"], 0, 0, *groups)

        self.objects = {
            "map": Obj(IMG_GAME["map"], 432, 180, *groups),
            "gps": Obj(IMG_GAME["gps"], 511, 184, *groups),
            "gold": Obj(IMG_GAME["gold"], 435, 6, *groups),
            "soul": Obj(IMG_GAME["soul"], 568, 6, *groups),
            "icons": {
                "options": Obj(IMG_GAME["options"], 15, 980, *groups),
                "skills": Obj(IMG_GAME["skills"], 68, 980, *groups),
                "marketplace": Obj(IMG_GAME["marketplace"], 121, 980, *groups),
                "proficiency": Obj(IMG_GAME["proficiency"], 174, 980, *groups),
                "chest": Obj(IMG_GAME["chest"], 227, 980, *groups),
                "save": Obj(IMG_GAME["save"], 354, 980, *groups),
                "next": Obj(IMG_GAME["next"], 712, 104, *groups),
                "previous": Obj(IMG_GAME["previous"], 404, 104, *groups),
            },
            "commands": {
                "b_attack": Obj(IMG_GAME["b_attack"], 15, 890, *groups),
                "b_defense": Obj(IMG_GAME["b_defense"], 139, 890, *groups),
                "b_flee": Obj(IMG_GAME["b_flee"], 263, 890, *groups),
                "b_skills": Obj(IMG_GAME["b_skills"], 75, 925, *groups),
                "b_items": Obj(IMG_GAME["b_items"], 200, 925, *groups),
            },
        }


class Game(View):
    is_active = True
    block_battle = False
    respawn_enemies = False
    turn_enemy = False
    index_battle = 0

    group_character = pg.sprite.Group()
    group_opponent = pg.sprite.Group()
    map_db = MapDB()

    main_screen = pg.display.get_surface()

    def __init__(self, *groups):

        View.__init__(self, *groups)

        self.battle = Battle()
        self.character = Character(self.group_character)

        self.location: str = self.character.location
        self.map: dict = self.map_db.get_map_info()

        self.log_battle = []
        self.loots_for_enemy = {}
        self.l_enemies_in_the_area: list[object] = []

        self._enemies_in_the_area()

    # GAME EVENTS
    def _save_and_exit(self, pos_mouse):
        if self.objects["icons"]["save"].rect.collidepoint(pos_mouse):
            self.character.save()
            save_log_and_exit()

    def _return_menu(self, pos_mouse):
        if self.objects["icons"]["options"].rect.collidepoint(pos_mouse):
            self.character.save()
            self._enemies_in_the_area()
            self.battle.erase_log(self.log_battle, self.loots_for_enemy)

            self.is_active = False

    def _select_land(self, pos_mouse):

        index = self.map["name"].index(self.location)

        if self.character.c_stamina >= 0.5:
            if self.objects["icons"]["next"].rect.collidepoint(pos_mouse):

                index = index if index + 1 >= len(self.map["name"]) else index + 1

                self.respawn_enemies = True
                self.character.c_stamina -= 0.5

            elif self.objects["icons"]["previous"].rect.collidepoint(pos_mouse):

                index = 0 if index - 1 <= 0 else index - 1

                self.respawn_enemies = True
                self.character.c_stamina -= 0.5

        self.objects["gps"].rect.topleft = self.map["pos"][index]
        self.location = self.map["name"][index]
        self.character.location = self.location

    def _select_enemy(self, pos_mouse):
        for index, obj in enumerate(self.l_enemies_in_the_area):
            if obj.rect.collidepoint(pos_mouse):
                self.battle.erase_log(self.log_battle, self.loots_for_enemy)
                self.index_battle = index
                self.block_battle = True
                break

    def _draw_icons_on_hover(self, pos_mouse):
        def inner(objs: dict):
            for obj in objs:
                sprite = obj
                if objs[obj].rect.collidepoint(pos_mouse):
                    sprite = "select_" + obj
                objs[obj].image = pg.image.load(IMG_GAME[sprite])

        inner(self.objects["icons"])
        inner(self.objects["commands"])

    # GAME CONTROL
    def _enemies_in_the_area(self) -> None:

        tag = [tag for tag in self.map["tag"] if tag in self.location.casefold()]

        del self.l_enemies_in_the_area[::]

        [self.group_opponent.remove(sprite) for sprite in self.group_opponent.sprites()]

        pos_y = 430

        for cnt in range(6):
            unpack = [*tag, 430, pos_y, self.main_screen, self.group_opponent]
            self.l_enemies_in_the_area.append(Enemy(*unpack))

            pos_y += 95

    def _update_location(self) -> None:

        self.location = self.character.location

        if self.index_battle >= len(self.l_enemies_in_the_area):
            self.index_battle -= 1

        if len(self.l_enemies_in_the_area) <= 0:
            self._enemies_in_the_area()

        draw_texts(
            screen=self.main_screen,
            text="{:^35}".format(self.location),
            pos_x=404,
            pos_y=104,
            size=25,
        )

    def _change_command(self, pos_mouse):

        if (
            self.character.c_health > 0
            and self.character.c_stamina >= 0.3
            and self.enemy.c_health > 0
        ):

            for key, action in self.objects["commands"].items():

                if action.rect.collidepoint(pos_mouse):

                    self.block_battle = True

                    match key:
                        case "b_attack":
                            self._commands_attack()
                        case "b_defense":
                            self._commands_defense()
                        case "b_flee":
                            self._commands_flee()
                        case "b_skills":
                            pass
                        case "b_items":
                            pass

                    self.turn_enemy = True
                    self.battle.erase_log(self.loots_for_enemy)

    def _commands_attack(self):

        damage: dict = self.battle.attack(att=self.character, defe=self.enemy)

        self.battle.energy_used_in_battle(self.character)

        self.battle.take_damage(self.enemy, damage, self.log_battle)

        self.log_battle.append(
            self.battle.log_attack(self.character.name, self.enemy.name, damage)
        )

    def _commands_defense(self):

        self.battle.energy_used_in_battle(self.character)

        self.log_battle.append(
            self.battle.log_defense(self.character.name, self.battle.defense())
        )

    def _commands_flee(self):

        self.block_battle: bool = self.battle.flee()

        self.battle.energy_used_in_battle(self.character)

        self.log_battle.append(
            self.battle.log_flee(self.character.name, self.block_battle)
        )

    def _commands_enemy_battle(self):

        if self.turn_enemy and self.enemy.c_health > 0 and self.enemy.c_stamina >= 0.3:

            action = choice(["attack", "attack", "defense"])

            match action:

                case "attack":
                    damage_enemy: dict = self.battle.attack(self.enemy, self.character)

                    self.battle.energy_used_in_battle(self.enemy)

                    self.battle.take_damage(
                        self.character, damage_enemy, self.log_battle
                    )

                    self.log_battle.append(
                        self.battle.log_attack(
                            self.enemy.name, self.character.name, damage_enemy
                        )
                    )

                case "defense":

                    self.battle.energy_used_in_battle(self.enemy)

                    self.log_battle.append(
                        self.battle.log_defense(self.enemy.name, self.battle.defense())
                    )

    def _battle(self):
        self.enemy = self.l_enemies_in_the_area[self.index_battle]

        self._draw_battle()
        self._commands_enemy_battle()

        if self.enemy.c_health <= 0:
            self.loots_for_enemy = {
                "xp": self.enemy.xp,
                "gold": self.enemy.gold,
                "soul": self.enemy.soul,
            }

            self.battle.take_loots(self.character, self.enemy)
            self.battle.erase_log(self.log_battle)

            self.block_battle = False
            self.battle.kill_sprite_enemy(self.l_enemies_in_the_area, self.index_battle)

        self.turn_enemy = False

    def _draw_battle(self):

        self.battle.draw_loots(self.loots_for_enemy)

        self.battle.draw_log(self.log_battle)

        self.battle.draw_enemy_bar_status(self.l_enemies_in_the_area[self.index_battle])

        self.battle.draw_enemy_info_status(
            self.l_enemies_in_the_area[self.index_battle]
        )

        self.battle.draw_enemy(self.l_enemies_in_the_area[self.index_battle])

        color_block = COLORS["YELLOW"] if self.block_battle else COLORS["WHITE"]

        draw_rect(screen=self.main_screen, color=color_block, rect=[15, 370, 373, 590])

    def events(self, event, pos_mouse):

        if event.type == pg.MOUSEBUTTONDOWN:
            self._change_command(pos_mouse)

            if not self.block_battle:
                self._select_land(pos_mouse)
                self._select_enemy(pos_mouse)
                self._save_and_exit(pos_mouse)
                self._return_menu(pos_mouse)

        self._draw_icons_on_hover(pos_mouse)

        self.character.events(event, pos_mouse)

        [enemy.events(pos_mouse) for enemy in self.l_enemies_in_the_area]

    def update(self):

        if self.respawn_enemies:
            self._enemies_in_the_area()
            self.battle.erase_log(self.log_battle, self.loots_for_enemy)
            self.respawn_enemies = False

        self._battle()
        self._update_location()
        self.character.update()

        self.group_character.draw(self.main_screen)
        self.group_opponent.draw(self.main_screen)

        [enemy.update() for enemy in self.l_enemies_in_the_area]
