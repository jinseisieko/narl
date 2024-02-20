from source.Constants import *
from source.Interface.Buttons import Button
from source.Interface.Video import Video
from source.Settings.SettingsData import *


class SettingsInterfaceThird:
    def __init__(self, screen, container, video=Video("resource/video/gameplay1.mp4")) -> None:
        super().__init__()
        self.background = pg.Surface((WIDTH, HEIGHT))
        self.font2 = pygame.font.Font('resource/fonts/EightBits.ttf', 90)

        self.video = video

        self.container = container

        self.button_exit = Button("Exit", np.array([WIDTH / 2 - 160, HEIGHT - 100]), np.array([150, 50]),
                                  font=self.font2)
        self.button_apply = Button("Apply", np.array([WIDTH / 2 + 160, HEIGHT - 100]), np.array([150, 50]),
                                   font=self.font2)
        self.button_back = Button("<", np.array([0 + HEIGHT / 12, HEIGHT / 12]), np.array([50, 50]),
                                  font=self.font2)

        self.screen = screen

    def draw(self):
        self.screen.blit(self.background, (0, 0))

        self.button_exit.draw(self.screen)
        self.button_apply.draw(self.screen)
        self.button_back.draw(self.screen)

    def update(self):
        self.video.update(self.background)
        if not self.video.active:
            self.video.repeat()

    def check_event(self, event): ...
