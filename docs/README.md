<div align="center">
    <img align="center" src="https://img.shields.io/badge/Python-white?style=for-the-badge&logo=python&logoColor=yellow">
    <img align="center" src="https://img.shields.io/badge/PYGAME-white?style=for-the-badge&logo=python&logoColor=orange">    
    <img align="center" src="https://img.shields.io/badge/SQLITE3-white?style=for-the-badge&logo=sqlite&logoColor=blue">
</div>

<br>

<h1 align="center">
    The Hero's Journey  v.2.6
</h1>


<div align="center">
    <img windth="500" src="img/gif1.gif">
    <img windth="500" src="img/gif2.gif">
</div>

## About

This is my first personal project \o/

I started this game to practice programming, I chose to make this game because it would be fun and also a challenge.

It's in the first version, I'll add and refine it over time, but for now you can download and play. (Soon I will share the executable on google drive.)

The Hero's Journey is a turn-based rpg, and its plot takes place on a continent in chaos between factions, kingdoms, races and even worlds.


## The current scope:

- Choose from three ethnicities of Elves
- Choose from three classes according to your chosen ethnicity
- Create and Delete characters (up to 9 characters saved)
- Level progression system
- 55 areas to venture into and battle with region-specific opponents.
- Battle system (Attack, Defend and Evade)
- Battle Status System (Dodge, Block, Critical)
- Intuitive battle log

> You can watch the video on [Youtube](https://www.youtube.com/watch?v=v-M-O1niVuk)



## Run game

Clone this project
```console
git clone https://github.com/Fernando-Medeiros/Pygame-RPG.git
```

Create the virtual environment
```console
virtualenv .venv
```

Activate .venv
```console
# Linux
source .venv/bin/activate
# Windows Power Shell
.\.venv\Scripts\activate.ps1
```

Install dependencies
```console
pip install -r requirements.txt
```

Start the game
```console
python main.py
```


## Structure
```console
.
├── app
│   ├── battle
│   │   ├── battle.py
│   │   ├── log.py
│   │   ├── skills.py
│   │   └── view.py
│   ├── character
│   │   ├── base.py
│   │   ├── character.py
│   │   ├── settings.py
│   │   └── view.py
│   ├── database
│   │   ├── base.py
│   │   ├── enemies_db.py
│   │   ├── enemies.json
│   │   ├── map_db.py
│   │   ├── map.json
│   ├── events.py
│   ├── functiontools.py
│   ├── game.py
│   ├── menu
│   │   ├── load.py
│   │   ├── menu.py
│   │   ├── newgame.py
│   │   ├── options.py
│   │   └── settings.py
│   ├── opponent
│   │   ├── base.py
│   │   ├── opponent.py
│   │   └── view.py
│   └── sound.py
├── docs
│   ├── img
│   │   └── ...
│   ├── LICENSE
│   ├── log.txt
│   └── README.md
├── main.py
├── paths.py
├── requirements.txt
├── runtime.txt
├── save
│   └── ...
└── static
    ├── context_info
    │   ├── dark
    │   │   └── ...
    │   ├── forest
    │   │   └── ...
    │   └── grey
    │       └── ...
    ├── images
    │   ├── classes
    │   │   └── ...
    │   ├── enemies
    │   │   └── ...
    │   │  
    │   ├── menu
    │   │   ├── load
    │   │   │   └── ...
    │   │   ├── newgame
    │   │   │   └── ...
    │   │   ├── options
    │   │   │   └── ...
    │   │   └── ...
    │   └── sprites_credits.txt
    ├── sound
    │   └── ...
    └── soundtrack
        └── ...
```


## Menu

When starting the Game you have the following options:

- New game
- Load game
- Credits
- Configuration
- Quit


 Basic system settings:

- Standard screen 747 x 1050 or Full Screen
- Increase game speed from 30 FPS to 60 FPS
- Mute


<div align="center">
    <img windth="470" height="300" src="img/menu.png">
    <img windth="470" height="300" src="img/credits.png">
    <img windth="470" height="300" src="img/options.png">
</div>


## Create and Load the Character

The game allows a maximum of 9 save games

When creating a new game:

- Each elf ethnicity has its history and characteristics.
- Each ethnicity has three classes
- Each class has unique abilities.


<div align="center">
    <img windth="470" height="300" src="img/newgame.png">
    <img windth="470" height="300" src="img/classes.png">
    <img windth="470" height="300" src="img/load.png">
</div>


## Exploring the World

The game currently has 55 areas

Each area has an average of 10 unique opponents with randomly generated stats

The battle system:

- Basic Actions (Attack, Defend, Evade)
- Intuitive battle log
- Stamina consumption for stocks
- Automatic health, energy and stamina regeneration


<div align="center">
    <img windth="470" height="300" src="img/game-world.png">
    <img windth="470" height="300" src="img/game-battle.png">
    <img windth="470" height="300" src="img/sprites.png">
</div>


## Credits

All opponent and character sprites are authored by the
[Oryx Design Lab](https://www.oryxdesignlab.com/home)

The game map is authored by
[Rarameth](https://www.deviantart.com/rarameth/art/Terras-Novas-Arkan-Mapa-para-RPG-de-mesa-659378593)


## License

License - MIT

You can reuse this project, remember that Oryx Design Lab sprites and Rarameth map have not been licensed for commercial purposes, this project is for study purposes only.