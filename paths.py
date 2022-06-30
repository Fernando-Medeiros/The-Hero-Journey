import pygame as pg

pg.init(), pg.font.init(), pg.mixer.init()

LANGUAGE = 'EN'  # --- > EN or BR

URL_CREDIT = 'https://github.com/Fernando-Medeiros'

LIST_CLASSES = [
    ['duelist', 'mage', 'assassin'],
    ['warrior', 'mage', 'warden']
]

BASIC_ATTRIBUTES = ['Force', 'Agility', 'Vitality', 'Intelligence', 'Resistance']

if LANGUAGE == 'EN':
    NAME_OF_THE_GAME = "The Hero's Journey"
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
    LIST_LANDS = [
        'Strange Island', 'Island of Wolves', 'Marine Point', 'Fields of Slimes', 'River of Vipers', 'Forest of Elves',
        'Dark Passage', 'Mines of Noria', 'Two Rivers', 'Wind Fields', 'Noria City', 'Lands of Noria'
    ]

else:
    NAME_OF_THE_GAME = "A Jornada do Herói"
    txt_options = {
        'title': 'OPÇÕES',
        'caption': ['Tela', 'Fps', 'Som'],
        'screen': ['Tela Cheia', 'Padrão'],
        'fps': ['30 fps', '60 fps'],
        'sound': ['Ligado', 'Desligado']
    }
    list_ethnicities = ['Elfos Escuros', 'Elfos das Florestas', 'Elfos Cinzentos']
    list_guides_menu = ['novo_jogo', 'carregar', 'créditos', 'opções', 'sair']
    title_load = 'Registros'
    title_new_game = 'Etnias', 'Classes'
    LIST_LANDS = [
        'Ilha Estranha', 'Ilha dos Lobos', 'Ponto Marinho', 'Campos de Slimes', 'Rio das Víboras', 'Floresta dos Elfos',
        'Passagem Negra', 'Minas de Noria', 'Dois Rios', 'Campos de Vento', 'Cidade de Noria', 'Terras de Noria'
    ]

POS_GPS = [
    (449, 198), (468, 183), (511, 184), (494, 200), (509, 214), (524, 205),
    (528, 216), (512, 224), (502, 233), (509, 249), (514, 264), (504, 276)
]

DARK_ELF = {
    'duelist': [2, 3, 3, 1, 2],
    'mage': [1, 2, 3, 4, 1],
    'assassin': [2, 4, 3, 1, 1]
}

GREY_ELF = {
    'warrior': [4, 1, 4, 1, 1],
    'mage': [1, 1, 4, 4, 1],
    'warden': [1, 1, 3, 1, 5]
}

FOREST_ELF = {
    'warrior': [2, 3, 3, 1, 2],
    'mage': [1, 1, 4, 4, 1],
    'warden': [1, 3, 3, 1, 3]
}

CLASS_PROGRESSION_MELEE, CLASS_PROGRESSION_MAGE = [1, 1, 1.5, 1, 1], [1, 1, 1, 1.5, 1]

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

LIST_ENEMIES = []
with open('assets/list_enemies.txt', mode='r', encoding='utf-8') as file:
    for x in file.readlines():
        LIST_ENEMIES.append(x.replace("\n", "").split(':'))

FOLDER = {
    'save': 'save/',
    'menu': 'assets/images/menu/',
    'new_game': 'assets/images/menu/newgame/',
    'load': 'assets/images/menu/load/',
    'options': 'assets/images/menu/options/',
    'classes': 'assets/images/classes/',
    'sound': 'assets/sound/',
    'soundtrack': 'assets/soundtrack/',
    'game': 'assets/images/game/',
    'enemies': 'assets/images/enemies/'

}

COLORS = {
    'WHITE': (255, 255, 255),
    'BLACK': (0, 0, 0),
    'RED': (176, 31, 31),
    'GREEN': (29, 161, 85),
    'BLUE': (67, 138, 167),
    'YELLOW': (235, 197, 70),
    'BLUE_2': (6, 0, 56),
    'ACTIVE': 0
}

