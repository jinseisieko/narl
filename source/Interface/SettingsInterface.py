import pygame as pg

from source.Constants import *
from source.Interface.Buttons import Button
from source.Interface.TextInput import TextInput
from source.Interface.Video import Video


class SettingsInterface():
    def __init__(self, screen) -> None:
        super().__init__()
        self.background = pg.Surface((WIDTH, HEIGHT))
        self.font2 = pygame.font.Font('resource/fonts/EightBits.ttf', 90)

        self.video = Video("resource/video/gameplay1.mov")

        self.text_input1 = TextInput(WIDTH / 2 - 100, HEIGHT / 4)
        self.text_input2 = TextInput(WIDTH / 2 - 100, HEIGHT / 4 + 100)
        self.text_input3 = TextInput(WIDTH / 2 - 100, HEIGHT / 4 + 200)
        self.text_input4 = TextInput(WIDTH / 2 - 100, HEIGHT / 4 + 300)

        self.button_exit = Button("Exit", np.array([WIDTH / 2, HEIGHT / 4 + 400]), np.array([150, 50]), font=self.font2)
        self.button_apply = Button("Apply", np.array([WIDTH / 2, HEIGHT / 4 + 200]), np.array([150, 50]), font=self.font2)

        self.screen = screen

    def draw(self):
        self.screen.blit(self.background, (0, 0))
        self.text_input1.draw(self.screen)
        self.text_input2.draw(self.screen)
        self.text_input3.draw(self.screen)
        self.text_input4.draw(self.screen)
        self.button_exit.draw(self.screen)
        self.button_apply.draw(self.screen)

    def update(self):
        self.text_input1.update()
        self.text_input2.update()
        self.text_input3.update()
        self.text_input4.update()

        self.video.update(self.background)
        if not self.video.active:
            self.video.repeat()

    def check_event(self, event):
        self.text_input1.handle_event(event)
        self.text_input2.handle_event(event)
        self.text_input3.handle_event(event)
        self.text_input4.handle_event(event)
