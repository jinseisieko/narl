import pygame as pg

from source.Constants import *
from source.Settings.SettingsData import SFX_VOLUME, MASTER_VOLUME


class ProgressBar:
    font1 = pg.font.Font("resource/fonts/EightBits.ttf", 90)
    font2 = pg.font.Font("resource/fonts/EightBits.ttf", 40)

    def __init__(self, max_, dt_, name, description, w=(WIDTH // 2) - 400, h=75) -> None:
        super().__init__()

        self.w = w
        self.h = h
        self.max_ = max_
        self.dt_ = dt_
        self.name = name
        self.description = description

        self.progress_bar = pg.Surface((w * 2, h * 2)).convert_alpha()
        self.progress_bar.fill((0, 0, 0, 0))
        self.text_name = self.font1.render(self.name, True, (0, 0, 0))
        self.text_description = self.font2.render(self.description, True, (0, 0, 0))
        self.progress_bar.blit(self.text_name, (0, 0))
        pg.draw.rect(self.progress_bar, (255, 255, 255), (0, self.text_name.get_height() + 5, self.w * 2, 30))
        pg.draw.rect(self.progress_bar, "#7452ff",
                     (0, self.text_name.get_height() + 5, int((self.w * 2) / self.max_ * self.dt_), 30))
        pg.draw.rect(self.progress_bar, (0, 0, 0), (0, self.text_name.get_height() + 5, self.w * 2, 30),
                     width=5)

        self.description_ = False

    def draw(self, screen, x, y):
        screen.blit(self.progress_bar, (x - self.w, y))
        if self.description_:
            pg.draw.rect(screen, (255, 255, 255),
                         (x + self.w - self.text_description.get_width(), y + self.h//2, self.text_description.get_width(),
                          self.text_description.get_height()))
            screen.blit(self.text_description, (x + self.w - self.text_description.get_width(), y + self.h//2, self.text_description.get_width(),
                          self.text_description.get_height()))

    def update(self, mouse_pos, x, y):
        if len(np.where(np.abs(mouse_pos - np.array((x, y + self.h))) <= np.array((self.w, self.h)))[0]) == 2:
            sn1 = pg.mixer.Sound("resource/music/click3.mp3")
            sn1.set_volume(0.2 * SFX_VOLUME[0] * MASTER_VOLUME[0])
            sn1.play()
            self.description_ = True
            return
        self.description_ = False
