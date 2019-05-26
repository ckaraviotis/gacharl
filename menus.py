"""
Define all the menus in the game

Menus are a class with a few methods.

display: The entry point for the class. Fires up a loop that stays open until
a condition is met (e.g. a keypress)

render: Called in the display() while loop. Draws the menu to the screen.

result: If the menu needs to return something (e.g. an item selection), it is
handled through this method.
"""
# pylint: disable=no-member,too-many-function-args
import pygame
import utils

"""
Simple menu to display when paused
Use this as a starting point for further menus
"""
class PauseMenu:
    def __init__(self, surface, assets, key):
        self.surface = surface
        self.font = assets.fonts['menu']
        self.key = key

    def render(self):
        """
        Draw to screen. Called in the menu while loop
        """
        text_surface = self.font.render('PAUSED', False, (0, 235, 0), (0, 0, 0))

        text_rect = text_surface.get_rect()
        window_rect = self.surface.get_rect()
        text_rect.center = window_rect.center

        self.surface.blit(text_surface, text_rect)
        pygame.display.flip()

    def display(self):
        """
        Activate the menu. Halts game activity while open
        """
        closed = False
        while not closed:
            self.render()
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.KEYDOWN:
                    if event.key == self.key:
                        closed = True

"""
Menu to display choices when the player opens their inventory
"""
class InventoryMenu:
    def __init__(self, surface, assets, key, items):
        self.surface = surface
        self.font = assets.fonts['menu2']
        self.key = key
        self.items = items

    def render(self):
        # Draw menu background
        window_rect = self.surface.get_rect()
        menu_surface = pygame.Surface((300, 600))
        menu_surface.fill((0, 0, 0))
        menu_surface_rect = menu_surface.get_rect()
        menu_surface_rect.center = window_rect.center

        # Draw list of items
        for i, item in enumerate(self.items):
            # Icon
            width = int(item.owner.w*0.5)
            height = int(item.owner.h*0.5)
            icon_surface = pygame.Surface((item.owner.w, item.owner.h))
            icon = pygame.transform.scale(item.owner.sprite[0], (width, height))
            icon_surface.blit(icon, (0, 0))

            # Text
            text_surface = self.font.render(item.owner.name, False, (80, 100, 150), (0, 0, 0))

            # Blit surfaces onto menu
            y = 5 + (i * height)
            menu_surface.blit(icon_surface, (5, y))
            menu_surface.blit(text_surface, (10 + width, y + 5))

        self.surface.blit(menu_surface, menu_surface_rect)
        pygame.display.flip()

    def display(self):
        closed = False
        while not closed:
            self.render()
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.KEYDOWN:
                    if event.key == self.key:
                        closed = True