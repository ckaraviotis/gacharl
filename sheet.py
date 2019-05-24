'''A simple sprite sheet'''
import pygame
pygame.init()

class Sheet:
    def __init__(self, width, height, scale, image, animated = True):
        self.width = width
        self.height = height
        self.scale = scale
        self.animated = animated

        if self.animated:
            frame0 = f'{image}0.png'
            frame1 = f'{image}1.png'
            
            # Scale up the image!
            orig = pygame.image.load(frame0).convert_alpha()
            size = orig.get_size()
            self.image = pygame.transform.scale(orig, (int(size[0]*self.scale), int(size[1]*self.scale)))

            # Scale up the image! - Frame 2
            orig = pygame.image.load(frame1).convert_alpha()
            size = orig.get_size()
            self.image1 = pygame.transform.scale(orig, (int(size[0]*self.scale), int(size[1]*self.scale)))
        else:
            # Scale up the image!
            orig = pygame.image.load(f'{image}.png').convert_alpha()
            size = orig.get_size()
            self.image = pygame.transform.scale(orig, (int(size[0]*self.scale), int(size[1]*self.scale)))

        # Automatic spriteage
        new_size = self.image.get_size()
        cols = int(new_size[0] / self.width)
        rows = int(new_size[1] / self.height)

        self.info = f'{image}: x:{cols}, y{rows}'
        self.sprites = []
        self.sprites1 = []

        for y in range(rows):
            r = []
            r2 = []
            for x in range(cols):
                r.append(self.index((x, y)))
                if self.animated:
                    r2.append(self.index2((x, y)))
            self.sprites.append(r)
            if self.animated:
                self.sprites1.append(r2)
        
        msg = 'init done'

        
    # TODO: Refactor this jesus
    def index(self, loc):
        '''loc should be a tuple of (col, row)'''
        return self.image.subsurface((loc[0] * self.width, loc[1] * self.height, self.width, self.height))

    def index2(self, loc):
        '''loc should be a tuple of (col, row)'''
        return self.image1.subsurface((loc[0] * self.width, loc[1] * self.height, self.width, self.height))

    def get(self, coords, frame = 0):
        if self.animated:
            if frame > 0:
                return self.sprites1[coords[1]][coords[0]]

        return self.sprites[coords[1]][coords[0]]
            