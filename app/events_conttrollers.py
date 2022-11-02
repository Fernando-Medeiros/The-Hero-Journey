from settings import FOLDER, GROUPS, check_records
from .menu.menu import Menu
from .menu.newgame import NewGame
from .menu.load import Load
from .menu.options import Options
from .game import Game


class RoadMapMenu:
    class_road_map_menu = True

    group_sprites_options = GROUPS['options']
    group_sprites_load = GROUPS['load']
    group_sprites_new_game = GROUPS['new']
    group_sprites_menu = GROUPS['menu']

    menu_ = Menu(group_sprites_menu)
    new = NewGame(group_sprites_new_game)
    load = Load(group_sprites_load)
    options = Options(group_sprites_options)


    def draw(self, main_screen):
        loading = self.new.check + self.load.check

        if loading == '' and self.class_road_map_menu:

            if self.menu_.class_menu:
                self.group_sprites_menu.draw(main_screen)
                self.menu_.update()

            elif self.menu_.check == 'new' and self.new.class_new_game:
                self.group_sprites_new_game.draw(main_screen)
                self.new.update()

            elif self.menu_.check == 'load' and self.load.class_load:
                self.group_sprites_load.draw(main_screen)
                self.load.update()

            elif self.menu_.check == 'options' and self.options.class_options:
                self.group_sprites_options.draw(main_screen)
                self.options.update()

            else:
                self.menu_.class_menu = True
                self.new.class_new_game = True
                self.load.class_load = True
                self.options.class_options = True

        else:
            road_map_menu.menu_.check, road_map_menu.new.check, road_map_menu.load.check = '', '', ''
            self.class_road_map_menu = False


    def events(self, event):
        if self.class_road_map_menu:

            if self.menu_.class_menu:
                self.menu_.events_menu(event)

            elif self.menu_.check == 'new' and self.new.class_new_game:
                self.new.events_new_game(event)

            elif self.menu_.check == 'load' and self.load.class_load:
                self.load.events_load(event)

            elif self.menu_.check == 'options' and self.options.class_options:
                self.options.events_options(event)


class RoadMapGame:

    @staticmethod
    def _get_index_from_name(name):
        for index, item in enumerate(check_records(FOLDER['save'])):
            if str(name) == item[0]:
                return index
        return 0

    class_road_map_game = True

    group_sprites_game_interface = GROUPS['game']

    game_interface = Game(group_sprites_game_interface)
    index_name = 0


    def draw(self, main_screen):

        if self.class_road_map_game:

            if self.game_interface.class_game:

                self.group_sprites_game_interface.draw(main_screen)
                self.game_interface.character.index = self._get_index_from_name(self.index_name)
                self.game_interface.update(main_screen)

            else:

                self.class_road_map_game = False
                self.game_interface.class_game = True


    def events(self, event):

        if self.class_road_map_game:

            if self.game_interface.class_game:

                self.game_interface.events_game(event)



road_map_menu = RoadMapMenu()
road_map_game = RoadMapGame()