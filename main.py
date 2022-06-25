from settings import *
from roadmap import RoadMapMenu

road_map_menu = RoadMapMenu()


def draw():
    road_map_menu.draw(MAIN_SCREEN)


def events():
    for event in pg.event.get():

        if event.type == pg.QUIT:
            save_log()

        road_map_menu.events(event)


def update():
    FRAMES.tick(road_map_menu.options.MAX_FRAMES)
    draw()
    events()
    pg.display.update()


if __name__ == '__main__':
    while True:
        update()
