from random import choice

import pygame as pg

from app.battle.battle import Battle
from app.character.character import Character
from app.database.enemies_db import EnemieDB
from app.database.map_db import MapDB
from app.functiontools import (COLORS, Obj, draw_rect, draw_texts,
                               save_log_and_exit)
from app.opponent.opponent import Enemy
from paths import *

from .sound import SONGS

SONGS['orpheus'].play()


class Events:

    def __init__(self, *groups):

        self.bg = Obj(IMG_GAME['bg'], 0, 0, *groups)
        
        self.tools = {
            'map': Obj(IMG_GAME['map'], 432, 180, *groups),
            'gps': Obj(IMG_GAME['gps'], 511, 184, *groups)
        }
        self.loots = {
            'gold': Obj(IMG_GAME['gold'], 435, 6, *groups),
            'soul': Obj(IMG_GAME['soul'], 568, 6, *groups)
        }
        self.icons = {
            'options': Obj(IMG_GAME['options'], 15, 980, *groups),
            'skills': Obj(IMG_GAME['skills'], 68, 980, *groups),
            'marketplace': Obj(IMG_GAME['marketplace'], 121, 980, *groups),
            'proficiency': Obj(IMG_GAME['proficiency'], 174, 980, *groups),
            'chest': Obj(IMG_GAME['chest'], 227, 980, *groups),
            'save': Obj(IMG_GAME['save'], 354, 980, *groups),
            'next': Obj(IMG_GAME['next'], 712, 104, *groups),
            'previous': Obj(IMG_GAME['previous'], 404, 104, *groups),
        }
        self.commands_battle = {
            'b_attack': Obj(IMG_GAME['b_attack'], 15, 890, *groups),
            'b_defense': Obj(IMG_GAME['b_defense'], 139, 890, *groups),
            'b_flee': Obj(IMG_GAME['b_flee'], 263, 890, *groups),
            'b_skills': Obj(IMG_GAME['b_skills'], 75, 925, *groups),
            'b_items': Obj(IMG_GAME['b_items'], 200, 925, *groups),
        }

    def _save_and_exit(self, pos_mouse):
    
        if self.icons['save'].rect.collidepoint(pos_mouse):

            self.character.save()
            save_log_and_exit()

    def _return_menu(self, pos_mouse):

        if self.icons['options'].rect.collidepoint(pos_mouse):

            self.character.save()

            self.location = 'Sea North'

            self._enemies_in_the_area()

            self.battle.erase_log(self.log_battle, self.loots_for_enemy)

            self.is_active = False

    def _select_land(self, pos_mouse):

        index = self.map['name'].index(self.location)

        if self.char_current['stamina'] >= 0.5:

            if self.icons['next'].rect.collidepoint(pos_mouse):

                index = index if index + 1 >= len(self.map['name']) else index + 1

                self.respawn_enemies = True

                self.char_current['stamina'] -= 0.5
              

            elif self.icons['previous'].rect.collidepoint(pos_mouse):

                index = 0 if index - 1 <= 0 else index - 1

                self.respawn_enemies = True

                self.char_current['stamina'] -= 0.5
              

        self.tools['gps'].rect.topleft = (self.map['pos'][index])

        self.location = self.map['name'][index]

        self.character.location = self.location

    def _select_enemy(self, pos_mouse):

        for index, obj in enumerate(self.list_enemies_in_area):

            if obj.rect.collidepoint(pos_mouse):

                self.battle.erase_log(self.log_battle, self.loots_for_enemy)

                self.index_battle = index

                self.block_battle = True
                break
    
    def _get_mouse_events_to_show_interactive(self, pos_mouse):
        
        for key in self.icons.keys():

            if self.icons[key].rect.collidepoint(pos_mouse):

                img = 'select_' + key
            else:
                img = key

            self.icons[key].image = pg.image.load(IMG_GAME[img])

        for key in self.commands_battle.keys():

            if self.commands_battle[key].rect.collidepoint(pos_mouse):

                img = 'select_' + key
            else:
                img = key

            self.commands_battle[key].image = pg.image.load(IMG_GAME[img])


