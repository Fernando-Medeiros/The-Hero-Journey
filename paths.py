import pygame as pg

pg.init(), pg.font.init(), pg.mixer.init()

LANGUAGE = 'EN'  # --- > EN or BR

URL_CREDIT = 'https://github.com/Fernando-Medeiros'

list_class = [
    ['duelist', 'mage', 'assassin'],
    ['warrior', 'mage', 'warden']
]

if LANGUAGE == 'EN':
    NAME_OF_THE_GAME = "The Hero's Journey"
    txt_options = {
        'title': 'OPTIONS',
        'caption': ['Screen', 'Fps', 'Sound'],
        'screen': ['Full screen', 'Default'],
        'fps': ['30 fps', '60 fps'],
        'sound': ['on', 'off']
    }
else:
    NAME_OF_THE_GAME = "A Jornada do Herói"
    txt_options = {
        'title': 'OPÇÕES',
        'caption': ['Tela', 'Fps', 'Som'],
        'screen': ['Tela Cheia', 'Padrão'],
        'fps': ['30 fps', '60 fps'],
        'sound': ['Ligado', 'Desligado']
    }

DARK_ELF = {
    'duelist': [3, 2, 2, 1, 1],
    'mage': [1, 1, 2, 4, 1],
    'assassin': [2, 4, 1, 1, 1]
}

GREY_ELF = {
    'warrior': [3, 1, 3, 1, 1],
    'mage': [1, 1, 3, 2, 2],
    'warden': [1, 1, 3, 1, 3]
}

FOREST_ELF = {
    'warrior': [2, 2, 2, 1, 2],
    'mage': [1, 1, 4, 2, 1],
    'warden': [1, 2, 2, 1, 3]
}
class_progression_melee, class_progression_mage = [1, 1, 1, 1, 1], [1, 1, 1, 1, 1]

SKILLS = {
    'd_duelist': {'EN': ['Duelism', 'Combat with Two Weapons'],
                  'BR': ['Duelismo', 'Combate com Duas Armas']},

    'd_mage': {'EN': ['Conjuration', 'Arcana Recovery'],
               'BR': ['Conjuração', 'Recuperação Arcana']},

    'd_assassin': {'EN': ['Supernatural Dodge', 'Lucky Strike'],
                   'BR': ['Esquiva Sobrenatural', 'Golpe de Sorte']},

    'f_warrior': {'EN': ['Wild Combat Form', 'Wild Form of Elemental'],
                  'BR': ['Forma Selvagem de Combate', 'Forma Selvagem de Elemental']},

    'f_mage': {'EN': ['Circle Spells', 'Natural Recovery'],
               'BR': ['Magias de Circulo', 'Recuperação Natural']},

    'f_warden': {'EN': ['Dodge Fortification', 'Hybrid Defense'],
                 'BR': ['Fortificação de Esquiva', 'Defesa Hibrida']},

    'g_warrior': {'EN': ['Get You Breath Back', 'Combat with Big Weapons'],
                  'BR': ['Retomar Fôlego', 'Combate com Armas Grandes']},

    'g_mage': {'EN': ['Overlord', 'Arcana Recovery'],
               'BR': ['Sobrecarga', 'Recuperação Arcana']},

    'g_warden': {'EN': ['Fortification', 'Defense Specialist'],
                 'BR': ['Fortificação', 'Especialista em Defesa']}
}

FOLDER = {
    'save': 'save/',
    'menu': 'assets/images/' + LANGUAGE + '/menu/',
    'new_game': 'assets/images/' + LANGUAGE + '/menu/newgame/',
    'load': 'assets/images/' + LANGUAGE + '/menu/load/',
    'options': 'assets/images/' + LANGUAGE + '/menu/options/',
    'classes': 'assets/images/' + LANGUAGE + '/classes/',
    'sound': 'assets/sound/',
    'soundtrack': 'assets/soundtrack/',
    'game': 'assets/images/' + LANGUAGE + '/game/'

}

COLORS = {
    'WHITE': (255, 255, 255),
    'BLACK': (0, 0, 0),
    'RED': (176, 31, 31),
    'GREEN': (29, 161, 85),
    'BLUE': (67, 138, 167),
    'YELLOW': (235, 197, 70),
    'ACTIVE': 0
}

GROUPS = {
    'menu': pg.sprite.Group(),
    'new': pg.sprite.Group(),
    'load': pg.sprite.Group(),
    'options': pg.sprite.Group(),
    'char': pg.sprite.Group(),
    'opponent': pg.sprite.Group(),
    'game': pg.sprite.Group()
}

IMG_MENU = {
    'bg': FOLDER['menu'] + 'bg_menu.png',
    'new': FOLDER['menu'] + 'new_game.png',
    'load': FOLDER['menu'] + 'load.png',
    'credit': FOLDER['menu'] + 'credit.png',
    'options': FOLDER['menu'] + 'options.png',
    'quit': FOLDER['menu'] + 'quit.png',
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
    'dark_elf': FOLDER['new_game'] + 'dark_elf.png',
    'grey_elf': FOLDER['new_game'] + 'grey_elf.png',
    'forest_elf': FOLDER['new_game'] + 'forest_elf.png',

    'HERALDRY_BOX': FOLDER['new_game'] + 'heraldry_box.png',
    'info_dark': FOLDER['new_game'] + 'INFO_DARK_ELF.png',
    'info_grey': FOLDER['new_game'] + 'INFO_GREY_ELF.png',
    'info_forest': FOLDER['new_game'] + 'INFO_FOREST_ELF.png',

    'duelist': FOLDER['new_game'] + 'class_duelist.png',
    'mage': FOLDER['new_game'] + 'class_mage.png',
    'assassin': FOLDER['new_game'] + 'class_assassin.png',
    'warrior': FOLDER['new_game'] + 'class_warrior.png',
    'warden': FOLDER['new_game'] + 'class_warden.png',

    'BOX_STATUS': FOLDER['new_game'] + 'box_status.png',
    'info_ed_duelist': FOLDER['new_game'] + 'status_ed_duelist.png',
    'info_ed_mage': FOLDER['new_game'] + 'status_ed_mage.png',
    'info_ed_assassin': FOLDER['new_game'] + 'status_ed_assassin.png',
    'info_ef_warrior': FOLDER['new_game'] + 'status_ef_warrior.png',
    'info_ef_warden': FOLDER['new_game'] + 'status_ef_warden.png',
    'info_ef_mage': FOLDER['new_game'] + 'status_ef_mage.png',
    'info_eg_warrior': FOLDER['new_game'] + 'status_eg_warrior.png',
    'info_eg_mage': FOLDER['new_game'] + 'status_eg_mage.png',
    'info_eg_warden': FOLDER['new_game'] + 'status_eg_warden.png',

    'max_records': FOLDER['new_game'] + 'max_records.png'
}

IMG_LOAD = {
    'bg': FOLDER['load'] + 'bg.png',
    'box': FOLDER['load'] + 'box.png',
    'del': FOLDER['load'] + 'del.png',
    'select_add': FOLDER['load'] + 'add_active.png',
    'select_del': FOLDER['load'] + 'del_active.png'
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
    'proficiency': FOLDER['game'] + 'proficiency.png'
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

SOUNDS = {
    'click': pg.mixer.Sound(FOLDER['sound'] + 'click.mp3')
}

SONGS = {
    'orpheus': pg.mixer.Sound(FOLDER['soundtrack'] + 'orpheus.mp3')
}
