import constants

class Log:
    def __init__(self):
        self.messages = []
        self.messages.append(('debug', 'Log initialized'))
        self.font = constants.FONT_DBG2
        self.font_height = self.get_font_height()
        self.lines = 8
    
    def add(self, message, level):
        self.messages.append((level, message))
    
    def r2(self, surface):
        pos = self.lines if len(self.messages) >= self.lines else len(self.messages)
        lines = self.messages[-pos:]

        y = 0

        for i in range(pos):
            level, text = lines[i]            
            self.render(f'[{level}]: {text}', (0, y), surface)
            y += self.font_height

    def render(self, text, coords, surface):
        text_surface, text_rect = self.create_text_surface(text, constants.COLOR_WHITE)
        text_rect.topleft = coords
        surface.blit(text_surface, text_rect)

    def create_text_surface(self, text, color):
        text_surface = self.font.render(text, False, color, constants.COLOR_BLACK)
        return text_surface, text_surface.get_rect()
    
    def set_font(self, font):
        self.font = font
        self.font_height = self.get_font_height()
    
    def get_font_height(self):
        fo = self.font.render('a', False, (0,0,0))
        fr = fo.get_rect()
        return fr.height
