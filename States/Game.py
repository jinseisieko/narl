import pygame as pg

from Constants import *
from Functions.Functions import DT
from Inventory.ItemImages.InitializationOfObjectImages import init_images
from States.InterfaceState import InterfaceState
from States.MainGameMode import MainGameMode
from States.MainMenu import MainMenu


class Game:

    def __init__(self) -> None:
        super().__init__()
        self.screen: pg.Surface = pg.display.set_mode((WIDTH, HEIGHT), flags=pg.NOFRAME, depth=0)
        init_images()

        self.state: InterfaceState = MainMenu(self.screen, self)

        self.dt = 1 / FPS
        self.key_pressed: (list, None) = None
        self.running = True

        global GAME
        GAME = self

    def change_pseudo_constants(self):
        self.dt = DT(CLOCK)
        self.key_pressed = pg.key.get_pressed()

    def end_cycle(self):
        pg.display.flip()
        CLOCK.tick(FPS)

    def play(self):
        self.change_pseudo_constants()
        self.state.check_events()
        self.state.update()
        self.end_cycle()

    def change_state(self, name):
        if name == "MainGameMode":
            self.state = MainGameMode(self.screen, self)


GAME = None
Game()
