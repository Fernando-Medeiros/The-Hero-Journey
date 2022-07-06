from codes.opponent.opponent import Enemy
from codes.character.character import Character
from codes.battle.battle import *


class Game:
    class_game = True
    respawn_enemies = False
    turn_player, turn_enemy = False, False

    check = ''
    index_battle = 0

    group_sprites_opponent = GROUPS['opponent']

    battle = Battle()
    character = Character()

    gps = 'Sea North'

    def __init__(self, *groups):

        self._bg = Obj(IMG_GAME['bg'], 0, 0, *groups)

        self._tools = {
            'map': Obj(IMG_GAME['map'], 432, 180, *groups),
            'gps': Obj(IMG_GAME['gps'], 494, 200, *groups)
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
            'attack': Obj(IMG_GAME['b_attack'], 15, 890, *groups),
            'defense': Obj(IMG_GAME['b_defense'], 139, 890, *groups),
            'flee': Obj(IMG_GAME['b_flee'], 263, 890, *groups),
            'skills': Obj(IMG_GAME['b_skills'], 75, 925, *groups),
            'items': Obj(IMG_GAME['b_items'], 200, 925, *groups),
        }
        self._list_enemies_in_area = []

        self.log_battle = []
        self.loots_for_enemy = {}

        self._enemies_in_the_area()

        self.char_attribute, self.char_status, self.char_current, self.char_others = \
            self.battle.data_character(self.character)

        self.enemy_attribute, self.enemy_status, self.enemy_current, self.enemy_loots = \
            self.battle.data_enemy(self._list_enemies_in_area[self.index_battle])

    def _select_land(self, pos_mouse):

        index = LIST_LANDS.index(self.gps)

        if self._icons['next'].rect.collidepoint(pos_mouse):

            index = index if index + 1 >= len(LIST_LANDS) else index + 1

            self.respawn_enemies = True

            click_sound.play()

        elif self._icons['previous'].rect.collidepoint(pos_mouse):

            index = 0 if index - 1 <= 0 else index - 1

            self.respawn_enemies = True

            click_sound.play()

        self._tools['gps'].rect.topleft = (POS_GPS[index])
        self.gps = LIST_LANDS[index]

    def _lands(self):

        draw_texts(MAIN_SCREEN, f'{self.gps:^35}', 404, 104, size=25)

    def _check_enemies_for_area(self):

        idd_ = ['corrupted', 'beasts', 'slimes', 'vipers', 'whisper',
                'passage', 'mines', 'road', 'wind', 'city', 'lands',
                'golems', 'dragons', 'sea', 'draconian', 'mystical',
                'elders', 'wild elves', 'dead', 'hell', 'lizardman',
                'cursed', 'goblin', 'orc', 'grey elves', 'gnomes',
                'fomorian', 'druids', 'mages', 'dark elves', 'mythical',
                'witches', 'aesir', 'shadow', 'warriors', 'rose', 'noldor',
                'three'
                ]
        idd_name = ''

        for key in idd_:

            if key in self.gps.casefold():
                idd_name = key
                break

        return [data_list for data_list in LIST_ENEMIES if idd_name == data_list[0]]

    def _enemies_in_the_area(self):

        del self._list_enemies_in_area[::]
        for sprite in self.group_sprites_opponent.sprites():
            self.group_sprites_opponent.remove(sprite)

        try:
            y = 430
            for n in range(6):
                enemies = choice(self._check_enemies_for_area())

                self._list_enemies_in_area.append(
                    Enemy(enemies, FOLDER['enemies'] + enemies[1] + '.png', 430, y, self.group_sprites_opponent))
                y += 95

        except IndexError:
            return -1

    def _get_mouse_events(self, pos_mouse):

        mouse_collision_changing_image(
            self._icons['next'], pos_mouse, IMG_GAME['select_next'], IMG_GAME['next'])
        mouse_collision_changing_image(
            self._icons['previous'], pos_mouse, IMG_GAME['select_previous'], IMG_GAME['previous'])

        mouse_collision_changing_image(
            self._icons['save'], pos_mouse, IMG_GAME['select_save'], IMG_GAME['save'])
        mouse_collision_changing_image(
            self._icons['options'], pos_mouse, IMG_GAME['select_options'], IMG_GAME['options'])

        mouse_collision_changing_image(
            self._icons['skills'], pos_mouse, IMG_GAME['select_skills'], IMG_GAME['skills'])
        mouse_collision_changing_image(
            self._icons['marketplace'], pos_mouse, IMG_GAME['select_marketplace'], IMG_GAME['marketplace'])

        mouse_collision_changing_image(
            self._icons['proficiency'], pos_mouse, IMG_GAME['select_proficiency'], IMG_GAME['proficiency'])
        mouse_collision_changing_image(
            self._icons['chest'], pos_mouse, IMG_GAME['select_chest'], IMG_GAME['chest'])

    def _save_and_exit(self, pos_mouse):

        if self._icons['save'].rect.collidepoint(pos_mouse):
            self.character.save(), save_log()

    def _return_menu(self, pos_mouse):

        if self._icons['options'].rect.collidepoint(pos_mouse):
            self.character.save()
            self._check_enemies_for_area(), self._enemies_in_the_area()
            self.gps, self.check = 'Sea North', 'menu'
            self.class_game = False

    def _select_enemy(self, pos_mouse):

        for index, obj in enumerate(self._list_enemies_in_area):

            if obj.rect.collidepoint(pos_mouse):
                self.battle.erase_log(self.log_battle)
                self.battle.erase_loots(self.loots_for_enemy)
                self.index_battle = index
                break

    def _change_command(self, pos_mouse):

        if self.commands_battle['attack'].rect.collidepoint(pos_mouse):
            self._commands_attack()

        elif self.commands_battle['defense'].rect.collidepoint(pos_mouse):
            self._commands_defense()

        elif self.commands_battle['flee'].rect.collidepoint(pos_mouse):
            pass  # flee

        elif self.commands_battle['skills'].rect.collidepoint(pos_mouse):
            pass  # skill

        elif self.commands_battle['items'].rect.collidepoint(pos_mouse):
            pass  # itens

    def _check_index_enemy(self):

        if self.index_battle >= len(self._list_enemies_in_area):
            self.index_battle -= 1

        if len(self._list_enemies_in_area) == 0:
            self._enemies_in_the_area()

    def _update_status(self):

        self._check_index_enemy()

        self.char_attribute, self.char_status, self.char_current, self.char_others = \
            self.battle.data_character(self.character)

        self.enemy_attribute, self.enemy_status, self.enemy_current, self.enemy_loots = \
            self.battle.data_enemy(self._list_enemies_in_area[self.index_battle])

    def _commands_attack(self):

        if self.char_current['hp'] > 0:
            self.battle.erase_loots(self.loots_for_enemy)

            damage_char = attack_(self.char_status, self.enemy_status)
            self.battle.take_damage(self.enemy_current, damage_char)
            self.log_battle.append(self.battle.log_attack(self.char_attribute, damage_char))

            self.turn_enemy = True

    def _commands_defense(self):

        if self.char_current['hp'] > 0:

            self.battle.erase_loots(self.loots_for_enemy)

            defense_(self.char_status)
            self.log_battle.append(self.battle.log_defense(self.char_attribute))

            self.turn_enemy = True

    def _commands_enemy_battle(self):

        choose_movement = choice(['attack', 'defense', 'attack', 'defense', 'attack', 'defense'])

        match choose_movement:

            case 'attack':
                damage_enemy = attack_(self.enemy_status, self.char_status)

                self.battle.take_damage(self.char_current, damage_enemy)

                self.log_battle.append(self.battle.log_attack(self.enemy_attribute, damage_enemy))

            case 'defense':
                defense_(self.enemy_status)
                self.log_battle.append(self.battle.log_defense(self.enemy_attribute))

            case _:
                pass

    def _battle(self):

        self._update_status()

        pos_x, pos_y = 25, 560

        if self.turn_enemy and self.enemy_current['hp'] > 0:
            self._commands_enemy_battle()

        if self.enemy_current['hp'] <= 0:
            self.loots_for_enemy = dict(self.enemy_loots)

            self.battle.erase_log(self.log_battle)
            self.battle.take_loots(self.char_others, self.char_attribute, self.enemy_loots)

        self.battle.draw_loots(self.loots_for_enemy)
        self.battle.draw_battle_info(self.log_battle, pos_x, pos_y)
        self.battle.draw_bar_status(self._list_enemies_in_area, self.index_battle)
        self.battle.draw_sprite_enemy(self._list_enemies_in_area, self.index_battle)

        self.battle.kill_sprite_enemy(self._list_enemies_in_area, self.index_battle)

        self.turn_enemy = False

    def events_game(self, event):

        pos_mouse = pg.mouse.get_pos()

        if event.type == pg.MOUSEBUTTONDOWN:
            self._save_and_exit(pos_mouse)
            self._return_menu(pos_mouse)
            self._select_land(pos_mouse)
            self._select_enemy(pos_mouse)
            self._change_command(pos_mouse)

        if event.type == pg.MOUSEMOTION:
            self._get_mouse_events(pos_mouse)

        self.character.events_character(event)
        [obj.events(event) for obj in self._list_enemies_in_area]

    def update(self, main_screen):

        if self.respawn_enemies:
            self._check_enemies_for_area()
            self._enemies_in_the_area()
            self.battle.erase_log(self.log_battle)
            self.battle.erase_loots(self.loots_for_enemy)

            self.respawn_enemies = False

        self._battle()
        self._lands()

        self.character.update()
        self.group_sprites_opponent.draw(main_screen)

        [obj.update() for obj in self._list_enemies_in_area]

        DrawStatusBar(1, 1, 100, 373).draw(MAIN_SCREEN, COLORS['BLACK'], 15, 370, 590, 0)
