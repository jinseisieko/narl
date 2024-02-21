from source.Functions.Functions import *
from source.Interface.Buttons import Button
from source.Interface.Video import Video


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

        self.menu_change_button = Button(get_key_code(CONTROLS["MENU"]).replace("K_", ""),
                                         np.array([WIDTH / 2 + 300, HEIGHT // 2 - 300 - 50]),
                                         np.array([150, 50]), font=self.font2)

        self.shoot_change_button = Button(get_key_code(CONTROLS["SHOOT"]).replace("K_", ""),
                                          np.array([WIDTH / 2 + 300, HEIGHT // 2 - 100 - 50]),
                                          np.array([150, 50]), font=self.font2)

        self.console_change_button = Button(get_key_code(CONTROLS["OPEN_CONSOLE"]).replace("K_", ""),
                                            np.array([WIDTH / 2 + 300, HEIGHT // 2 + 100 - 50]),
                                            np.array([150, 50]), font=self.font2)

        self.menu_text = self.font2.render("Open menu", 0, 0)
        self.menu_text_rect = self.menu_text.get_rect()
        self.menu_text_rect.center = [WIDTH // 2 - 300, HEIGHT // 2 - 300 - 50]

        self.shoot_text = self.font2.render("Shoot", 0, 0)
        self.shoot_text_rect = self.shoot_text.get_rect()
        self.shoot_text_rect.center = [WIDTH // 2 - 300, HEIGHT // 2 - 100 - 50]

        self.console_text = self.font2.render("Open console", 0, 0)
        self.console_text_rect = self.console_text.get_rect()
        self.console_text_rect.center = [WIDTH // 2 - 300, HEIGHT // 2 + 100 - 50]

        self.screen = screen

    def draw(self):
        self.screen.blit(self.background, (0, 0))

        self.screen.blit(self.menu_text, self.menu_text_rect)
        self.screen.blit(self.shoot_text, self.shoot_text_rect)
        self.screen.blit(self.console_text, self.console_text_rect)


        self.button_exit.draw(self.screen)
        self.button_apply.draw(self.screen)
        self.button_back.draw(self.screen)
        self.menu_change_button.draw(self.screen)
        self.shoot_change_button.draw(self.screen)
        self.console_change_button.draw(self.screen)

    def update(self):
        self.video.update(self.background)
        if not self.video.active:
            self.video.repeat()

    def check_event(self, event): ...
