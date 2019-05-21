import pygame
from sheet import Sheet
pygame.init()


WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# Color defs
COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_GREY = (100, 100, 100)

COLOR_DEFAULT_BG = COLOR_GREY

# Map vars
MAP_WIDTH = 50
MAP_HEIGHT = 20

# Sprites!
SPRITE_WIDTH = 16
SPRITE_HEIGHT = 16

# Sprite Sheets
PLAYERS = Sheet(SPRITE_WIDTH, SPRITE_HEIGHT, 15, 8, "data/img/Characters/Player0.png")
PLAYERS.add('Warrior', (0, 1))
PLAYERS.add('Ranger', (0, 2))
PLAYERS.add('Barbarian', (0, 3))

SLIMES = Sheet(SPRITE_WIDTH, SPRITE_HEIGHT, 15, 8, "data/img/Characters/Slime0.png")
SLIMES.add('SlimeA', (1, 0))
SLIMES.add('SlimeB', (1, 1))
SLIMES.add('SlimeC', (1, 2))

FLOOR = Sheet(SPRITE_WIDTH, SPRITE_HEIGHT, 39, 21, "data/img/Objects/Floor.png")
FLOOR.add('TOP_LEFT', (12, 0))
FLOOR.add('TOP_CENTER', (12, 1))
FLOOR.add('TOP_RIGHT', (12, 2))
FLOOR.add('MID_LEFT', (13, 0))
FLOOR.add('MID_CENTER', (13, 1))
FLOOR.add('MID_RIGHT', (13, 2))
FLOOR.add('BOT_LEFT', (14, 0))
FLOOR.add('BOT_CENTER', (14, 1))
FLOOR.add('BOT_RIGHT', (14, 2))

WALL = Sheet(SPRITE_WIDTH, SPRITE_HEIGHT, 52, 20, "data/img/Objects/Wall.png")
WALL.add('TOP_LEFT', (6, 0))
WALL.add('TOP_CENTER', (6, 1))
WALL.add('TOP_RIGHT', (6, 2))
WALL.add('MID_LEFT', (7, 0))
WALL.add('MID_CENTER', (7, 1))
WALL.add('MID_RIGHT', (7, 2))
WALL.add('BOT_LEFT', (8, 0))
WALL.add('BOT_CENTER', (8, 1))
WALL.add('BOT_RIGHT', (8, 2))

# Individual sprites
S_PLAYER = PLAYERS.get('default')
S_FLOOR = FLOOR.get('MID_CENTER')
S_WALL = WALL.get('MID_CENTER')
S_ENEMY = SLIMES.get('SlimeB')
S_ENEMY_2 = SLIMES.get('SlimeA')
