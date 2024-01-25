import numpy as np
import pygame as pg

from source.States.InterfaceState import InterfaceState
from source.Interface.TitleScreen import TitleScreen


class MainMenu(InterfaceState):

    def start(self):
        pg.mouse.set_visible(True)
        self.game.fps = self.title_screen.video.fps

    def __init__(self, screen, game) -> None:
        super().__init__(screen, game)

        self.title_screen: TitleScreen = TitleScreen(self.screen)

        self.start()

    def update(self):
        self.title_screen.update()
        self.title_screen.draw()

    def check_events(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_pos = np.array(pg.mouse.get_pos())
                if self.title_screen.buttons["ContinueButton"].update(mouse_pos):
                    self.game.change_state("MainGameMode")
                if self.title_screen.buttons["ExitButton"].update(mouse_pos):
                    self.game.running = False
                    quit()