
LIST_CLASSES = [
    ['duelist', 'mage', 'assassin'],
    ['warrior', 'mage', 'warden']
]
BASIC_ATTRIBUTES = ['Force', 'Agility', 'Vitality', 'Intelligence', 'Resistance']

DARK_ELF = {
    'duelist': [3, 4, 4, 2, 3],
    'mage': [2, 3, 4, 5, 2],
    'assassin': [3, 5, 4, 2, 2]
}
GREY_ELF = {
    'warrior': [5, 2, 5, 2, 2],
    'mage': [2, 2, 5, 5, 2],
    'warden': [2, 2, 4, 2, 6]
}
FOREST_ELF = {
    'warrior': [3, 4, 4, 2, 3],
    'mage': [2, 2, 5, 5, 2],
    'warden': [2, 4, 4, 2, 4]
}
CLASS_PROGRESSION_MELEE = [2, 1, 1, 1, 1]
CLASS_PROGRESSION_MAGE = [1, 1, 1, 2, 1]

SKILLS = {
    'd_duelist': ['Duelism', 'Combat with Two Weapons'],
    'd_mage': ['Conjuration', 'Arcana Recovery'],
    'd_assassin': ['Supernatural Dodge', 'Lucky Strike'],

    'f_warrior': ['Wild Combat Form', 'Wild Form of Elemental'],
    'f_mage': ['Circle Spells', 'Natural Recovery'],
    'f_warden': ['Dodge Fortification', 'Hybrid Defense'],

    'g_warrior': ['Get You Breath Back', 'Combat with Big Weapons'],
    'g_mage': ['Overlord', 'Arcana Recovery'],
    'g_warden': ['Fortification', 'Defense Specialist'],
}




"""
CONTEXT INFO
"""
txt_options = {
    'title': 'OPTIONS',
    'caption': ['Screen', 'Fps', 'Sound'],
    'screen': ['Full screen', 'Default'],
    'fps': ['30 fps', '60 fps'],
    'sound': ['on', 'off']
}
list_ethnicities = ['Dark Elves', 'Forest Elves', 'Grey Elves']
list_guides_menu = ['new_game  ', ' load', 'credits', 'options', ' quit']
title_load = 'Records'
title_new_game = 'Ethnicities', 'Classes'

INFO_MAX_RECORDS = \
    """RECORD SPACES 9/9|
    RETURN TO MENU|
    RELEASE ONE OR MORE SPACES|
    TO CREATE NEW RECORDS..."""


def read(name, file):
    read = open(f'static/context_info/{name}/{file}.txt', mode='r+', encoding='utf-8')
    read = '\r'.join(read.readlines())
    return read

INFO_HERALDRY = {
    'dark': read('dark', 'heraldry'),
    'forest': read('forest', 'heraldry'),
    'grey': read('grey', 'heraldry'), 
    }

INFO_SKILLS = {
    'd_duelist': read('dark', 'duelist'),
    'd_mage': read('dark', 'mage'),
    'd_assassin': read('dark', 'assassin'),

    'f_warrior': read('forest', 'warrior'),
    'f_mage': read('forest', 'mage'),
    'f_warden': read('forest', 'warden'),

    'g_warrior': read('grey', 'warrior'),
    'g_mage': read('grey', 'mage'),
    'g_warden':read('grey', 'warden')
}



"""
AREA MAPS SETTINGS
"""
LIST_LANDS = [
    'Corrupted Island', 'Island of Beasts', 'Sea North', 'Fields of Slimes', 'River of Vipers', 'Whispering Forest',
    'Foggy Passage', 'Mines of Noria', 'West Road', 'Wind Fields', 'Noria City', 'Lands of Noria',
    'Domain of Golems', 'Field of Dragons', 'Sea Dragon', 'Desolate Road', 'Draconian Domain', 'Mystical Disorder',
    'City Ghabul', 'Dragon City', 'Draconian Harbor', 'Isle of Elders', 'Forest of Wild Elves', "No Man's lands",
    'Desert of the Dead', "Hell's Gate", 'Dragons Mountains', 'Ymir City', 'Lizardmans Area', 'Cursed Tower',
    'Goblin Horde', 'Orc Horde', 'Grey Elves Mountains', 'Gnomes Hideout', 'Storm Wind Valley', 'Fomorian Invasion',
    'Aretuza City', 'North Road', 'Forest of the Druids', 'Mages Guild', 'Dark Elves Tunnels', 'Mythical Zone',
    'North Sea', 'Witches Guild', 'Aesir', 'Shadow Guild', 'Warriors Guild', 'Rose Cross Guild',
    'Noldor', 'Three Crowns'
]

ID_AREA = [
    'corrupted', 'beasts', 'slimes', 'vipers', 'whisper',
    'passage', 'mines', 'road', 'wind', 'city', 'lands',
    'golems', 'dragons', 'sea', 'draconian', 'mystical',
    'elders', 'wild elves', 'dead', 'hell', 'lizardman',
    'cursed', 'goblin', 'orc', 'grey elves', 'gnomes',
    'fomorian', 'druids', 'mages', 'dark elves', 'mythical',
    'witches', 'aesir', 'shadow', 'warriors', 'rose', 'noldor',
    'three'
    ]

POS_GPS = [
    (449, 198), (468, 183), (511, 184), (494, 200), (509, 214), (524, 205),
    (528, 216), (512, 224), (502, 233), (509, 249), (514, 264), (504, 276),
    (488, 262), (466, 257), (457, 273), (470, 288), (477, 308), (459, 319),
    (460, 337), (490, 324), (530, 319), (573, 336), (608, 359), (639, 346),
    (659, 327), (661, 308), (635, 305), (612, 316), (592, 301), (614, 282),
    (635, 268), (664, 259), (685, 238), (668, 226), (649, 238), (628, 245),
    (614, 245), (626, 224), (646, 201), (628, 201), (620, 180), (609, 194),
    (600, 209), (586, 201), (592, 176), (572, 180), (559, 197), (535, 193),
    (539, 207), (553, 220)
]



"""
PATHS
"""
FOLDER = {
    'save': 'save/',
    'menu': 'static/images/menu/',
    'new_game': 'static/images/menu/newgame/',
    'load': 'static/images/menu/load/',
    'options': 'static/images/menu/options/',
    'classes': 'static/images/classes/',
    'sound': 'static/sound/',
    'soundtrack': 'static/soundtrack/',
    'game': 'static/images/game/',
    'enemies': 'static/images/enemies/'
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