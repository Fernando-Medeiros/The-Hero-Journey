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

FOLDER = {
    'save': 'save/',
    'menu': 'images/' + LANGUAGE + '/menu/',
    'new_game': 'images/' + LANGUAGE + '/menu/newgame/',
    'load': 'images/' + LANGUAGE + '/menu/load/',
    'options': 'images/' + LANGUAGE + '/menu/options/',
    'classes': 'images/' + LANGUAGE + '/classes/',
    'sound': 'sound/',
    'soundtrack': 'soundtrack/',

}

COLORS = {
    'WHITE': (255, 255, 255),
    'BLACK': (0, 0, 0),
    'RED': (255, 0, 0),
    'ACTIVE': 0
}

GROUPS = {
    'menu': pg.sprite.Group(),
    'new': pg.sprite.Group(),
    'load': pg.sprite.Group(),
    'options': pg.sprite.Group()
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
