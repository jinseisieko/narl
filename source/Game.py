import pygame as pg

from source.Constants import *
from source.Functions.Functions import DT
from source.Image.InitializationForGame import init_images_for_game
from source.Image.InitializationForItems import init_images_for_items
from source.States.InterfaceState import InterfaceState
from source.States.MainGameMode import MainGameMode
from source.States.MainMenu import MainMenu


class Game:

    def __init__(self) -> None:
        super().__init__()
        self.fps = FPS

        self.screen: pg.Surface = pg.display.set_mode((WIDTH, HEIGHT), flags=pg.NOFRAME, depth=0)
        init_images_for_items()
        init_images_for_game()
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
        CLOCK.tick(self.fps)

    def play(self):
        self.change_pseudo_constants()
        for event in pg.event.get():
            if event.type == pg.QUIT or self.key_pressed[pg.K_DELETE]:
                self.running = False
                quit()
            self.state.check_events(event)
        self.state.update()
        self.end_cycle()

    def change_state(self, name):
        if name == "MainGameMode":
            self.state = MainGameMode(self.screen, self)


GAME = None
Game()
