import pygame.font

from source.Interface.Buttons import *
from source.Interface.Video import Video


class MainMenuInterface:
    def __init__(self, screen):
        self.screen = screen
        self.background = pg.Surface((WIDTH, HEIGHT))

        self.video = Video("resource/video/gameplay1.mov")

        self.buttons = {}

        self.font1 = pygame.font.Font('resource/fonts/EightBits.ttf', 150)
        self.font2 = pygame.font.Font('resource/fonts/EightBits.ttf', 90)

        self.text1 = self.font1.render("Nightmare:", 0, "#7452ff", )
        self.text_rect1 = self.text1.get_rect()
        self.text_rect1.center = np.array([WIDTH / 2, HEIGHT / 3 - 250])

        self.text2 = self.font1.render("Area of Reality and Lies", True, "#7452ff")
        self.text_rect2 = self.text2.get_rect()
        self.text_rect2.center = np.array([WIDTH / 2, HEIGHT / 3 - 150])

        self.buttons["ContinueButton"] = Button("Continue", np.array([WIDTH / 2, HEIGHT / 3]), np.array([150, 50]),
                                                font=self.font2)
        self.buttons["StartButton"] = Button("Start", np.array([WIDTH / 2, HEIGHT / 3 + 150]), np.array([150, 50]),
                                             font=self.font2)
        self.buttons["ArcadeButton"] = Button("Arcade", np.array([WIDTH / 2, HEIGHT / 3 + 300]), np.array([150, 50]), font=self.font2)
        self.buttons["SettingsButton"] = Button("Settings", np.array([WIDTH / 2, HEIGHT / 3 + 450]),
                                                np.array([150, 50]), font=self.font2)
        self.buttons["ExitButton"] = Button("Exit", np.array([WIDTH / 2, HEIGHT / 3 + 600]), np.array([150, 50]),
                                            font=self.font2)

    def draw(self):
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.text1, self.text_rect1)
        self.screen.blit(self.text2, self.text_rect2)
        self.draw_buttons(self.screen)

    def update(self):
        self.video.update(self.background)
        if not self.video.active:
            self.video.repeat()

    def draw_buttons(self, screen):
        for x in self.buttons.values():
            x.draw(screen)
