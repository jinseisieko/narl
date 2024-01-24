import pygame as pg

from Constants import *


class Button:
    def __init__(self, screen, text, pos, half_size):
        self.screen = screen
        self.half_size = half_size
        self.pos = pos
        self.background = pg.Surface(2 * self.half_size)
        self.background.fill("yellow")
        self.font = pygame.font.Font(None, 72)
        self.text = self.font.render(text, True, "red")
        self.text_rect = self.text.get_rect()
        self.text_rect.center = self.pos

    def draw(self):
        self.screen.blit(self.background, self.pos - self.half_size)
        self.screen.blit(self.text, self.text_rect)

    def update(self, mouse_pos):
        if len(np.where(np.abs(mouse_pos - self.pos) <= self.half_size)[0]) == 2:
            return 1
        return 0


class StartButton(Button):
    def __init__(self, screen):
        super().__init__(screen, "Start", np.array([WIDTH / 2, HEIGHT / 2]), np.array([150, 50]))


class ExitButton(Button):
    def __init__(self, screen):
        super().__init__(screen, "Exit", np.array([WIDTH / 2, HEIGHT / 2 + 200]), np.array([150, 50]))
