import numpy as np
import pygame as pg

from source.Interface.PauseTitle import PauseTitle
from source.States.InterfaceData import Data
from source.States.InterfaceState import InterfaceState


class Pause(InterfaceState):

    def __init__(self, screen, game, last_: Data, last_frame) -> None:
        super().__init__(screen, game)
        self.type = "Pause"
        self.data = last_
        self.title_pause = PauseTitle(self.screen, last_frame)
        self.begin()

    def update(self):
        self.title_pause.update()
        self.title_pause.draw()

    def begin(self):
        pg.mouse.set_visible(True)

    def check_events(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                sn1 = pg.mixer.Sound("../resource/music/click.mp3")
                sn1.set_volume(0.2)
                sn1.play()
                mouse_pos = np.array(pg.mouse.get_pos())
                if self.title_pause.buttons["ContinueButton"].update(mouse_pos):
                    self.data.start()
                    self.game.set_state(self.data)
                if self.title_pause.buttons["ExitMenuButton"].update(mouse_pos):
                    ...
                    self.game.change_state("MainMenu")
