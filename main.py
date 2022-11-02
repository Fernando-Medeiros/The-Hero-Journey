from settings import (
        DATETIME_INIT_APP, FRAMES, MAIN_SCREEN,
        save_log_and_exit, pg)

from app.events_conttrollers import road_map_menu, road_map_game



def draw():
    if road_map_menu.class_road_map_menu:
        road_map_menu.draw(MAIN_SCREEN)

    elif road_map_game.class_road_map_game:

        road_map_game.index_name = road_map_menu.load.name_for_loading + road_map_menu.new.name_for_loading
        road_map_game.draw(MAIN_SCREEN)

    else:
        road_map_menu.class_road_map_menu = True
        road_map_game.class_road_map_game = True
        road_map_menu.load.name_for_loading, road_map_menu.new.name_for_loading = '', ''


def events():
    for event in pg.event.get():

        if event.type == pg.QUIT:
            save_log_and_exit(DATETIME_INIT_APP)

        if road_map_menu.class_road_map_menu:
            road_map_menu.events(event)

        elif road_map_game.class_road_map_game:
            road_map_game.events(event)


def update():
    FRAMES.tick(road_map_menu.options.MAX_FRAMES)
    draw()
    events()
    pg.display.update()


if __name__ == '__main__':
    while True:
        update()
