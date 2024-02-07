from typing import Any

import pygame as pg
from pygame import Surface

from source.Constants import *
from source.Functions.Functions import DT
from source.Image.InitializationForGame import init_images_for_game
from source.Image.InitializationForItems import init_images_for_items
from source.Interface.InletInterface import InletInterface
from source.MetaPlayer.MetaPlayer import MetaPlayer
from source.Settings.SettingsData import *
from source.States.Inlet import Inlet
from source.States.InterfaceState import InterfaceState
from source.States.Loading import Loading
from source.States.MainGameMode import MainGameMode
from source.States.MainMenu import MainMenu
from source.States.Pause import Pause
from source.Settings.SettingsData import *
from source.States.Settings import Settings
from source.Save.ModelSave import set_save_db


class MainWindow:
    """Game window Class"""

    def __init__(self) -> None:
        super().__init__()
        self.fps: int = MAX_FPS[0]

        set_save_db("resource/players/test_pl1")
        self.fps: int = MAX_FPS
        self.meta_player = MetaPlayer()
        self.meta_player.init_db()
        self.screen: pg.Surface = pg.display.set_mode((WIDTH, HEIGHT), flags=pg.NOFRAME, depth=0)

        # need to initialize pygame images after creating screen
        init_images_for_items()
        init_images_for_game()

        # is the main variable that is responsible for the state, like pause or main menu.
        self.state: InterfaceState = Inlet(self.screen, self)

        self.dt: float = 0

        self.key_pressed: (list, None) = None
        self.running: bool = True

        # pg.mixer.music.load("../resource/music/chipichipichapachapa.mp3")
        # pg.mixer.music.play(loops=-1)
        # pg.mixer.music.queue("../resource/music/Y2mate.mx - Bruh sound effect (128 kbps).mp3", loops=-1)
        # pg.mixer.music.queue("../resource/music/Y2mate.mx - Metal pipe falling sound effect but it’s more violent (128 kbps).mp3", loops=-1)
        # pg.mixer.music.set_volume(1)

        # Singleton architecture element
        global MAIN_WINDOW
        MAIN_WINDOW = self

    def change_pseudo_constants(self) -> None:
        """method of updating all constants in the frame"""
        self.dt = DT(CLOCK)
        self.key_pressed = pg.key.get_pressed()

    def end_cycle(self):
        """method is needed to complete the action in the frame"""
        pg.display.flip()
        CLOCK.tick(self.fps)

    def play(self):
        """main method for window operation"""
        self.change_pseudo_constants()
        for event in pg.event.get():
            if event.type == pg.QUIT or self.key_pressed[pg.K_DELETE]:
                self.running = False
                quit()
            self.state.check_events(event)
        self.state.update()
        self.end_cycle()

    def change_state(self, name: str, data: Any = None) -> None:
        """status selection function"""
        if name == "MainGameMode":
            self.state = Loading(self.screen, self, MainGameMode, self.screen, self, mode=data)
        if name == "MainMenu":
            self.state = MainMenu(self.screen, self)
        if name == "Pause":
            self.state = Pause(self.screen, self, last_=data, last_frame=Surface((0, 0)))

    def set_state(self, class_: InterfaceState) -> None:
        """status setting function"""
        self.state = class_


MAIN_WINDOW: (MainMenu, None) = None
if MAIN_WINDOW is None:
    MainWindow()
