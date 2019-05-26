import constants
import utils

class Log:
    def __init__(self, font):
        self.messages = []
        self.messages.append(('debug', 'Log initialized'))
        self.font = font
        self.font_height = utils.get_font_height(font, 'a')
        self.lines = 8

    def add(self, message, level = 'debug'):
        self.messages.append((level, message))

    def render_lines(self, surface):
        pos = self.lines if len(self.messages) >= self.lines else len(self.messages)
        lines = self.messages[-pos:]

        y = 0

        for i in range(pos):
            level, text = lines[i]
            self.render(f'[{level}]: {text}', (0, y), surface)
            y += self.font_height

    def render(self, text, coords, surface):
        text_surface, text_rect = self.create_text_surface(text, constants.COLOR_GREY)
        text_rect.topleft = coords
        surface.blit(text_surface, text_rect)

    def create_text_surface(self, text, color):
        text_surface = self.font.render(text, False, color, constants.COLOR_BLACK)
        return text_surface, text_surface.get_rect()

    def set_font(self, font):
        self.font = font
        self.font_height = utils.get_font_height(font, 'a')
