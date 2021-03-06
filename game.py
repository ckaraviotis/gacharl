'''Main Game container object'''
# pylint: disable=no-member
import pygame
import constants
import messages as Messages
import level as Level
import assets as Assets
import menus as Menus
import effects

class Game:
    def __init__(self):
        self.assets = Assets.Assets()
        self.surface = pygame.display.set_mode((constants.MAP_WIDTH * self.assets.sprites.width, constants.MAP_HEIGHT * self.assets.sprites.height))

        # Load the sprites - called AFTER the display is initialized
        self.assets.load_sprites()

        self.level = []
        self.log = Messages.Log(self.assets.fonts['log'])
        self.create_level()
        self.clock = pygame.time.Clock()
        self.paused = False

    def current_level(self):
        return self.level[-1]

    def create_level(self):
        self.level.append(Level.Level(self, constants.MAP_WIDTH, constants.MAP_HEIGHT))

    def update(self):
        """
        Update all game logic etc.
        Returns True if the game has quit
        """
        events = pygame.event.get()
        level = self.current_level()
        action = self.handle_keys(events, level)

        if action == 'quit':
            return True

        # Handle FOV
        level.calculate_fov(level.player.x, level.player.y, 8)

        # Ai Turns
        if action == 'player-action':
            for npc in level.npcs:
                if npc.ai:
                    npc.ai.turn(level)

        # Render!
        self.render()

        # Update display outside of render loop. This allows other methods
        # E.g. Menu render methods to update the display without causing
        # jitter
        pygame.display.flip()
        # self.log.add(f'FPS: {str(int(self.clock.get_fps()))}', 'debug')
        return False

    def render(self):
        ''' The main game rendering method '''
        # Clear the display
        self.surface.fill(constants.COLOR_DEFAULT_BG)

        self.current_level().render(self.surface)

        # Update the display
        self.log.render_lines(self.surface)
        self.clock.tick(constants.FPS_LIMIT)

    def handle_keys(self, events, level):
        # Process events this frame
        for event in events:
            if event.type == pygame.QUIT:
                return 'quit'
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    level.player.creature.move(0, -1, level)
                    return 'player-action'
                if event.key == pygame.K_DOWN:
                    level.player.creature.move(0, 1, level)
                    return 'player-action'
                if event.key == pygame.K_LEFT:
                    level.player.creature.move(-1, 0, level)
                    return 'player-action'
                if event.key == pygame.K_RIGHT:
                    level.player.creature.move(1, 0, level)
                    return 'player-action'
                if event.key == pygame.K_PERIOD:
                    level.player.creature.move(0, 0, level)
                    return 'player-action'
                if event.key == pygame.K_g:
                    """Get"""
                    objects = level.get_objects(level.player.x, level.player.y)

                    for o in objects:
                        if o.item:
                            o.item.pick_up(level.player)
                    return 'player-action'
                if event.key == pygame.K_d:
                    """Drop"""
                    # TODO: Do we want to access this directly, or have a method on container that handles this?
                    items = [o for o in level.player.container.contents]
                    menu = Menus.InventoryMenu(self.surface, self.assets, pygame.K_d, items)
                    result = menu.display()

                    if result:
                        items = level.player.container.contents
                        for i in items:
                            if i == result:
                                i.drop(level.player.x, level.player.y)
                                return 'player-action'
                if event.key == pygame.K_u:
                    """Use Item"""
                    items = [o for o in level.player.container.contents]
                    menu = Menus.InventoryMenu(self.surface, self.assets, pygame.K_d, items)
                    result = menu.display()

                    if result:
                        items = level.player.container.contents
                        for i in items:
                            if i == result:
                                i.use([level.player, 5])
                                return 'player-action'
                if event.key == pygame.K_p:
                    """Pause"""
                    menu = Menus.PauseMenu(self.surface, self.assets, pygame.K_p)
                    menu.display()
                if event.key == pygame.K_k:
                    """KILL"""
                    menu = Menus.SelectMenu(self.surface, self.render, self.assets, pygame.K_l)
                    result = menu.display()
                    effects.sunstrike([level, self.log, result])

                    return 'player-cast'
                if event.key == pygame.K_l:
                    """Look"""
                    menu = Menus.SelectMenu(self.surface, self.render, self.assets, pygame.K_l)
                    result = menu.display()
                    objects = level.get_objects(result[0], result[1])

                    for o in objects:
                        if o.creature:
                            self.log.add(f'You see {o.creature.name} the {o.name}', 'info')
                        else:
                            self.log.add(f'You see a {o.name}', 'info')

                    return 'player-look'
                if event.key == pygame.K_y:
                    """Lightning"""
                    menu = Menus.LineToCellMenu(self, pygame.K_y, limit=5)
                    result = menu.display()
                    effects.lightning([level, self.log, result])

                    return 'player-cast'
                if event.key == pygame.K_f:
                    """Lightning"""
                    menu = Menus.LineToRadiusMenu(self, pygame.K_f, limit=8, radius=3)
                    result = menu.display()
                    effects.lightning([level, self.log, result])

                    return 'player-cast'
                if event.key == pygame.K_c:
                    """KILL"""
                    menu = Menus.SelectMenu(self.surface, self.render, self.assets, pygame.K_c)
                    result = menu.display()
                    effects.confuse([level, self.log, result])

                    return 'player-cast'
