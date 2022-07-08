from codes.character_opponent.opponent import Enemy
from codes.character_opponent.character import Character
from codes.battle.battle import *


class Game:

    class_game = True
    respawn_enemies, block_battle = False, False
    turn_enemy = False

    group_sprites_opponent = GROUPS['opponent']

    battle = Battle()
    character = Character()

    gps = 'Sea North'
    index_battle = 0

    def __init__(self, *groups):

        self._bg = Obj(IMG_GAME['bg'], 0, 0, *groups)

        self._tools = {
            'map': Obj(IMG_GAME['map'], 432, 180, *groups),
            'gps': Obj(IMG_GAME['gps'], 511, 184, *groups)
        }
        self._loots = {
            'gold': Obj(IMG_GAME['gold'], 435, 6, *groups),
            'soul': Obj(IMG_GAME['soul'], 568, 6, *groups)
        }
        self._icons = {
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
        self._list_enemies_in_area = []

        self.log_battle = []
        self.loots_for_enemy = {}

        self._enemies_in_the_area()

        self.char_attribute, self.char_status, self.char_current, self.char_others = \
            self.battle.data_character(self.character)

        self.enemy_attribute, self.enemy_status, self.enemy_current, self.enemy_loots = \
            self.battle.data_enemy(self._list_enemies_in_area[self.index_battle])

    def _save_and_exit(self, pos_mouse):

        if self._icons['save'].rect.collidepoint(pos_mouse):
            self.character.save(), save_log()

    def _return_menu(self, pos_mouse):

        if self._icons['options'].rect.collidepoint(pos_mouse):

            self.character.save()
            self.gps = 'Sea North'

            self._check_enemies_for_area(), self._enemies_in_the_area()
            self.battle.erase_log(self.log_battle, self.loots_for_enemy)

            self.class_game = False

    def _select_land(self, pos_mouse):

        index = LIST_LANDS.index(self.gps)

        if self.char_current['stamina'] > 1:

            if self._icons['next'].rect.collidepoint(pos_mouse):

                index = index if index + 1 >= len(LIST_LANDS) else index + 1

                self.respawn_enemies = True

                self.char_current['stamina'] -= 1
                click_sound.play()

            elif self._icons['previous'].rect.collidepoint(pos_mouse):

                index = 0 if index - 1 <= 0 else index - 1

                self.respawn_enemies = True

                self.char_current['stamina'] -= 1
                click_sound.play()

        self._tools['gps'].rect.topleft = (POS_GPS[index])
        self.gps = LIST_LANDS[index]

    def _select_enemy(self, pos_mouse):

        for index, obj in enumerate(self._list_enemies_in_area):

            if obj.rect.collidepoint(pos_mouse):
                self.battle.erase_log(self.log_battle, self.loots_for_enemy)

                self.index_battle = index
                self.block_battle = True
                break

    def _check_enemies_for_area(self):

        id_name = ''

        for key in ID_AREA:

            if key in self.gps.casefold():
                id_name = key
                break

        return [data_list for data_list in LIST_ENEMIES if id_name == data_list[0]]

    def _enemies_in_the_area(self):

        del self._list_enemies_in_area[::]

        for sprite in self.group_sprites_opponent.sprites():

            self.group_sprites_opponent.remove(sprite)

        y = 430
        for n in range(6):
            enemies = choice(self._check_enemies_for_area())

            enemy_obj = Enemy(enemies, FOLDER['enemies'] + enemies[1] + '.png', 430, y, self.group_sprites_opponent)

            self._list_enemies_in_area.append(enemy_obj)
            y += 95

    def _check_index_enemy(self):

        if self.index_battle >= len(self._list_enemies_in_area):
            self.index_battle -= 1

        if len(self._list_enemies_in_area) <= 0:
            self._enemies_in_the_area()

    def _change_command(self, pos_mouse):

        if self.char_current['hp'] > 0.1 and self.char_current['stamina'] >= 0.3 and self.enemy_current['hp'] > 0:

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

        damage_char = self.battle.ATTACK(self.char_status, self.enemy_status)

        self.battle.energy_used_in_battle(self.char_current)

        self.battle.take_damage(self.enemy_current, damage_char, self.log_battle)

        self.log_battle.append(self.battle.log_attack(self.char_attribute, self.enemy_attribute, damage_char))

    def _commands_defense(self):

        defense = self.battle.defense()

        self.battle.energy_used_in_battle(self.char_current)

        self.log_battle.append(self.battle.log_defense(self.char_attribute, defense))

    def _commands_flee(self):

        self.block_battle = self.battle.flee()

        self.battle.energy_used_in_battle(self.char_current)

        self.log_battle.append(self.battle.log_flee(self.char_attribute, self.block_battle))

    def _commands_enemy_battle(self):

        if self.turn_enemy and self.enemy_current['hp'] > 0.1 and self.enemy_current['stamina'] >= 0.3:

            choose_movement = choice(['attack', 'attack', 'defense'])

            match choose_movement:

                case 'attack':
                    damage_enemy = self.battle.ATTACK(self.enemy_status, self.char_status)

                    self.battle.energy_used_in_battle(self.enemy_current)

                    self.battle.take_damage(self.char_current, damage_enemy, self.log_battle)

                    self.log_battle.append(self.battle.log_attack(self.enemy_attribute, self.char_attribute, damage_enemy))

                case 'defense':
                    defense = self.battle.defense()

                    self.battle.energy_used_in_battle(self.enemy_current)

                    self.log_battle.append(self.battle.log_defense(self.enemy_attribute, defense))

    def _battle(self):

        self._update_status()

        self._draw_battle()

        self._commands_enemy_battle()

        if self.enemy_current['hp'] <= 0:

            self.loots_for_enemy = dict(self.enemy_loots)
            self.block_battle = False

            self.battle.erase_log(self.log_battle)
            self.battle.take_loots(self.char_others, self.char_attribute, self.enemy_loots)

            self.battle.kill_sprite_enemy(self._list_enemies_in_area, self.index_battle)

        self.turn_enemy = False

    def _draw_name_of_land(self):

        draw_texts(MAIN_SCREEN, f'{self.gps:^35}', 404, 104, size=25)

    def _draw_battle(self):

        self.battle.draw_loots(self.loots_for_enemy)
        self.battle.draw_battle_info(self.log_battle)

        self.battle.draw_bar_status(self._list_enemies_in_area[self.index_battle])
        self.battle.draw_info_status_enemy(self._list_enemies_in_area[self.index_battle])

        self.battle.draw_enemy_sprite(self._list_enemies_in_area, self.index_battle)

        color_block = COLORS['YELLOW'] if self.block_battle else COLORS['WHITE']

        DrawStatusBar(1, 1, 100, 373).draw(MAIN_SCREEN, COLORS['BLACK'], 15, 370, 590, 0, color_bg=color_block)

    def _get_mouse_events(self, pos_mouse):

        for key in self._icons.keys():

            if self._icons[key].rect.collidepoint(pos_mouse):

                __img = 'select_' + key
            else:
                __img = key

            self._icons[key].image = pg.image.load(IMG_GAME[__img])

        for key in self.commands_battle.keys():

            if self.commands_battle[key].rect.collidepoint(pos_mouse):

                __img = 'select_' + key
            else:
                __img = key

            self.commands_battle[key].image = pg.image.load(IMG_GAME[__img])

    def _update_status(self):

        self._check_index_enemy()

        self.char_attribute, self.char_status, self.char_current, self.char_others = \
            self.battle.data_character(self.character)

        self.enemy_attribute, self.enemy_status, self.enemy_current, self.enemy_loots = \
            self.battle.data_enemy(self._list_enemies_in_area[self.index_battle])

    def events_game(self, event):

        pos_mouse = pg.mouse.get_pos()

        if event.type == pg.MOUSEBUTTONDOWN:

            self._change_command(pos_mouse)

            if not self.block_battle:
                self._select_land(pos_mouse)
                self._select_enemy(pos_mouse)
                self._save_and_exit(pos_mouse)
                self._return_menu(pos_mouse)

        if event.type == pg.MOUSEMOTION:
            self._get_mouse_events(pos_mouse)

        self.character.events_character(event)
        [obj.events(event) for obj in self._list_enemies_in_area]

    def update(self, main_screen):

        if self.respawn_enemies:

            self._check_enemies_for_area()
            self._enemies_in_the_area()
            self.battle.erase_log(self.log_battle, self.loots_for_enemy)
            self.respawn_enemies = False

        self._battle()
        self._draw_name_of_land()

        self.character.update()
        self.group_sprites_opponent.draw(main_screen)

        [obj.update() for obj in self._list_enemies_in_area]
