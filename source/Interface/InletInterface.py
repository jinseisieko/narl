import pygame.font

from source.Interface.Buttons import *
from source.Interface.TextInput import TextInput
from source.Interface.Video import Video


class InletInterface:
    def __init__(self, screen, video=Video("resource/video/gameplay1.mov")):
        self.screen = screen
        self.background = pg.Surface((WIDTH, HEIGHT))

        self.video = video

        self.buttons = {}

        self.font1 = pygame.font.Font('resource/fonts/EightBits.ttf', 150)
        self.font2 = pygame.font.Font('resource/fonts/EightBits.ttf', 90)

        self.text1 = self.font1.render("Nightmare:", 0, "#7452ff", )
        self.text_rect1 = self.text1.get_rect()
        self.text_rect1.center = np.array([WIDTH / 2, HEIGHT / 3 - 250])

        self.text2 = self.font1.render("Area of Reality and Lies", True, "#7452ff")
        self.text_rect2 = self.text2.get_rect()
        self.text_rect2.center = np.array([WIDTH / 2, HEIGHT / 3 - 150])

        self.text_input1 = TextInput(WIDTH / 2, HEIGHT / 4 + 50)
        self.text_input2 = TextInput(WIDTH / 2, HEIGHT / 4 + 200)

        self.buttons["LogIn"] = Button("LogIn", np.array([WIDTH / 2, HEIGHT / 4 + 400]), np.array([150, 50]),
                                       font=self.font2)
        self.buttons["SignIn"] = Button("SignIn", np.array([WIDTH / 2, HEIGHT / 4 + 550]), np.array([150, 50]),
                                        font=self.font2)

    def draw(self):
        self.screen.blit(self.background, (0, 0))
        self.text_input1.draw(self.screen)
        self.text_input2.draw(self.screen)
        self.screen.blit(self.text1, self.text_rect1)
        self.screen.blit(self.text2, self.text_rect2)
        self.draw_buttons(self.screen)

    def update(self):
        self.text_input1.update()
        self.text_input2.update()

        self.video.update(self.background)
        if not self.video.active:
            self.video.repeat()

    def draw_buttons(self, screen):
        for x in self.buttons.values():
            x.draw(screen)

    def check_event(self, event):
        self.text_input1.handle_event(event)
        self.text_input2.handle_event(event)
