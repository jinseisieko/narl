import numpy as np
import pygame as pg

from source.Interface.PauseInterface import PauseInterface
from source.Save.Save import save
from source.States.InterfaceData import Data
from source.States.InterfaceState import InterfaceState
from source.Settings.SettingsData import CONTROLS


class PauseArcade(InterfaceState):

    def __init__(self, screen, main_window, last_, last_frame) -> None:
        super().__init__(screen, main_window)
        self.type = "Pause"
        self.data = last_
        self.title_pause = PauseInterface(self.screen, last_frame)
        self.begin()

    def update(self):
        self.title_pause.update()
        self.title_pause.draw()

    def begin(self):
        pg.mouse.set_visible(True)

    def check_events(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_pos = np.array(pg.mouse.get_pos())
                if self.title_pause.buttons["ContinueButton"].update(mouse_pos):
                    self.data.start()
                    self.main_window.set_state(self.data)
                if self.title_pause.buttons["ExitMenuButton"].update(mouse_pos):
                    self.main_window.tasksAndAchievements.save()
                    self.main_window.change_state("MainMenu")
