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
import constants

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
        self.item_selected = None

    def render(self):
        menu_width = 300
        menu_height = 300

        # Draw menu background
        window_rect = self.surface.get_rect()
        menu_surface = pygame.Surface((menu_width, menu_height))
        menu_surface.fill((0, 0, 0))
        menu_surface_rect = menu_surface.get_rect()
        menu_surface_rect.center = window_rect.center

        # Mouse gubbins
        pos = pygame.mouse.get_pos()
        rpos = (pos[0] - menu_surface_rect.x, pos[1] - menu_surface_rect.y)
        mouse_in_menu = rpos > (0, 0) and rpos < (menu_width, menu_height)

        item_hovered = None

        # Draw list of items
        for i, item in enumerate(self.items):
            # Icon
            width = int(item.owner.w*0.5)
            height = int(item.owner.h*0.5)

            # Figure out which item we're hovering
            if mouse_in_menu:
                item_hovered = int(rpos[1] / height)
                # print(f'Hovering item {item_hovered}')

            icon_surface = pygame.Surface((item.owner.w, item.owner.h))
            icon = pygame.transform.scale(item.owner.sprite[0], (width, height))
            icon_surface.blit(icon, (0, 0))

            bgcol = constants.COLOR_BLACK
            if item_hovered == i:
                bgcol = constants.COLOR_ATOMIC_TANGERINE

            # Text
            text_surface = self.font.render(item.name, False, constants.COLOR_DARK_MODERATE_BLUE, bgcol)

            # Blit surfaces onto menu
            y = 5 + (i * height)
            menu_surface.blit(icon_surface, (5, y))
            menu_surface.blit(text_surface, (10 + width, y + 5))

        self.surface.blit(menu_surface, menu_surface_rect)
        pygame.display.flip()

        if item_hovered != None:
            self.item_selected = item_hovered

    def result(self):
        if self.item_selected != None and self.item_selected < len(self.items):
            return self.items[self.item_selected]
        return None

    def display(self):
        closed = False
        while not closed:
            self.render()
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.KEYDOWN:
                    if event.key == self.key:
                        closed = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        closed = True

        return self.result()

"""
Menu to display for cell/target selection
"""
class SelectMenu:
    def __init__(self, surface, out_render, assets, key):
        self.surface = surface
        self.font = assets.fonts['menu']
        self.key = key
        self.sprite = assets.sprites.S_CELL_HIGHLIGHT
        self.sp2 = self.sprite.copy()
        self.sp2.fill((255, 255, 255, 100), None, pygame.BLEND_RGBA_MULT)
        self.assets = assets
        self.out_render = out_render

    def render(self):
        """
        Draw to screen. Called in the menu while loop
        """
        self.out_render()

        # Divide then multiply to get a Floor effect to the nearest tile
        pos = pygame.mouse.get_pos()
        cell_pos = ( int(pos[0] / self.assets.sprites.width), int(pos[1] / self.assets.sprites.height))
        target_pos = (int(cell_pos[0] * self.assets.sprites.width), int(cell_pos[1] * self.assets.sprites.height))
        self.selected = cell_pos

        self.surface.blit(self.sprite, target_pos)
        pygame.display.flip()

    def result(self):
        return self.selected

    def display(self):
        closed = False
        while not closed:
            self.render()
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.KEYDOWN:
                    if event.key == self.key:
                        closed = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        closed = True

        return self.result()

"""
Menu to display for cell/target selection
"""
class LineToCellMenu:
    def __init__(self, game, key, bypassWalls = False):
        """Constructor
        game: A game instance
        key: The keypress to terminate the menu
        """
        self.surface = game.surface
        self.font = game.assets.fonts['menu']
        self.key = key
        self.sprite = game.assets.sprites.S_CELL_HIGHLIGHT
        self.assets = game.assets
        self.out_render = game.render
        self.level = game.current_level()
        self.bypassWalls = bypassWalls

    def render(self):
        """
        Draw to screen. Called in the menu while loop
        """
        self.out_render()

        # Divide then multiply to get a Floor effect to the nearest tile
        pos = pygame.mouse.get_pos()
        cell_pos = ( int(pos[0] / self.assets.sprites.width), int(pos[1] / self.assets.sprites.height))

        line = self.level.get_line((self.level.player.x, self.level.player.y), cell_pos, self.bypassWalls)
        self.selected = line

        for i, tile in enumerate(line):
            corrected = (int(tile[0] * self.assets.sprites.width), int(tile[1] * self.assets.sprites.height))
            if i == len(line) - 1:
                self.surface.blit(self.sprite, corrected)
            else:
                temp = pygame.Surface((self.assets.sprites.width, self.assets.sprites.height))
                temp.fill(constants.COLOR_ARYLIDE_YELLOW)
                temp.set_alpha(80)
                self.surface.blit(temp, corrected)

        pygame.display.flip()

    def result(self):
        return self.selected

    def display(self):
        closed = False
        while not closed:
            self.render()
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.KEYDOWN:
                    if event.key == self.key:
                        closed = True
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        closed = True

        return self.result()