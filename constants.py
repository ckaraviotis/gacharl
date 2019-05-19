import pygame
pygame.init()


WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# Color defs
COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_GREY = (100, 100, 100)

COLOR_DEFAULT_BG = COLOR_GREY

# Map vars
MAP_WIDTH = 30
MAP_HEIGHT = 30

# Sprites!
SPRITE_WIDTH = 16
SPRITE_HEIGHT = 16

# Sprite Sheets
DOGS = pygame.image.load("data/img/Characters/Dog1.png")
FLOOR = pygame.image.load("data/img/Objects/Floor.png")
WALL = pygame.image.load("data/img/Objects/Wall.png")

# Individual sprites
S_PLAYER = DOGS.subsurface((0, 0, SPRITE_WIDTH, SPRITE_HEIGHT))
S_FLOOR = FLOOR.subsurface((1 * SPRITE_WIDTH, 4 * SPRITE_WIDTH, SPRITE_WIDTH, SPRITE_HEIGHT))
S_WALL = WALL.subsurface((0 * SPRITE_WIDTH, 5 * SPRITE_WIDTH, SPRITE_WIDTH, SPRITE_HEIGHT))
