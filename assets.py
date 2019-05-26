import pygame
import sprites_dawn as sprites

class Assets:
    def __init__(self):
        self.fonts = self.load_fonts()
        self.sprites = sprites.Sprites()


    def load_fonts(self):
        font_debug = pygame.font.Font('data/fonts/Bebas-Regular.ttf', 24)
        font_menu = pygame.font.Font('data/fonts/Bebas-Regular.ttf', 48)
        font_log = pygame.font.Font('data/fonts/SDS_8x8.ttf', 12)
        font_menu2 = pygame.font.Font('data/fonts/SDS_8x8.ttf', 16)
        return {
            'debug': font_debug,
            'log'  : font_log,
            'menu' : font_menu,
            'menu2': font_menu2
        }

    def load_sprites(self):
        self.sprites.load()