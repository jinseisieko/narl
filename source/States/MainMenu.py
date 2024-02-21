import time

import numpy as np
import pygame as pg

from source.Interface.MainMenuInterface import MainMenuInterface
from source.Interface.Video import Video
from source.Settings.SettingsContainer import SettingsContainer
from source.States.Achievements import Achievements
from source.States.Arcade import Arcade
from source.States.EnemiesInformation import EnemiesInformation
from source.States.InterfaceState import InterfaceState
from source.States.ItemInformation import ItemInformation
from source.States.ItemsCreator import ItemsCreator
from source.States.Loading import Loading
from source.States.SettingsFirst import SettingsFirst
from source.States.Tasks import Tasks


class MainMenu(InterfaceState):

    def begin(self):
        pg.mouse.set_visible(True)
        self.main_window.fps = self.interface_screen.video.fps

    def __init__(self, screen, main_window, video=Video("resource/video/gameplay1.mp4")) -> None:
        super().__init__(screen, main_window)

        self.interface_screen: MainMenuInterface = MainMenuInterface(self.screen, video)
        self.begin()

    def update(self):
        self.interface_screen.update()
        self.interface_screen.draw()

    def check_events(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_pos = np.array(pg.mouse.get_pos())
                if self.interface_screen.buttons["ContinueButton"].update(mouse_pos):
                    self.main_window.change_state("MainGameMode", data=1)
                if self.interface_screen.buttons["StartButton"].update(mouse_pos):
                    self.main_window.change_state("MainGameMode", data=0)
                if self.interface_screen.buttons["ArcadeButton"].update(mouse_pos):
                    self.main_window.set_state(Loading(self.screen, self.main_window, Arcade, self.screen, self.main_window))
                if self.interface_screen.buttons["SettingsButton"].update(mouse_pos):
                    self.main_window.set_state(
                        SettingsFirst(self.screen, self.main_window, video=self.interface_screen.video,
                                      settings_container=SettingsContainer(self.main_window)))
                if self.interface_screen.buttons["Tasks"].update(mouse_pos):
                    self.main_window.set_state(Tasks(self.screen, self.main_window))
                if self.interface_screen.buttons["ExitButton"].update(mouse_pos):
                    self.main_window.running = False
                    time.sleep(0.2)
                if self.interface_screen.buttons["ItemsCreator"].update(mouse_pos):
                    self.main_window.set_state(ItemsCreator(self.screen, self.main_window))
                if self.interface_screen.buttons["Achievements"].update(mouse_pos):
                    self.main_window.set_state(Achievements(self.screen, self.main_window))
                if self.interface_screen.buttons["Items"].update(mouse_pos):
                    self.main_window.set_state(ItemInformation(self.screen, self.main_window))
                if self.interface_screen.buttons["Enemies"].update(mouse_pos):
                    self.main_window.set_state(EnemiesInformation(self.screen, self.main_window))


