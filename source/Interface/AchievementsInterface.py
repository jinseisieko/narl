import pygame.font

from source.Interface.Buttons import *
from source.Interface.ProgressBar import ProgressBar
from source.Interface.Video import Video


class AchievementsInterface:
    def __init__(self, screen, tasksAndAchievements, video=Video("resource/video/gameplay1.mp4")):
        self.screen = screen
        self.background = pg.Surface((WIDTH, HEIGHT))
        self.tasksAndAchievements = tasksAndAchievements
        self.video = video

        self.font1 = pygame.font.Font('resource/fonts/EightBits.ttf', 150)
        self.font2 = pygame.font.Font('resource/fonts/EightBits.ttf', 90)

        self.text1 = self.font1.render("Achievements", 0, "#7452ff", )
        self.text_rect1 = self.text1.get_rect()
        self.text_rect1.center = np.array([WIDTH / 2, 40])
        self.shift = 0

        self.list_progress_bar = []

        for task in tasksAndAchievements.achievements.values():
            if task["id"] == "kill_1000_enemies":
                self.list_progress_bar.append(
                    ProgressBar(1000, task["data"]["count"], task["name"], task["description"],
                                fulfillment=task["fulfillment"]))

        self.button_exit = Button("Exit", np.array([WIDTH / 2, HEIGHT - 100]), np.array([150, 50]),
                                  font=self.font2)

    def draw(self):
        self.screen.blit(self.background, (0, 0))

        for i, prb in enumerate(self.list_progress_bar):
            prb.draw(self.screen, WIDTH // 2, 160 * i + 130 + self.shift)

        self.screen.blit(self.text1, self.text_rect1)
        self.button_exit.draw(self.screen)

    def add_shift(self, n):
        self.shift += n
        if self.shift > 0:
            self.shift = 0

        if self.shift < -(len(self.list_progress_bar) * 160) + (HEIGHT - 400) and (
                len(self.list_progress_bar) * 160) > (HEIGHT - 400):
            self.shift = -len(self.list_progress_bar) * 160 + (HEIGHT - 400)
        elif (len(self.list_progress_bar) * 160) < (HEIGHT - 400):
            self.shift = 0

    def update_progress_bars(self):
        mouse_pos = np.array(pg.mouse.get_pos())
        for i, prb in enumerate(self.list_progress_bar):
            prb.update(mouse_pos, WIDTH // 2, 160 * i + 130 + self.shift)

    def update(self):

        self.video.update(self.background)
        if not self.video.active:
            self.video.repeat()
