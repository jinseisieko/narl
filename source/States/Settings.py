import pygame as pg

import source.Settings.SettingsData
from source.Interface.SettingsInterface import SettingsInterface
from source.States.InterfaceState import InterfaceState


class Settings(InterfaceState):

    def __init__(self, screen, main_window) -> None:
        super().__init__(screen, main_window)
        self.main_window = main_window
        self.interface_setting = SettingsInterface(screen)
        self.begin()

    def update(self):
        self.interface_setting.update()
        self.interface_setting.draw()

    def check_events(self, event):
        self.interface_setting.check_event(event)

        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                if self.interface_setting.button_exit.update(pg.mouse.get_pos()):
                    self.main_window.change_state("MainMenu")
                if self.interface_setting.button_apply.update(pg.mouse.get_pos()):
                    source.Settings.SettingsData.update(
                        self.interface_setting.text_input1.get(),
                        self.interface_setting.text_input2.get(),
                        self.interface_setting.text_input3.get(),
                        self.interface_setting.text_input4.get()
                    )
                    self.main_window.change_state("MainMenu")

    def begin(self):
        pg.mouse.set_visible(True)
        self.main_window.fps = self.interface_setting.video.fps
