from source.Interface.Buttons import *
from source.Interface.Video import Video


class LoadingTitle:
    def __init__(self, screen):
        self.screen = screen
        self.background = pg.Surface((WIDTH, HEIGHT))

        self.video = Video("resource/video/lemon_loading.avi")

    def draw(self):
        self.screen.blit(self.background, (0, 0))

    def update(self):
        self.video.update(self.background)
        if not self.video.active:
            self.video.repeat()
