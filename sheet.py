'''A simple sprite sheet'''
import constants
import pygame

class Sheet:
    def __init__(self, width, height, rows, cols, image):
        self.width = width
        self.height = height
        self.rows = rows
        self.cols = cols
        
        # Scale up the image!
        orig = pygame.image.load(image)
        size = orig.get_size()
        self.image = pygame.transform.scale(orig, (int(size[0]*2), int(size[1]*2)))

        # Create a default sprite from the top-left
        self.sprites = {'default': self.index((0, 0))}
        
    
    def index(self, loc):
        '''loc should be a tuple of (row, col)'''
        return self.image.subsurface((loc[1] * self.width, loc[0] * self.height, self.width, self.height))
    
    def add(self, name, loc):
        self.sprites[name] = self.index(loc)
    
    def get(self, name):
        return self.sprites[name]
