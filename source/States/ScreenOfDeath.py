import numpy as np
import pygame as pg

from source.Interface.ScreenOfDeathInterface import ScreenOfDeathInterface
from source.States.InterfaceState import InterfaceState


class ScreenOfDeath(InterfaceState):
    def begin(self):
        pg.mouse.set_visible(True)

    def check_events(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                sn1 = pg.mixer.Sound("resource/music/click.mp3")
                sn1.set_volume(0.2)
                sn1.play()
                mouse_pos = np.array(pg.mouse.get_pos())
                if self.title_screen_of_death.buttons["ExitMenuButton"].update(mouse_pos):
                    # создание пустого сохранения
                    self.game.change_state("MainMenu")

    def update(self):
        self.title_screen_of_death.update()
        self.title_screen_of_death.draw()

    def __init__(self, screen, game, last_frame) -> None:
        super().__init__(screen, game)
        self.type = "ScreenOfDeath"
        self.title_screen_of_death = ScreenOfDeathInterface(self.screen, last_frame)
        self.begin()
