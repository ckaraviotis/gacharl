import pygame
pygame.init()


WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600

# Color defs
COLOR_BLACK = (0, 0, 0)
COLOR_WHITE = (255, 255, 255)
COLOR_GREY = (100, 100, 100)

COLOR_DEFAULT_BG = COLOR_GREY

# Sprites?
SPRITE_WIDTH = 16
SPRITE_HEIGHT = 16
DOGS = pygame.image.load("data/img/Characters/Dog1.png")
S_PLAYER = DOGS.subsurface((0,0,SPRITE_WIDTH, SPRITE_HEIGHT))