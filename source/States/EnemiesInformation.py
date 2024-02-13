import numpy as np
import pygame as pg

from source.Interface.EnemiesInformationInterface import EnemiesInformationInterface
from source.Interface.Video import Video
from source.States.InterfaceState import InterfaceState


class EnemiesInformation(InterfaceState):

    def __init__(self, screen, main_window, video=Video("resource/video/gameplay1.mov")) -> None:
        super().__init__(screen, main_window)

        self.EnemiesInformation_interface = EnemiesInformationInterface(screen, main_window, video)

        self.movement = False
        self.last_mouse_pos = pg.mouse.get_pos()
        self.begin()

    def update(self):
        self.EnemiesInformation_interface.update()
        self.EnemiesInformation_interface.draw()

        if self.movement:
            self.EnemiesInformation_interface.add_shift(pg.mouse.get_pos()[1] - self.last_mouse_pos[1])

        self.last_mouse_pos = pg.mouse.get_pos()

    def check_events(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                if self.EnemiesInformation_interface.button_exit.update(np.array(pg.mouse.get_pos())):
                    self.main_window.change_state("MainMenu")
                    return

            if event.button == 3:
                self.movement = True

        if event.type == pg.MOUSEBUTTONUP:
            if event.button == 3:
                self.movement = False

    def begin(self):
        pg.mouse.set_visible(True)
        self.main_window.fps = self.EnemiesInformation_interface.video.fps
