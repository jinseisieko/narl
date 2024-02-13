import pyperclip

from source.Settings.SettingsData import *


class TextInput:
    font = pg.font.Font("resource/fonts/EightBits.ttf", 90)

    def __init__(self, x_, y_, w=700, f_s=90, b_w=6) -> None:
        super().__init__()
        self.b_w = b_w
        self.w = w
        self.font = pg.font.Font("resource/fonts/EightBits.ttf", f_s)
        self.color1: tuple[int, int, int] = (0, 0, 0)
        self.color2: tuple[int, int, int] = (100, 100, 100)

        self.text: str = ''
        self.txt_surface: pg.Surface = self.font.render(self.text, True, self.color1)

        self.x: int = x_
        self.y: int = y_

        self.width: int = max(w, self.txt_surface.get_width() + 10)
        self.height: int = self.txt_surface.get_height()
        self.half_size = np.array([self.width // 2, self.height // 2])
        self.active = False

        self.ctrl = False

    def handle_event(self, event) -> None:
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                x_, y_ = pg.mouse.get_pos()
                if self.x - self.half_size[0] < x_ < self.x + self.half_size[0] and self.y - self.half_size[
                    1] < y_ < self.y + self.half_size[1]:
                    self.active = True
                else:
                    self.active = False
        if self.active:
            if event.type == pg.KEYUP:
                if event.key == pg.KMOD_CTRL or event.key == pg.K_LCTRL:
                    self.ctrl = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.KMOD_CTRL or event.key == pg.K_LCTRL:
                    self.ctrl = True
                elif event.key == pg.K_v and self.ctrl:
                    self.text += pyperclip.paste()
                elif event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
        self.txt_surface = self.font.render(self.text, True, self.color1)

    def update(self) -> None:
        self.width = max(self.w, self.txt_surface.get_width() + 10)
        self.height = self.txt_surface.get_height() + 4
        self.half_size = np.array([self.width // 2, self.height // 2])

    def draw(self, screen) -> None:
        """method for drawing text input"""
        screen.blit(self.txt_surface, (self.x + 10 - self.half_size[0], self.y + 3 - self.half_size[1]))
        pg.draw.rect(screen, self.color1 if self.active else self.color2,
                     (self.x - self.half_size[0], self.y - self.half_size[1], self.width, self.height), self.b_w)

    def get(self):
        return self.text

    def set(self, text):
        self.text = str(text)
