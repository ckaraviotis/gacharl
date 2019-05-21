'''An Actor is the base class for all other objects in the game'''
import constants

class Actor:
    def __init__(self, x, y, sprite, name, creature = None, ai = None):
        self.x = x
        self.y = y
        self.sprite = sprite
        self.name = name
        self.creature = creature
        self.ai = ai

        if creature:    
            creature.owner = self
        if ai:
            ai.owner = self

    def render(self, surface):
         # Draw character
        surface.blit(self.sprite, (self.x * constants.SPRITE_WIDTH, self.y * constants.SPRITE_HEIGHT))
