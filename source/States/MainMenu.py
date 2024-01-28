import numpy as np
import pygame as pg

from source.Interface.TitleScreen import TitleScreen
from source.States.InterfaceState import InterfaceState


class MainMenu(InterfaceState):

    def begin(self):
        pg.mouse.set_visible(True)
        self.game.fps = self.title_screen.video.fps

    def __init__(self, screen, game) -> None:
        super().__init__(screen, game)

        self.title_screen: TitleScreen = TitleScreen(self.screen)

        self.begin()

    def update(self):
        self.title_screen.update()
        self.title_screen.draw()

    def check_events(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                sn1 = pg.mixer.Sound("../resource/music/click.mp3")
                sn1.set_volume(0.2)
                sn1.play()
                mouse_pos = np.array(pg.mouse.get_pos())
                if self.title_screen.buttons["ContinueButton"].update(mouse_pos):
                    self.game.change_state("MainGameMode")
                if self.title_screen.buttons["ExitButton"].update(mouse_pos):
                    self.game.running = False
                    quit()
