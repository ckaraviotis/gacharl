def get_font_height(font, text):
        fo = font.render(text, False, (0,0,0))
        fr = fo.get_rect()
        return fr.height

def get_font_width(font, text):
        fo = font.render(text, False, (0,0,0))
        fr = fo.get_rect()
        return fr.width