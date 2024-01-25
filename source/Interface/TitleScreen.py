from source.Interface.Buttons import *
from source.Interface.Video import Video


class TitleScreen:
    def __init__(self, screen):
        self.screen = screen
        self.background = pg.Surface((WIDTH, HEIGHT))

        self.video = Video("../resource/video/chipichipichapachapa.avi")

        self.buttons = {}

        self.text1 = pygame.font.Font(None, 100).render("Nightmare:", True, "#2792B7")
        self.text_rect1 = self.text1.get_rect()
        self.text_rect1.center = np.array([WIDTH / 2, HEIGHT / 3 - 250])

        self.text2 = pygame.font.Font(None, 100).render("Area of Reality and Lies", True, "#2792B7")
        self.text_rect2 = self.text2.get_rect()
        self.text_rect2.center = np.array([WIDTH / 2, HEIGHT / 3 - 150])

        self.buttons["ContinueButton"] = ContinueButton(self.background)
        self.buttons["StartButton"] = StartButton(self.background)
        self.buttons["ArcadeButton"] = ArcadeButton(self.background)
        self.buttons["SettingsButton"] = SettingsButton(self.background)
        self.buttons["ExitButton"] = ExitButton(self.background)

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
