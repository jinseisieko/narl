from source.Interface.PauseTitle import PauseTitle
from source.States.InterfaceState import InterfaceState
import pygame as pg
import numpy as np


class Pause(InterfaceState):
    def __init__(self, screen, game) -> None:
        super().__init__(screen, game)

        self.title_pause = PauseTitle(self.screen)
        self.start()

    def update(self):
        self.title_pause.update()
        self.title_pause.draw()

    def start(self):
        pg.mouse.set_visible(True)

    def check_events(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_pos = np.array(pg.mouse.get_pos())
                if self.title_pause.buttons["ContinueButton"].update(mouse_pos):
                    self.game.change_state("MainGameMode")
                if self.title_pause.buttons["ExitMenuButton"].update(mouse_pos):
                    self.game.change_state("MainMenu")