class Game(Events):

    is_active = True

    block_battle = False

    respawn_enemies = False

    turn_enemy = False

    index_battle = 0

    group_opponent = pg.sprite.Group()
    enemie_db = EnemieDB()
    map_db = MapDB()

    def __init__(self, main_screen: pg.Surface, *groups):
        
        Events.__init__(self, *groups)
        
        self.main_screen = main_screen
        
        self.battle = Battle(main_screen)

        self.character = Character(main_screen)
        
        self.list_enemies_in_area: list[object] = []

        self.location: str  = self.character.location

        self.map: dict = self.map_db.get_map_info()

        self.log_battle = []

        self.loots_for_enemy = {}

        self._enemies_in_the_area() 
                

    def _enemies_in_the_area(self):
    
        tag = [tag for tag in self.map['tag'] if tag in self.location.casefold()]

        del self.list_enemies_in_area[::]

        [self.group_opponent.remove(sprite) for sprite in self.group_opponent.sprites()]
        
        def add_enemy():        
            pos_y = 430
            for cnt in range(6):
                     
                enemy: dict = self.enemie_db.get_random_enemy_by_tag(*tag)

                self.list_enemies_in_area.append(
                    Enemy(
                        enemy,    
                        '{}{}'.format(FOLDERS['enemies'], enemy['sprite']),
                        430,
                        pos_y,
                        self.main_screen,
                        self.group_opponent)
                    )
                pos_y += 95

        add_enemy()


    def _update_location(self) -> None:
        
        self.location = self.character.location

        if self.index_battle >= len(self.list_enemies_in_area):

            self.index_battle -= 1

        if len(self.list_enemies_in_area) <= 0:

            self._enemies_in_the_area()

        draw_texts(
            screen=self.main_screen,
            text='{:^35}'.format(self.location),
            pos_x=404,
            pos_y=104,
            size=25
        )


    def _change_command(self, pos_mouse):

        if self.char_current['hp'] > 0 and self.char_current['stamina'] >= 0.3 and self.enemy['current']['hp'] > 0:

            for key in self.commands_battle.keys():

                if self.commands_battle[key].rect.collidepoint(pos_mouse):

                    self.block_battle = True

                    match key:

                        case 'b_attack':
                            self._commands_attack()

                        case 'b_defense':
                            self._commands_defense()

                        case 'b_flee':
                            self._commands_flee()

                        case 'b_skills':
                            pass

                        case 'b_items':
                            pass

                    self.turn_enemy = True
                    self.battle.erase_log(self.loots_for_enemy)


    def _commands_attack(self):

        damage: dict = self.battle.attack(
            att=self.char_status,
            defe=self.enemy['status'])

        self.battle.energy_used_in_battle(self.char_current)

        self.battle.take_damage(self.enemy['current'], damage, self.log_battle)

        self.log_battle.append(self.battle.log_attack(self.char_attribute, self.enemy['attributes'], damage))


    def _commands_defense(self):

        self.battle.energy_used_in_battle(self.char_current)

        self.log_battle.append(self.battle.log_defense(self.char_attribute, self.battle.defense()))


    def _commands_flee(self):

        self.block_battle: bool = self.battle.flee()

        self.battle.energy_used_in_battle(self.char_current)

        self.log_battle.append(self.battle.log_flee(self.char_attribute, self.block_battle))


    def _commands_enemy_battle(self):

        if self.turn_enemy and self.enemy['current']['hp'] > 0 and self.enemy['current']['stamina'] >= 0.3:

            action = choice(['attack', 'attack', 'defense'])

            match action:

                case 'attack':
                    damage_enemy: dict = self.battle.attack(self.enemy['status'], self.char_status)

                    self.battle.energy_used_in_battle(self.enemy['current'])

                    self.battle.take_damage(self.char_current, damage_enemy, self.log_battle)

                    self.log_battle.append(self.battle.log_attack(self.enemy['attributes'], self.char_attribute, damage_enemy))

                case 'defense':
                  
                    self.battle.energy_used_in_battle(self.enemy['current'])

                    self.log_battle.append(self.battle.log_defense(self.enemy['attributes'], self.battle.defense()))


    def _battle(self):

        self._update_status()

        self._draw_battle()

        self._commands_enemy_battle()

        if self.enemy['current']['hp'] <= 0:

            self.loots_for_enemy = self.enemy['attributes']

            self.battle.take_loots(self.char_others, self.char_attribute, self.enemy['attributes'])

            self.battle.erase_log(self.log_battle)

            self.block_battle = False

            self.battle.kill_sprite_enemy(self.list_enemies_in_area, self.index_battle)

        self.turn_enemy = False



    def _draw_battle(self):

        self.battle.draw_loots(self.loots_for_enemy)

        self.battle.draw_battle_info(self.log_battle)

        self.battle.draw_bar_status(self.list_enemies_in_area[self.index_battle])

        self.battle.draw_info_status_enemy(self.list_enemies_in_area[self.index_battle])

        self.battle.draw_enemy_sprite(self.list_enemies_in_area, self.index_battle)

        color_block = COLORS['YELLOW'] if self.block_battle else COLORS['WHITE']

        draw_rect(
            screen=self.main_screen,
            color=color_block,
            rect=[15, 370, 373, 590]
        )



    def _update_status(self):

        self.char_attribute, self.char_status, self.char_current, self.char_others = \
            self.battle.data_character(self.character)

        self.enemy = self.list_enemies_in_area[self.index_battle].entity



    def events(self, event):

        pos_mouse = pg.mouse.get_pos()

        if event.type == pg.MOUSEBUTTONDOWN:

            self._change_command(pos_mouse)

            if not self.block_battle:

                self._select_land(pos_mouse)
                self._select_enemy(pos_mouse)
                self._save_and_exit(pos_mouse)
                self._return_menu(pos_mouse)

        self._get_mouse_events_to_show_interactive(pos_mouse)

        self.character.events(event, pos_mouse)

        [obj.events(pos_mouse) for obj in self.list_enemies_in_area]


    def update(self):
        
        if self.respawn_enemies:

            self._enemies_in_the_area()

            self.battle.erase_log(self.log_battle, self.loots_for_enemy)

            self.respawn_enemies = False

        self._battle()
        
        self._update_location()

        self.character.update()

        self.group_opponent.draw(self.main_screen)
     
        [obj.update() for obj in self.list_enemies_in_area]