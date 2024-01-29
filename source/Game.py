import pygame as pg
from pygame import Surface

from source.Constants import *
from source.Functions.Functions import DT
from source.Image.InitializationForGame import init_images_for_game
from source.Image.InitializationForItems import init_images_for_items
from source.States.InterfaceState import InterfaceState
from source.States.Loading import Loading
from source.States.MainGameMode import MainGameMode
from source.States.MainMenu import MainMenu
from source.States.Pause import Pause


class Game:

    def __init__(self) -> None:
        super().__init__()
        self.fps = FPS

        self.screen: pg.Surface = pg.display.set_mode((WIDTH, HEIGHT), flags=pg.NOFRAME, depth=0)
        init_images_for_items()
        init_images_for_game()
        self.state: InterfaceState = MainMenu(self.screen, self)

        self.dt = 0
        self.key_pressed: (list, None) = None
        self.running = True

        # pg.mixer.music.load("../resource/music/chipichipichapachapa.mp3")
        # pg.mixer.music.play(loops=-1)
        # pg.mixer.music.queue("../resource/music/Y2mate.mx - Bruh sound effect (128 kbps).mp3", loops=-1)
        # pg.mixer.music.queue("../resource/music/Y2mate.mx - Metal pipe falling sound effect but it’s more violent (128 kbps).mp3", loops=-1)
        # pg.mixer.music.set_volume(1)

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

    def change_state(self, name, data=None, mode=0):

        if name == "MainGameMode":
            self.state = Loading(self.screen, self, MainGameMode(self.screen, self, mode=mode))
        if name == "MainMenu":
            self.state = MainMenu(self.screen, self)
        if name == "Pause":
            self.state = Pause(self.screen, self, last_=data, last_frame=Surface((0, 0)))


    def set_state(self, class_):
        self.state = class_


GAME = None
Game()
