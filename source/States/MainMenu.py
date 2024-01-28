import time

import numpy as np
import pygame as pg

from source.Interface.MainMenuTitle import MainMenuTitle
from source.States.InterfaceState import InterfaceState


class MainMenu(InterfaceState):

    def begin(self):
        pg.mouse.set_visible(True)
        self.game.fps = self.title_screen.video.fps

    def __init__(self, screen, game) -> None:
        super().__init__(screen, game)

        self.title_screen: MainMenuTitle = MainMenuTitle(self.screen)

        self.begin()

    def update(self):
        self.title_screen.update()
        self.title_screen.draw()

    def check_events(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_pos = np.array(pg.mouse.get_pos())
                if self.title_screen.buttons["ContinueButton"].update(mouse_pos):
                    self.game.change_state("MainGameMode", mode=1)
                if self.title_screen.buttons["StartButton"].update(mouse_pos):
                    self.game.change_state("MainGameMode", mode=0)
                if self.title_screen.buttons["ArcadeButton"].update(mouse_pos):
                    pass
                if self.title_screen.buttons["SettingsButton"].update(mouse_pos):
                    pass
                if self.title_screen.buttons["ExitButton"].update(mouse_pos):
                    self.game.running = False
                    time.sleep(0.2)
