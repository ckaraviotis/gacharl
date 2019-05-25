'''An Actor is the base class for all other objects in the game'''
import constants

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
        self.alive = True
        self.animation_speed = 0.5
        self.animation_timer = 0
        self.animation_change = constants.FPS_LIMIT * self.animation_speed
        self.animation_reset = constants.FPS_LIMIT

        if creature:
            creature.owner = self
        if ai:
            ai.owner = self

    def render(self, surface):
         # Draw character
        if len(self.sprite) > 1 and self.alive:
            if self.animation_timer <= self.animation_change:
                surface.blit(self.sprite[0], (self.x * self.w, self.y * self.h))
            else:
                surface.blit(self.sprite[1], (self.x * self.w, self.y * self.h))
            self.animation_timer += 1

            if self.animation_timer >= self.animation_reset:
                self.animation_timer = 0
        else:
            surface.blit(self.sprite[0], (self.x * self.w, self.y * self.h))
