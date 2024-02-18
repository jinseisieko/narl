import numpy as np
import pygame as pg

from source.Constants import WIDTH, HEIGHT
from source.Interface.Buttons import Button
from source.Interface.TextNameAndDescription import TextNameAndDescription
from source.Interface.Video import Video
from source.Inventory.Items.ItemModel import DB, ItemsRank1, ItemsRank3, ItemsRank2, ItemsBlocked


class ItemInformationInterface:
    def __init__(self, screen, main_window, video=Video("resource/video/gameplay1.mp4")) -> None:
        super().__init__()
        self.main_window = main_window
        self.screen = screen
        self.background = pg.Surface((WIDTH, HEIGHT))
        self.video = video
        self.list_items = []

        self.shift = 0

        self.font1 = pg.font.Font('resource/fonts/EightBits.ttf', 150)
        self.font2 = pg.font.Font('resource/fonts/EightBits.ttf', 90)

        self.text1 = self.font1.render("Items", 0, "#7452ff", )
        self.text_rect1 = self.text1.get_rect()
        self.text_rect1.center = np.array([WIDTH / 2, 40])

        with DB.atomic():
            for item in ItemsRank1.select():
                self.list_items.append(TextNameAndDescription(item.name + " - 1", item.description, item.id))
            for item in ItemsRank2.select():
                self.list_items.append(TextNameAndDescription(item.name + " - 2", item.description, item.id))
            for item in ItemsRank3.select():
                self.list_items.append(TextNameAndDescription(item.name + " - 3", item.description, item.id))

        with DB.atomic():
            for item in ItemsBlocked.select().where(ItemsBlocked.player == self.main_window.meta_player.name):
                print(self.main_window.meta_player.name, item.blocked)
                self.list_items.append(
                    TextNameAndDescription(item.name + " - " + ("blocked" if item.blocked else "unlocked"),
                                           item.description, item.id))

        self.button_exit = Button("Exit", np.array([WIDTH / 2, HEIGHT - 100]), np.array([150, 50]),
                                  font=self.font2)

    def draw(self):
        self.screen.blit(self.background, (0, 0))

        for i, prb in enumerate(self.list_items):
            prb.draw(self.screen, WIDTH // 2, 160 * i + 130 + self.shift)

        self.screen.blit(self.text1, self.text_rect1)
        self.button_exit.draw(self.screen)

    def add_shift(self, n):
        self.shift += n
        if self.shift > 0:
            self.shift = 0

        if self.shift < -(len(self.list_items) * 160) + (HEIGHT - 400) and (
                len(self.list_items) * 160) > (HEIGHT - 400):
            self.shift = -len(self.list_items) * 160 + (HEIGHT - 400)
        elif (len(self.list_items) * 160) < (HEIGHT - 400):
            self.shift = 0

    def update(self):
        self.video.update(self.background)
        if not self.video.active:
            self.video.repeat()
