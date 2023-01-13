import os

STATIC: str = os.getenv("STATIC", "static/")

FOLDERS = {
    "menu": STATIC + "images/menu/",
    "new_game": STATIC + "images/menu/newgame/",
    "load": STATIC + "images/menu/load/",
    "options": STATIC + "images/menu/options/",
    "classes": STATIC + "images/classes/",
    "sound": STATIC + "sound/",
    "soundtrack": STATIC + "soundtrack/",
    "game": STATIC + "images/game/",
    "enemies": STATIC + "images/enemies/",
}

IMG_MENU = {
    "bg": FOLDERS["menu"] + "bg_menu.png",
    "return": FOLDERS["menu"] + "return.png",
    "select": FOLDERS["menu"] + "select.png",
    "info_c": FOLDERS["menu"] + "info_credit.png",
    "select_return": FOLDERS["menu"] + "select_return.png",
}

IMG_NEW_GAME = {
    "bg": FOLDERS["new_game"] + "bg_new_game.png",
    "add": FOLDERS["new_game"] + "add.png",
    "interactive": FOLDERS["new_game"] + "interactive.png",
    "select": FOLDERS["new_game"] + "select.png",
    "HERALDRY_BOX": FOLDERS["new_game"] + "heraldry_box.png",
    "info_dark": FOLDERS["new_game"] + "INFO_DARK_ELF.png",
    "info_grey": FOLDERS["new_game"] + "INFO_GREY_ELF.png",
    "info_forest": FOLDERS["new_game"] + "INFO_FOREST_ELF.png",
    "BOX_STATUS": FOLDERS["new_game"] + "box_status.png",
    "max_records": FOLDERS["new_game"] + "max_records.png",
}

IMG_LOAD = {
    "bg": FOLDERS["load"] + "bg.png",
    "box": FOLDERS["load"] + "box.png",
    "del": FOLDERS["load"] + "del.png",
    "add": FOLDERS["load"] + "add.png",
    "select_add": FOLDERS["load"] + "select_add.png",
    "select_del": FOLDERS["load"] + "select_del.png",
}

IMG_OPTIONS = {
    "bg": FOLDERS["options"] + "bg.png",
    "inactive": FOLDERS["options"] + "inactive.png",
    "active": FOLDERS["options"] + "active.png",
}

IMG_GAME = {
    "bg": FOLDERS["game"] + "bg.png",
    "bg_char": FOLDERS["game"] + "bg_char.png",
    "map": FOLDERS["game"] + "map.png",
    "gps": FOLDERS["game"] + "gps.png",
    "gold": FOLDERS["game"] + "gold.png",
    "soul": FOLDERS["game"] + "soul.png",
    "marketplace": FOLDERS["game"] + "marketplace.png",
    "options": FOLDERS["game"] + "options.png",
    "save": FOLDERS["game"] + "save.png",
    "skills": FOLDERS["game"] + "skills.png",
    "proficiency": FOLDERS["game"] + "proficiency.png",
    "chest": FOLDERS["game"] + "chest.png",
    "next": FOLDERS["game"] + "next.png",
    "previous": FOLDERS["game"] + "previous.png",
    "select_save": FOLDERS["game"] + "select_save.png",
    "select_marketplace": FOLDERS["game"] + "select_marketplace.png",
    "select_options": FOLDERS["game"] + "select_options.png",
    "select_skills": FOLDERS["game"] + "select_skills.png",
    "select_proficiency": FOLDERS["game"] + "select_proficiency.png",
    "select_chest": FOLDERS["game"] + "select_chest.png",
    "select_next": FOLDERS["game"] + "select_next.png",
    "select_previous": FOLDERS["game"] + "select_previous.png",
    "b_attack": FOLDERS["game"] + "b_attack.png",
    "b_defense": FOLDERS["game"] + "b_defense.png",
    "b_flee": FOLDERS["game"] + "b_flee.png",
    "b_skills": FOLDERS["game"] + "b_skills.png",
    "b_items": FOLDERS["game"] + "b_items.png",
    "select_b_attack": FOLDERS["game"] + "select_b_attack.png",
    "select_b_defense": FOLDERS["game"] + "select_b_defense.png",
    "select_b_flee": FOLDERS["game"] + "select_b_flee.png",
    "select_b_skills": FOLDERS["game"] + "select_b_skills.png",
    "select_b_items": FOLDERS["game"] + "select_b_items.png",
}
