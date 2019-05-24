import pygame
import constants
import sprites_dawn as sprites
import messages as Messages
import level as Level

class Game:
    def __init__(self):
        self.sprites = sprites.Sprites()
        self.surface = pygame.display.set_mode((constants.MAP_WIDTH * self.sprites.width, constants.MAP_HEIGHT * self.sprites.height))
        self.sprites.load()
        self.level = []
        self.log = Messages.Log()
        self.create_level()
        self.clock = pygame.time.Clock()
    
    def current_level(self):
        return self.level[-1]
    
    def create_level(self):
        self.level.append(Level.Level(self, constants.MAP_WIDTH, constants.MAP_HEIGHT))
    
    def update(self):
        events = pygame.event.get()
        ai_move = False

        level = self.current_level()

        # Process events this frame
        for event in events:
            if event.type == pygame.QUIT:
                return True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_UP:
                    level.player.creature.move(0, -1, level)
                    ai_move = True
                if event.key == pygame.K_DOWN:
                    level.player.creature.move(0, 1, level)
                    ai_move = True
                if event.key == pygame.K_LEFT:
                    level.player.creature.move(-1, 0, level)
                    ai_move = True
                if event.key == pygame.K_RIGHT:
                    level.player.creature.move(1, 0, level)
                    ai_move = True
                if event.key == pygame.K_PERIOD:
                    level.player.creature.move(0, 0, level)
                    ai_move = True
        
        # Handle FOV
        level.calculate_fov(level.player.x, level.player.y, 8)

        # Ai Turns
        if ai_move:
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