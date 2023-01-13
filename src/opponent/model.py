class EnemyModel(object):
    name: str = "..."
    classe: str = "tag"
    level: int = 1

    force: float = 1
    agility: float = 1
    vitality: float = 1
    intelligence: float = 1
    resistance: float = 1

    xp: float = 1
    gold: int = 1
    soul: int = 1
    sprite: str = "..."

    health: float = 1
    energy: float = 1
    stamina: float = 1

    c_health: float = 1
    c_energy: float = 1
    c_stamina: float = 1

    r_health: float = 0.005
    r_energy: float = 0.005
    r_stamina: float = 0.009

    attack: float = 1
    defense: float = 1
    dodge: float = 1
    block: float = 1
    critical: float = 1
    luck: float = 1
