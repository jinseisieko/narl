import numpy as np
import pygame as pg

from source.Interface.AchievementsInterface import AchievementsInterface
from source.Interface.Video import Video
from source.States.InterfaceState import InterfaceState


class Achievements(InterfaceState):

    def begin(self):
        pg.mouse.set_visible(True)
        self.main_window.fps = self.interface_screen.video.fps

    def __init__(self, screen, main_window, video=Video("resource/video/gameplay1.mp4")) -> None:
        super().__init__(screen, main_window)

        self.interface_screen: AchievementsInterface = AchievementsInterface(self.screen, self.main_window.tasksAndAchievements, video=video)
        self.begin()

        self.movement = False
        self.last_mouse_pos = pg.mouse.get_pos()

    def update(self):
        self.interface_screen.update()
        self.interface_screen.draw()

        if self.movement:
            self.interface_screen.add_shift(pg.mouse.get_pos()[1] - self.last_mouse_pos[1])

        self.last_mouse_pos = pg.mouse.get_pos()

    def check_events(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                if self.interface_screen.button_exit.update(np.array(pg.mouse.get_pos())):
                    self.main_window.change_state("MainMenu")
                    return
                self.interface_screen.update_progress_bars()

            if event.button == 3:
                self.movement = True

        if event.type == pg.MOUSEBUTTONUP:
            if event.button == 3:
                self.movement = False
