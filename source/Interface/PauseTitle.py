import pygame.font

from source.Interface.Buttons import *
from source.Interface.Video import Video


class PauseTitle:
    def __init__(self, screen, last_frame):
        self.last_frame = last_frame
        self.screen = screen
        self.background = pg.Surface((WIDTH, HEIGHT))
        self.background.blit(self.last_frame, (0, 0))

        self.buttons = {}

        self.font1 = pygame.font.Font('../resource/fonts/EightBits.ttf', 150)
        self.font2 = pygame.font.Font('../resource/fonts/EightBits.ttf', 90)

        self.text1 = self.font1.render("Nightmare:", 0, "#000000", )
        self.text_rect1 = self.text1.get_rect()
        self.text_rect1.center = np.array([WIDTH / 2, HEIGHT / 3 - 250])

        self.text2 = self.font1.render("Area of Reality and Lies", True, "#000000")
        self.text_rect2 = self.text2.get_rect()
        self.text_rect2.center = np.array([WIDTH / 2, HEIGHT / 3 - 150])

        self.buttons["ContinueButton"] = ContinueButton(font=self.font2)
        self.buttons["ExitMenuButton"] = ExitMenuButton(font=self.font2)

    def draw(self):
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.text1, self.text_rect1)
        self.screen.blit(self.text2, self.text_rect2)
        self.draw_buttons(self.screen)

    def update(self):
        ...

    def draw_buttons(self, screen):
        for x in self.buttons.values():
            x.draw(screen)


