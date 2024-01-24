import numpy as np
import pygame as pg

from Buttons import StartButton, ExitButton
from States.InterfaceState import InterfaceState
from TitleScreen import TitleScreen


class MainMenu(InterfaceState):

    def start(self):
        pg.mouse.set_visible(True)

    def __init__(self, screen, game) -> None:
        super().__init__(screen, game)

        self.title_screen: TitleScreen = TitleScreen(self.screen)
        self.title_screen.buttons.append(StartButton(self.title_screen.background))
        self.title_screen.buttons.append(ExitButton(self.title_screen.background))

        self.start()

    def update(self):
        self.title_screen.draw()

    def check_events(self):

        for event in pg.event.get():

            if event.type == pg.QUIT or self.game.key_pressed[pg.K_DELETE]:
                self.game.running = False
                quit()
            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    mouse_pos = np.array(pg.mouse.get_pos())
                    if self.title_screen.buttons[0].update(mouse_pos):
                        self.game.change_state("MainGameMode")
                    if self.title_screen.buttons[1].update(mouse_pos):
                        self.game.running = False
                        quit()
