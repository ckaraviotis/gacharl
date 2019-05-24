from sheet import Sheet

# Sprites!
SOURCE_WIDTH = 16
SOURCE_HEIGHT = 16
SCALE_MULT = 3

SPRITE_WIDTH = SOURCE_WIDTH * SCALE_MULT
SPRITE_HEIGHT = SOURCE_HEIGHT * SCALE_MULT

# Sprite Sheets
PLAYERS = Sheet(SPRITE_WIDTH, SPRITE_HEIGHT, 15, 8, "data/img/Characters/Player0.png")
PLAYERS.add('Warrior',   (1, 0))
PLAYERS.add('Ranger',    (2, 0))
PLAYERS.add('Barbarian', (3, 0))

SLIMES = Sheet(SPRITE_WIDTH, SPRITE_HEIGHT, 15, 8, "data/img/Characters/Slime0.png")
SLIMES.add('SlimeA', (0, 1))
SLIMES.add('SlimeB', (1, 1))
SLIMES.add('SlimeC', (2, 1))

FLOOR = Sheet(SPRITE_WIDTH, SPRITE_HEIGHT, 39, 21, "data/img/Objects/Floor.png")
FLOOR.add('TOP_LEFT',   (0, 6))
FLOOR.add('TOP_CENTER', (1, 6))
FLOOR.add('TOP_RIGHT',  (2, 6))
FLOOR.add('MID_LEFT',   (0, 7))
FLOOR.add('MID_CENTER', (1, 7))
FLOOR.add('MID_RIGHT',  (2, 7))
FLOOR.add('BOT_LEFT',   (0, 8))
FLOOR.add('BOT_CENTER', (1, 8))
FLOOR.add('BOT_RIGHT',  (2, 8))
FLOOR.add('TOP_LEFT_DARK',   (0, 12))
FLOOR.add('TOP_CENTER_DARK', (1, 12))
FLOOR.add('TOP_RIGHT_DARK',  (2, 12))
FLOOR.add('MID_LEFT_DARK',   (0, 13))
FLOOR.add('MID_CENTER_DARK', (1, 13))
FLOOR.add('MID_RIGHT_DARK',  (2, 13))
FLOOR.add('BOT_LEFT_DARK',   (0, 14))
FLOOR.add('BOT_CENTER_DARK', (1, 14))
FLOOR.add('BOT_RIGHT_DARK',  (2, 14))


WALL = Sheet(SPRITE_WIDTH, SPRITE_HEIGHT, 52, 20, "data/img/Objects/Wall.png")
WALL.add('TOP_LEFT',   (0, 6))
WALL.add('TOP_CENTER', (1, 6))
WALL.add('TOP_RIGHT',  (2, 6))
WALL.add('MID_LEFT',   (0, 7))
WALL.add('MID_CENTER', (1, 7))
WALL.add('MID_RIGHT',  (2, 7))
WALL.add('BOT_LEFT',   (0, 8))
WALL.add('BOT_CENTER', (1, 8))
WALL.add('BOT_RIGHT',  (2, 8))
WALL.add('TOP_LEFT_DARK',   (0, 12))
WALL.add('TOP_CENTER_DARK', (1, 12))
WALL.add('TOP_RIGHT_DARK',  (2, 12))
WALL.add('MID_LEFT_DARK',   (0, 13))
WALL.add('MID_CENTER_DARK', (1, 13))
WALL.add('MID_RIGHT_DARK',  (2, 13))
WALL.add('BOT_LEFT_DARK',   (0, 14))
WALL.add('BOT_CENTER_DARK', (1, 14))
WALL.add('BOT_RIGHT_DARK',  (2, 14))


# Individual sprites
S_PLAYER = PLAYERS.get('default')
S_FLOOR = FLOOR.get('MID_CENTER')
S_WALL = WALL.get('MID_CENTER')
S_ENEMY = SLIMES.get('SlimeB')
S_ENEMY_2 = SLIMES.get('SlimeA')

S_FLOOR_UNEXPLORED = FLOOR.get('MID_CENTER_DARK')
S_WALL_UNEXPLORED = WALL.get('MID_CENTER_DARK')
