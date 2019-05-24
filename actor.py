'''An Actor is the base class for all other objects in the game'''

class Actor:
    def __init__(self, x, y, w, h, sprite, name, messages, creature = None, ai = None):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.sprite = sprite
        self.name = name
        self.creature = creature
        self.ai = ai
        self.messages = messages

        if creature:    
            creature.owner = self
        if ai:
            ai.owner = self

    def render(self, surface):
         # Draw character
        surface.blit(self.sprite, (self.x * self.w, self.y * self.h))
