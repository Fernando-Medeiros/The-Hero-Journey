import os

STATIC = os.environ['STATIC']

"""
PATHS
"""
FOLDER = {
    'save': 'save/',
    'menu': STATIC + 'images/menu/',
    'new_game': STATIC + 'images/menu/newgame/',
    'load': STATIC + 'images/menu/load/',
    'options': STATIC + 'images/menu/options/',
    'classes': STATIC + 'images/classes/',
    'sound': STATIC + 'sound/',
    'soundtrack': STATIC + 'soundtrack/',
    'game': STATIC + 'images/game/',
    'enemies': STATIC + 'images/enemies/',
}

IMG_MENU = {
    'bg': FOLDER['menu'] + 'bg_menu.png',
    'return': FOLDER['menu'] + 'return.png',
    'select': FOLDER['menu'] + 'select.png',
    'info_c': FOLDER['menu'] + 'info_credit.png',
    'select_return': FOLDER['menu'] + 'select_return.png'
}

IMG_NEW_GAME = {
    'bg': FOLDER['new_game'] + 'bg_new_game.png',
    'add': FOLDER['new_game'] + 'add.png',
    'interactive': FOLDER['new_game'] + 'interactive.png',
    'select': FOLDER['new_game'] + 'select.png',

    'HERALDRY_BOX': FOLDER['new_game'] + 'heraldry_box.png',
    'info_dark': FOLDER['new_game'] + 'INFO_DARK_ELF.png',
    'info_grey': FOLDER['new_game'] + 'INFO_GREY_ELF.png',
    'info_forest': FOLDER['new_game'] + 'INFO_FOREST_ELF.png',

    'BOX_STATUS': FOLDER['new_game'] + 'box_status.png',
    'max_records': FOLDER['new_game'] + 'max_records.png'
}

IMG_LOAD = {
    'bg': FOLDER['load'] + 'bg.png',
    'box': FOLDER['load'] + 'box.png',
    'del': FOLDER['load'] + 'del.png',
    'add': FOLDER['load'] + 'add.png',
    'select_add': FOLDER['load'] + 'select_add.png',
    'select_del': FOLDER['load'] + 'select_del.png'
}

IMG_OPTIONS = {
    'bg': FOLDER['options'] + 'bg.png',
    'inactive': FOLDER['options'] + 'inactive.png',
    'active': FOLDER['options'] + 'active.png'
}

IMG_GAME = {
    'bg': FOLDER['game'] + 'bg.png',
    'bg_char': FOLDER['game'] + 'bg_char.png',
    'map': FOLDER['game'] + 'map.png',
    'gps': FOLDER['game'] + 'gps.png',
    'gold': FOLDER['game'] + 'gold.png',
    'soul': FOLDER['game'] + 'soul.png',

    'marketplace': FOLDER['game'] + 'marketplace.png',
    'options': FOLDER['game'] + 'options.png',
    'save': FOLDER['game'] + 'save.png',
    'skills': FOLDER['game'] + 'skills.png',
    'proficiency': FOLDER['game'] + 'proficiency.png',
    'chest': FOLDER['game'] + 'chest.png',
    'next': FOLDER['game'] + 'next.png',
    'previous': FOLDER['game'] + 'previous.png',

    'select_save': FOLDER['game'] + 'select_save.png',
    'select_marketplace': FOLDER['game'] + 'select_marketplace.png',
    'select_options': FOLDER['game'] + 'select_options.png',
    'select_skills': FOLDER['game'] + 'select_skills.png',
    'select_proficiency': FOLDER['game'] + 'select_proficiency.png',
    'select_chest': FOLDER['game'] + 'select_chest.png',
    'select_next': FOLDER['game'] + 'select_next.png',
    'select_previous': FOLDER['game'] + 'select_previous.png',

    'b_attack': FOLDER['game'] + 'b_attack.png',
    'b_defense': FOLDER['game'] + 'b_defense.png',
    'b_flee': FOLDER['game'] + 'b_flee.png',
    'b_skills': FOLDER['game'] + 'b_skills.png',
    'b_items': FOLDER['game'] + 'b_items.png',

    'select_b_attack': FOLDER['game'] + 'select_b_attack.png',
    'select_b_defense': FOLDER['game'] + 'select_b_defense.png',
    'select_b_flee': FOLDER['game'] + 'select_b_flee.png',
    'select_b_skills': FOLDER['game'] + 'select_b_skills.png',
    'select_b_items': FOLDER['game'] + 'select_b_items.png'
}

IMG_CLASSES = {
    'ed_duelist': FOLDER['classes'] + 'ed_duelist.png',
    'ed_mage': FOLDER['classes'] + 'ed_mage.png',
    'ed_assassin': FOLDER['classes'] + 'ed_assassin.png',
    'ef_warrior': FOLDER['classes'] + 'ef_warrior.png',
    'ef_mage': FOLDER['classes'] + 'ef_mage.png',
    'ef_warden': FOLDER['classes'] + 'ef_warden.png',
    'eg_warrior': FOLDER['classes'] + 'eg_warrior.png',
    'eg_mage': FOLDER['classes'] + 'eg_mage.png',
    'eg_warden': FOLDER['classes'] + 'eg_warden.png'
}