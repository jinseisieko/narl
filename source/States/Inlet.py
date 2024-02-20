import numpy as np
import pygame as pg

from source.Interface.InletInterface import InletInterface
from source.Interface.Video import Video
from source.Inventory.Items.ItemModel import init
from source.Settings.Settings import load_settings
from source.Settings.SettingsData import MASTER_VOLUME, MUSIC_VOLUME, SFX_VOLUME, MAX_FPS, CONTROLS
from source.States.InterfaceState import InterfaceState
from source.States.MainMenu import MainMenu


class Inlet(InterfaceState):
    def begin(self):
        pg.mouse.set_visible(True)
        self.main_window.fps = self.inlet_interface.video.fps

    def __init__(self, screen, main_window, video=Video("resource/video/gameplay1.mp4")) -> None:
        super().__init__(screen, main_window)

        self.inlet_interface: InletInterface = InletInterface(self.screen, video=video)
        self.begin()

    def update(self):
        self.inlet_interface.update()
        self.inlet_interface.draw()

    def check_events(self, event):
        self.inlet_interface.check_event(event)
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_pos = np.array(pg.mouse.get_pos())
                if self.inlet_interface.buttons["LogIn"].update(mouse_pos):
                    self.main_window.meta_player.set(self.inlet_interface.text_input1.get(),
                                                     self.inlet_interface.text_input2.get())
                    self.main_window.set_state(MainMenu(self.screen, self.main_window))
                    self.main_window.tasksAndAchievements.init()
                    init(self.main_window.meta_player.name)
                    load_settings(MASTER_VOLUME, MUSIC_VOLUME, SFX_VOLUME, MAX_FPS, CONTROLS,
                                  self.main_window.meta_player.name)
                if self.inlet_interface.buttons["SignIn"].update(mouse_pos):
                    self.main_window.meta_player.register(self.inlet_interface.text_input1.get(),
                                                          self.inlet_interface.text_input2.get())
                    self.main_window.set_state(
                        MainMenu(self.screen, self.main_window, video=self.inlet_interface.video))
                    self.main_window.tasksAndAchievements.init()
                    init(self.main_window.meta_player.name)
                    load_settings(MASTER_VOLUME, MUSIC_VOLUME, SFX_VOLUME, MAX_FPS, CONTROLS,
                                  self.main_window.meta_player.name)
