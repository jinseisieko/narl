import numpy as np
import pygame as pg


class TextInput:
    font = pg.font.Font(None, 27)

    def __init__(self, x_, y_) -> None:
        super().__init__()
        self.color1: tuple[int, int, int] = (0, 0, 0)
        self.color2: tuple[int, int, int] = (100, 100, 100)

        self.text: str = ''
        self.txt_surface: pg.Surface = self.font.render(self.text, True, self.color1)

        self.x: int = x_
        self.y: int = y_

        self.width: int = max(200, self.txt_surface.get_width() + 10)
        self.height: int = self.txt_surface.get_height()
        self.half_size = np.array([self.width // 2, self.width // 2])
        self.active = False

    def handle_event(self, event) -> None:
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                x_, y_ = pg.mouse.get_pos()
                if self.x < x_ < self.x + self.width and self.y < y_ < self.y + self.height:
                    self.active = True
                else:
                    self.active = False
        if self.active:
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
        self.txt_surface = self.font.render(self.text, True, self.color1)

    def update(self) -> None:
        self.width = max(200, self.txt_surface.get_width() + 10)
        self.height = self.txt_surface.get_height() + 4
        self.half_size = np.array([self.width // 2, self.width // 2])

    def draw(self, screen) -> None:
        """method for drawing text input"""
        screen.blit(self.txt_surface, (self.x + 5, self.y + 5))
        pg.draw.rect(screen, self.color1 if self.active else self.color2, (self.x, self.y, self.width, self.height), 2)

    def get(self):
        return self.text