GROUPS = {
    'menu': pg.sprite.Group(),
    'new': pg.sprite.Group(),
    'load': pg.sprite.Group(),
    'options': pg.sprite.Group(),
    'opponent': pg.sprite.Group(),
    'game': pg.sprite.Group()
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
    'select_previous': FOLDER['game'] + 'select_previous.png'
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

INFO_HERALDRY = {
    'dark':
        {
            'EN':
    """
        Physically, dark elves are similar to surface elves. However,\r
    their skin is as black as ebony, and their hair is white or silver.\r 
    Unlike other elves, who maintain a relationship of respect,\r
    and harmony with the forests and woods where they live,\r
    dark elves maintain a relationship of domination with everything around them.\r
    Even the caves and tunnels that form their cities are subjugated,\r
    shaped and distorted to suit their designs.\r
    Dark elves are skilled artisans, and their stone and metalworking is famous even on the surface.\r
    Traditionally, dark elves are selfish and evil,\r
    and their entire culture and society is built around the concept of power at all costs.\r
    Dark elf citadels are treacherous places, where the rich and powerful play a dangerous game of power,\r
    in which those of lower caste are mere pawns, completely expendable.\r
    Dark elves have a great appreciation for magic of any kind,\r
    and spell casters tend to occupy a prominent place in their communities.""",

            'BR':
                """
        Fisicamente, os elfos negros são semelhantes aos elfos da superfície.\r
    No entanto, sua pele é preta como ébano e seus cabelos são brancos ou prateados.\r
    Ao contrário de outros elfos, que mantêm uma relação de respeito,\r
    e harmonia com as florestas e matas onde vivem,\r
    os elfos negros mantêm uma relação de dominação com tudo ao seu redor.\r
    Até as cavernas e túneis que formam suas cidades são subjugados,\r
    moldados e distorcidos para se adequarem aos seus projetos.\r
    Elfos negros são artesãos habilidosos,\r
    e seu trabalho com pedras e metais é famoso mesmo na superfície.\r
    Tradicionalmente, os elfos negros são egoístas e maus,\r
    e toda a sua cultura e sociedade são construídas em torno do conceito de poder a todo custo.\r
    As cidadelas dos elfos negros são lugares traiçoeiros,\r
    onde os ricos e poderosos jogam um perigoso jogo de poder,\r
    no qual os de casta inferior são meros peões, completamente dispensáveis.\r
    Elfos negros apreciam muito a magia de qualquer tipo,\r
    e os conjuradores tendem a ocupar um lugar de destaque em suas comunidades."""
        },

    'forest':
        {
            'EN':
                """
        The most reclusive of all surface elves are those who still guard the forests.\r
    They are similar in appearance to gray elves or high elves,\r
    but their robes define their tribal and savage origins.\r
    They have great skills in the forests, where they prefer to stay most of the time.\r
    Unlike gray elves (who build their cities highly ranked)\r
    or high elves (who prefer communities of other races),\r
    wood elves prefer to live in nomadic and wild groups, defending their territory.""",

            'BR':
                """
        Os mais reclusos de todos os elfos da superfície são aqueles que ainda guardam as florestas.\r
    Eles são semelhantes em aparência aos elfos cinzentos ou altos elfos,\r
    mas suas vestes definem suas origens tribais e selvagens.\r
    Eles têm grandes habilidades nas florestas, onde preferem ficar a maior parte do tempo.\r
    Ao contrário dos elfos cinzentos (que constroem suas cidades de alto nível)\r
    ou elfos altos (que preferem comunidades de outras raças),\r
    os elfos da floresta preferem viver em grupos nômades e selvagens, defendendo seu território."""
        },

    'grey':
        {
            'EN':
                """
        The Gray Elves are among the most noble and reclusive among elven society,\r
    they are an offshoot of the original high elves' lineage.\r
    They walked away from the world after leaving their mark, which was to ensure that the world\r
    was in the way of the gods. The Gray Elves see themselves as protectors of the good in the world,\r
    but they will only descend from their mountains and meadows to protect some "lesser" race,\r
    if it is facing great evil.\r
    Gray Elves are arrogant and condescending, full of self-importance.\r
    They never speak their minds, as long as it maintains the nobility of the elves.\r
    They avoid contact with other races, including other elves. \r
    They are not exactly intolerant of other races,\r
    but they do believe in the purity of the elven lineage. \r
    Only powerful mages are allowed into their mountain citadels,\r
    and even then they are met with great suspicion.\r
    Taller and thinner than other elves, Gray Elves have dark hair and eyes, some of which are rare.\r
    may have very light golden hair, and purple eyes. These elves are often confused\r
    with fairies and were probably the first to have contact with humans.""",

            'BR':
                """
        Os Elfos Cinzentos estão entre os mais nobres e reclusos da sociedade élfica,\r
    eles são um desdobramento da linhagem original dos altos elfos.\r
    Eles se afastaram do mundo depois de deixar sua marca, que era garantir que o mundo\r
    estava no caminho dos deuses. Os Elfos Cinzentos se vêem como protetores do bem no mundo,\r
    mas eles só descerão de suas montanhas e prados para proteger alguma raça "menor",\r
    se estiver enfrentando um grande mal.\r
    Elfos Cinzentos são arrogantes e condescendentes, cheios de auto-importância.\r
    Nunca falam o que pensam, desde que mantenha a nobreza dos elfos.\r
    Evitam o contato com outras raças, incluindo outros elfos.\r
    Eles não são exatamente intolerantes com outras raças, mas acreditam na pureza da linhagem élfica.\r
    Apenas magos poderosos são permitidos em suas cidadelas nas montanhas,\r
    e mesmo assim eles são recebidos com grande suspeita.\r
    Mais altos e mais magros do que outros elfos, os Elfos Cinzentos têm cabelos e olhos escuros,\r
    alguns dos quais são raros.\r
    pode ter cabelos dourados muito claros e olhos roxos. \r
    Esses elfos são muitas vezes confusos\r
    com fadas e provavelmente foram os primeiros a ter contato com humanos."""}
}

INFO_SKILLS = {
    'd_duelist':
    {
        'EN':
        """
    DUELISM\r
    When you wield a melee weapon in one hand,\r
    and no other weapons,\r
    you gain 25% bonus damage with that weapon.\r
    \r
    COMBAT WITH TWO WEAPONS\r
    When you are engaged in a two-weapon fight,\r
    you may occasionally land a second blow.""",

        'BR':
        """
    DUELISMO\r
    Quando você empunha uma arma corpo a corpo\r
    em apenas uma mão,\r
    você ganha 25% de dano adicional.\r
    \r
    COMBATE COM DUAS ARMAS\r
    Quando você está envolvido\r
    em uma luta com duas armas,\r
    ocasionalmente você pode\r
    acertar um segundo golpe."""
        },

    'd_mage':
        {
            'EN':
                """
    CONJURATION\r
    As a student of arcane magic,\r
    you possess a spellbook (or grimoire),\r
    that reveals the first glimpses\r
    of your true power.\r
    (receives a fixed element)\r
    \r
    ARCANA RECOVERY\r
    You learned how to recover some of your\r
    magical energy by studying your spellbook.\r
    (mana regeneration)""",

            'BR':
                """
    CONJURAÇÃO\r
    Como estudante de magia arcana,\r
    você possui um livro de feitiços (ou grimório),\r
    que revela os primeiros vislumbres\r
    de seu verdadeiro poder.\r
    (recebe um elemento fixo)\r
    \r
    RECUPERAÇÃO ARCANA\r
    Você aprendeu a recuperar um pouco\r
    de sua energia mágica estudando seu grimório.\r
    (regeneração de mana)"""
        },

    'd_assassin':
        {
            'EN':
                """
    SUPERNATURAL DODGE\r
    When an enemy you can see hits you\r
    with an attack,\r
    you can use your reaction to halve\r
    the damage taken.\r
    \r
    LUCKY STRIKE\r
    If one of your attacks fails,\r
    you can turn that failure into a hit,\r
    and get a second chance. (critical damage)""",

            'BR':
                """
    ESQUIVA SOBRENATURAL\r
    Quando um inimigo que você pode ver\r
    o atinge com um ataque,\r
    você pode usar sua reação para\r
    reduzir pela metade o dano recebido.\r
    \r
    GOLPE DE SORTE\r
    Se um de seus ataques falhar,\r
    você pode transformar essa falha em um acerto,\r
    e obter uma segunda chance. (dano crítico)"""
        },

    'f_warrior':
        {
            'EN':
                """
    WILD COMBAT FORM \r
    You assume a savage form adding a\r
    3% damage bonus for each free gear slot.\r
    \r
    WILD FORM OF ELEMENTAL\r
    Occasionally you summon an elemental form\r
    of pure essence to aid in the attack.\r
    The elemental's strength varies according\r
    to its level.""",

            'BR':
                """
    FORMA DE COMBATE SELVAGEM\r
    Você assume uma forma selvagem adicionando\r
    bônus de dano de 3%\r
    para cada slot de equipamento livre.\r
    \r
    FORMA SELVAGEM DO ELEMENTAL\r
    Ocasionalmente você invoca uma forma elemental\r
    de pura essência para ajudar no ataque.\r
    A força do elemental varia de acordo com seu nível."""
        },

    'f_mage':
        {
            'EN':
                """
    CIRCLE SPELLS\r
    Your mystical connection to the land infuses\r
    you with the ability to cast certain spells.\r
    random bonus depending on the terrain.\r
    \r
    NATURAL RECOVERY\r
    You can recover some of your magical energy\r
    by stopping to meditate and commune with nature.\r
    (hp and mp regeneration)""",

            'BR':
                """
    FEITIÇOS DE CÍRCULO\r
    Sua conexão mística com a terra o infunde\r
    com a habilidade de lançar certos feitiços.\r
    bônus aleatório dependendo do terreno.\r
    \r
    RECUPERAÇÃO NATURAL\r
    Você pode recuperar um pouco de sua energia\r
    mágica parando para meditar e comungar com a natureza.\r
    (regeneração de hp e mp)"""
        },

    'f_warden':
        {
            'EN':
                """
    DODGE FORTIFICATION\r
    Warden are experts in defense,\r
    and know how to maximize the\r
    potential of their armor,\r
    you receive a 5% bonus for each\r
    medium armor piece of equipment.\r
    \r
    HYBRID DEFENSE\r
    When using two weapons or two-handed weapons\r
    you add a 15% bonus to your total dodge attack.""",

            'BR':
                """
    ESQUIVA DE FORTIFICAÇÃO\r
    Os Guardiões são especialistas em defesa,\r
    e sabem como maximizar o potencial de suas armaduras,\r
    você recebe um bônus de 5%\r
    para cada equipamento de armadura média.\r
    \r
    DEFESA HÍBRIDA\r
    Ao usar duas armas ou armas de duas mãos,\r
    você adiciona um bônus de 15% ao seu ataque\r
    de esquiva total."""
        },

    'g_warrior':
        {
            'EN':
                """
    GET YOUR BREATH BACK\r
    You have a pool of stamina and\r
    can use it to protect yourself from harm.\r
    \r
    COMBAT WITH BIG WEAPONS \r
    When you are equipped with a two-handed weapon,\r
    you can occasionally use your vitality to\r
    increase % damage.""",

            'BR':
                """
    RECUPERE SUA RESPIRAÇÃO\r
    Você tem uma reserva de resistência,\r
    e pode usá-la para se proteger de danos.\r
    \r
    COMBATE COM ARMAS GRANDES\r
    Quando você está equipado com uma arma de duas mãos,\r
    ocasionalmente você pode usar sua\r
    vitalidade para aumentar % de dano."""
        },

    'g_mage':
        {
            'EN':
                """
    OVERLOAD\r
    You can increase the power of your simpler spells.\r
    Occasionally your magic negates\r
    the opponent's defense.\r
    \r
    ARCANA RECOVERY\r
    You learned how to recover some of your\r
    magical energy by studying your spellbook.\r
    (mana regeneration)""",

            'BR':
                """
    SOBRECARGA\r
    Você pode aumentar o poder de seus\r
    feitiços mais simples.\r
    Ocasionalmente, sua magia anula\r
    a defesa do oponente.\r
    \r
    RECUPERAÇÃO ARCANA\r
    Você aprendeu a recuperar um\r
    pouco de sua energia\r
    mágica estudando seu grimório.\r
    (regeneração de mana)"""
        },

    'g_warden':
        {
            'EN':
                """
    FORTIFICATION \r
    Warden are experts in defense,\r
    and know how to maximize the\r
    potential of their armor,\r
    you receive a 5% bonus for each piece of\r
    heavy armor equipment.\r
    \r
    DEFENSE SPECIALIST\r
    Your accumulated fortification,\r
    every 5 hits received,\r
    regenerates 8% of your health.""",

            'BR':
                """
    FORTIFICAÇÃO\r
    Os Guardiões são especialistas em defesa, \r
    e sabem como maximizar\r
    o potencial de suas armaduras,\r
    você recebe um bônus de 5%\r
    para cada peça de equipamento de armadura pesada.\r
    \r
    ESPECIALISTA EM DEFESA\r
    Sua fortificação acumulada,\r
    a cada 5 acertos recebidos,\r
    regenera 8% de sua saúde."""
        },

}
