'''Main Game container object'''
# pylint: disable=no-member
import pygame
import constants
import messages as Messages
import level as Level
import assets as Assets
import menus as Menus

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
        self.clock.tick(constants.FPS_LIMIT)
        # self.log.add(f'FPS: {str(int(self.clock.get_fps()))}', 'debug')
        return False

    def render(self):
        ''' The main game rendering method '''
        # Clear the display
        self.surface.fill(constants.COLOR_DEFAULT_BG)

        self.current_level().render(self.surface)

        # Update the display
        self.log.render_lines(self.surface)
        pygame.display.flip()

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
                    objects = level.get_objects(level.player.x, level.player.y)

                    for o in objects:
                        if o.item:
                            o.item.pick_up(level.player)
                    return 'player-action'
                if event.key == pygame.K_d:
                    items = level.player.container.contents
                    for i in items:
                        i.drop(level.player.x, level.player.y)
                    return 'player-action'
                if event.key == pygame.K_p:
                    self.menu_pause()

    def menu_pause(self):
        menu_closed = False

        menu = Menus.PauseMenu(self.surface, self.assets)


        while not menu_closed:
            menu.render()
            events = pygame.event.get()
            for event in events:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_p:
                        menu_closed = True