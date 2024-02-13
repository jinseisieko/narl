import numpy as np
import pygame as pg

from source.Constants import WIDTH, HEIGHT
from source.Interface.Buttons import Button
from source.Interface.TextNameAndDescription import TextNameAndDescription
from source.Interface.Video import Video


class EnemiesInformationInterface:
    def __init__(self, screen, main_window, video=Video("resource/video/gameplay1.mov")) -> None:
        super().__init__()
        self.main_window = main_window
        self.screen = screen
        self.background = pg.Surface((WIDTH, HEIGHT))
        self.video = video
        self.list_enemies = []

        self.shift = 0

        self.font1 = pg.font.Font('resource/fonts/EightBits.ttf', 150)
        self.font2 = pg.font.Font('resource/fonts/EightBits.ttf', 90)

        self.text1 = self.font1.render("Enemies", 0, "#7452ff", )
        self.text_rect1 = self.text1.get_rect()
        self.text_rect1.center = np.array([WIDTH / 2, 40])

        with open(r"resource/data/enemies.txt", "r", encoding="utf-8") as f:  # важный файл
            lines = f.readlines()
            print(lines)
            for i in range(0, len(lines), 3):
                self.list_enemies.append(
                    TextNameAndDescription(lines[i].strip(), lines[i + 1].strip(), lines[i + 2].strip(), enemies=True))
        print(self.list_enemies)
        self.button_exit = Button("Exit", np.array([WIDTH / 2, HEIGHT - 100]), np.array([150, 50]),
                                  font=self.font2)

    def draw(self):
        self.screen.blit(self.background, (0, 0))

        for i, prb in enumerate(self.list_enemies):
            prb.draw(self.screen, WIDTH // 2, 160 * i + 130 + self.shift)

        self.screen.blit(self.text1, self.text_rect1)
        self.button_exit.draw(self.screen)

    def add_shift(self, n):
        self.shift += n
        if self.shift > 0:
            self.shift = 0

        if self.shift < -(len(self.list_enemies) * 160) + (HEIGHT - 400) and (
                len(self.list_enemies) * 160) > (HEIGHT - 400):
            self.shift = -len(self.list_enemies) * 160 + (HEIGHT - 400)
        elif (len(self.list_enemies) * 160) < (HEIGHT - 400):
            self.shift = 0

    def update(self):
        self.video.update(self.background)
        if not self.video.active:
            self.video.repeat()
