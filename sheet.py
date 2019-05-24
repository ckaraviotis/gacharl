'''A simple sprite sheet'''
import pygame
import sprites_dawn as sprites


class Sheet:
    def __init__(self, width, height, rows, cols, image):
        self.width = width
        self.height = height
        self.rows = rows
        self.cols = cols
        
        # Scale up the image!
        orig = pygame.image.load(image)
        size = orig.get_size()
        self.image = pygame.transform.scale(orig, (int(size[0]*sprites.SCALE_MULT), int(size[1]*sprites.SCALE_MULT)))

        # Create a default sprite from the top-left
        self.sprites = {'default': self.index((0, 0))}
        
    
    def index(self, loc):
        '''loc should be a tuple of (col, row)'''
        return self.image.subsurface((loc[0] * self.width, loc[1] * self.height, self.width, self.height))
    
    def add(self, name, loc):
        self.sprites[name] = self.index(loc)
    
    def get(self, name):
        return self.sprites[name]
