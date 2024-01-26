import pygame as pg

from source.Constants import *


class Button:
    def __init__(self,text, pos, half_size, color1="yellow", color2="red", font=None):
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
            return 1
        return 0


class ContinueButton(Button):
    def __init__(self, screen, font=None):
        super().__init__("Continue", np.array([WIDTH / 2, HEIGHT / 3]), np.array([150, 50]), font=font)


class StartButton(Button):
    def __init__(self, screen, font=None):
        super().__init__("Start", np.array([WIDTH / 2, HEIGHT / 3 + 150]), np.array([150, 50]), font=font)


class ArcadeButton(Button):
    def __init__(self, screen, font=None):
        super().__init__("Arcade", np.array([WIDTH / 2, HEIGHT / 3 + 300]), np.array([150, 50]), font=font)


class SettingsButton(Button):
    def __init__(self, screen, font=None):
        super().__init__( "Settings", np.array([WIDTH / 2, HEIGHT / 3 + 450]), np.array([150, 50]), font=font)


class ExitButton(Button):
    def __init__(self, screen, font=None):
        super().__init__("Exit", np.array([WIDTH / 2, HEIGHT / 3 + 600]), np.array([150, 50]), font=font)
