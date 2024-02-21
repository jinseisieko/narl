from source.Functions.Functions import *
from source.Interface.Buttons import Button
from source.Interface.Video import Video


class SettingsInterfaceSecond:
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
        self.button_next = Button(">", np.array([WIDTH - HEIGHT / 12, HEIGHT / 12]), np.array([50, 50]),
                                  font=self.font2)

        self.screen = screen

        self.forward_change_button = Button(get_key_code(CONTROLS["FORWARD"]).replace("K_", ""), np.array([WIDTH / 2, 100]),
                                            np.array([150, 50]),
                                            font=self.font2)

        self.backward_change_button = Button(get_key_code(CONTROLS["BACKWARD"]).replace("K_", ""), np.array([WIDTH / 2, 200]), np.array([150, 50]),
                                             font=self.font2)

        self.left_change_button = Button(get_key_code(CONTROLS["LEFT"]).replace("K_", ""), np.array([WIDTH / 2, 300]), np.array([150, 50]),
                                         font=self.font2)

        self.right_change_button = Button(get_key_code(CONTROLS["RIGHT"]).replace("K_", ""), np.array([WIDTH / 2, 400]), np.array([150, 50]),
                                          font=self.font2)

    def draw(self):
        self.screen.blit(self.background, (0, 0))

        self.button_exit.draw(self.screen)
        self.button_apply.draw(self.screen)
        self.button_next.draw(self.screen)
        self.button_back.draw(self.screen)
        self.forward_change_button.draw(self.screen)
        self.backward_change_button.draw(self.screen)
        self.left_change_button.draw(self.screen)
        self.right_change_button.draw(self.screen)

    def update(self):
        self.video.update(self.background)
        if not self.video.active:
            self.video.repeat()

    def check_event(self, event): ...
