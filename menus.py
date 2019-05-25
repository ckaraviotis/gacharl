import pygame

"""
Simple menu to display when paused
"""
class PauseMenu:
    def __init__(self, surface, assets):
        self.surface = surface
        self.font = assets.fonts['menu']

    def render(self):
        text_surface = self.font.render('PAUSED', False, (0, 235, 0), (0, 0, 0))

        text_rect = text_surface.get_rect()
        window_rect = self.surface.get_rect()
        text_rect.center = window_rect.center

        self.surface.blit(text_surface, text_rect)
        pygame.display.flip()