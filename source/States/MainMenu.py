import time

import numpy as np
import pygame as pg

from source.Interface.MainMenuInterface import MainMenuInterface
from source.Settings.SettingsData import CONTROLS_1, CONTROLS_2
from source.States.InterfaceState import InterfaceState
from source.States.SettingsFirst import SettingsFirst


class MainMenu(InterfaceState):

    def begin(self):
        pg.mouse.set_visible(True)
        self.main_window.fps = self.title_screen.video.fps

    def __init__(self, screen, main_window) -> None:
        super().__init__(screen, main_window)

        self.title_screen: MainMenuInterface = MainMenuInterface(self.screen)
        self.begin()

    def update(self):
        self.title_screen.update()
        self.title_screen.draw()

    def check_events(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == CONTROLS_1["PRESS_L"] or event.button == CONTROLS_2["PRESS_L"]:
                mouse_pos = np.array(pg.mouse.get_pos())
                if self.title_screen.buttons["ContinueButton"].update(mouse_pos):
                    self.main_window.change_state("MainGameMode", data=1)
                if self.title_screen.buttons["StartButton"].update(mouse_pos):
                    self.main_window.change_state("MainGameMode", data=0)
                if self.title_screen.buttons["ArcadeButton"].update(mouse_pos):
                    self.main_window.change_state("RedactorMode", data=0)
                if self.title_screen.buttons["SettingsButton"].update(mouse_pos):
                    self.main_window.set_state(SettingsFirst(self.screen, self.main_window))
                if self.title_screen.buttons["ExitButton"].update(mouse_pos):
                    self.main_window.running = False
                    time.sleep(0.2)
