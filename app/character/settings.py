LIST_CLASSES = [
    ['duelist', 'mage', 'assassin'],
    ['warrior', 'mage', 'warden']
]

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

BASIC_ATTRIBUTES = [
    'force',
    'agility',
    'vitality',
    'intelligence',
    'resistance'
    ]

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


# INFO
def read(name, file):
    with open(f'static/context_info/{name}/{file}.txt', mode='r+', encoding='utf-8') as file:
        return '\r'.join(file.readlines())

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