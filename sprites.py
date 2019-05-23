from sheet import Sheet

# Sprites!
SPRITE_WIDTH = 17
SPRITE_HEIGHT = 17

# Sprite Sheets
SPRITES = Sheet(SPRITE_WIDTH, SPRITE_HEIGHT, 3, 32, "data/img/colored_transparent.png")
# Floor tiles
SPRITES.add('FloorA', (0, 0))
SPRITES.add('FloorB', (0, 1))
SPRITES.add('FloorC', (0, 2))
SPRITES.add('FloorD', (0, 3))
SPRITES.add('FloorE', (0, 4))

# Wall tiles
SPRITES.add('TOP_LEFT', (0, 18))
SPRITES.add('TOP_CENTER', (0, 19))
SPRITES.add('TOP_RIGHT', (0, 20))
SPRITES.add('MID_LEFT', (1, 18))
SPRITES.add('MID_CENTER', (1, 19))
SPRITES.add('MID_RIGHT', (1, 20))
SPRITES.add('BOT_LEFT', (2, 18))
SPRITES.add('BOT_CENTER', (2, 19))
SPRITES.add('BOT_RIGHT', (2, 20))

SPRITES.add('Wizzy', (0, 24))
SPRITES.add('Man', (0, 25))
SPRITES.add('Manspear', (0, 26))
SPRITES.add('Fiteboi', (0, 27))

SPRITES.add('Gobbo', (3, 25))
SPRITES.add('BigGob', (3, 26))


# Individual sprites
S_PLAYER = SPRITES.get('Wizzy')
S_FLOOR = SPRITES.get('FloorC')
S_WALL = SPRITES.get('BOT_CENTER')
S_ENEMY = SPRITES.get('Gobbo')
S_ENEMY_2 = SPRITES.get('BigGob')

S_WALL_UNEXPLORED = SPRITES.get('BOT_CENTER_DARK')
S_FLOOR_UNEXPLORED = SPRITES.get('FloorC_DARK')
