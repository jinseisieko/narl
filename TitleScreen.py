import pygame as pg

from Constants import *


class TitleScreen:
    def __init__(self, screen):
        self.screen = screen
        self.background = pg.Surface((WIDTH, HEIGHT))
        self.background.fill("green")
        self.buttons = []
        self.text1 = pygame.font.Font(None, 100).render("Nanotechnology:", None, "#2792B7")
        self.text_rect1 = self.text1.get_rect()
        self.text_rect1.center = np.array([WIDTH / 2, HEIGHT / 2 - 300])
        self.text2 = pygame.font.Font(None, 100).render("Arena of Reality and Lies", None, "#2792B7")
        self.text_rect2 = self.text2.get_rect()
        self.text_rect2.center = np.array([WIDTH / 2, HEIGHT / 2 - 200])

    def draw(self):
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.text1, self.text_rect1)
        self.screen.blit(self.text2, self.text_rect2)
        self.draw_buttons()

    def draw_buttons(self):
        for x in self.buttons:
            x.draw()
