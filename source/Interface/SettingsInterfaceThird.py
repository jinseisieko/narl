from source.Constants import *
from source.Interface.Buttons import Button
from source.Interface.Video import Video
from source.Settings.SettingsData import *


class SettingsInterfaceThird:
    def __init__(self, screen) -> None:
        super().__init__()
        self.background = pg.Surface((WIDTH, HEIGHT))
        self.font2 = pygame.font.Font('resource/fonts/EightBits.ttf', 90)

        self.video = Video("resource/video/gameplay1.mov")

        # self.text_input_master_volume = TextInput(WIDTH / 2 - 100, HEIGHT / 4)
        # self.text_input_music_volume = TextInput(WIDTH / 2 - 100, HEIGHT / 4 + 100)
        # self.text_input_sfx_volume = TextInput(WIDTH / 2 - 100, HEIGHT / 4 + 200)
        # self.text_input_fps = TextInput(WIDTH / 2 - 100, HEIGHT / 4 + 300)
        #
        # self.text_input_master_volume.set(MASTER_VOLUME[0])
        # self.text_input_music_volume.set(MUSIC_VOLUME[0])
        # self.text_input_sfx_volume.set(SFX_VOLUME[0])
        # self.text_input_fps.set(MAX_FPS[0])

        self.button_exit = Button("Exit", np.array([WIDTH / 2 - 160, HEIGHT - 100]), np.array([150, 50]),
                                  font=self.font2)
        self.button_apply = Button("Apply", np.array([WIDTH / 2 + 160, HEIGHT - 100]), np.array([150, 50]),
                                   font=self.font2)
        self.button_back = Button("<", np.array([0 + HEIGHT / 12, HEIGHT / 12]), np.array([50, 50]),
                                  font=self.font2)

        self.screen = screen

    def draw(self):
        self.screen.blit(self.background, (0, 0))
        # self.text_input_master_volume.draw(self.screen)
        # self.text_input_music_volume.draw(self.screen)
        # self.text_input_sfx_volume.draw(self.screen)
        # self.text_input_fps.draw(self.screen)
        self.button_exit.draw(self.screen)
        self.button_apply.draw(self.screen)
        self.button_back.draw(self.screen)

    def update(self):
        # self.text_input_master_volume.update()
        # self.text_input_music_volume.update()
        # self.text_input_sfx_volume.update()
        # self.text_input_fps.update()

        self.video.update(self.background)
        if not self.video.active:
            self.video.repeat()

    def check_event(self, event): ...
    # self.text_input_master_volume.handle_event(event)
    # self.text_input_music_volume.handle_event(event)
    # self.text_input_sfx_volume.handle_event(event)
    # self.text_input_fps.handle_event(event)
