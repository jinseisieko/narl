from source.Constants import *
from source.Settings.SettingsData import *


class Button:
    def __init__(self, text, pos, half_size, color1="#000000", color2="#7452ff", font=None):
        self.half_size = half_size
        self.pos = pos
        self.background = pg.Surface(2 * self.half_size)
        self.background.fill(color1)
        self.font = font
        if font is None:
            self.font = pg.font.Font(None, 90)
        self.text = self.font.render(text, True, color2)
        self.text_rect = self.text.get_rect()
        self.text_rect.center = self.pos

    def draw(self, screen):
        screen.blit(self.background, self.pos - self.half_size)
        screen.blit(self.text, self.text_rect)

    def update(self, mouse_pos):
        if len(np.where(np.abs(mouse_pos - self.pos) <= self.half_size)[0]) == 2:
            sn1 = pg.mixer.Sound("resource/music/click3.mp3")
            sn1.set_volume(0.2 * SFX_VOLUME[0] * MASTER_VOLUME[0])
            sn1.play()
            return 1
        return 0


class ImageButton(Button):
    def __init__(self, pos, half_size, image):
        super().__init__('', pos, half_size, 'black', 'black', None)
        self.background = pg.Surface(2 * self.half_size + 10)
        self.background.fill((255, 255, 255))
        image = pg.transform.scale(image, (2 * self.half_size))
        self.background.blit(image, (5, 5))


class ItemButton(ImageButton):
    def __init__(self, pos, half_size, image):
        super().__init__(pos, half_size, image)
