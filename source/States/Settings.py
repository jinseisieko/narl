from source.Interface.SettingsInterface import SettingsInterface
import source.Settings.SettingsData
from source.States.InterfaceState import InterfaceState
import pygame as pg

class Settings(InterfaceState):

    def __init__(self, screen, game) -> None:
        super().__init__(screen, game)
        self.game = game
        self.interface_setting = SettingsInterface(screen)
        self.begin()

    def update(self):
        self.interface_setting.update()
        self.interface_setting.draw()

    def check_events(self, event):
        self.interface_setting.check_event(event)

        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == source.Settings.SettingsData.CONTROLS_1["PRESS"] or event.button == source.Settings.SettingsData.CONTROLS_2["PRESS"]:
                if self.interface_setting.button_exit.update(pg.mouse.get_pos()):
                    self.game.change_state("MainMenu")
                if self.interface_setting.button_apply.update(pg.mouse.get_pos()):
                    source.Settings.SettingsData.update(
                        self.interface_setting.text_input1.get(),
                        self.interface_setting.text_input2.get(),
                        self.interface_setting.text_input3.get(),
                        self.interface_setting.text_input4.get()
                    )
                    self.game.change_state("MainMenu")

    def begin(self):
        pg.mouse.set_visible(True)
        self.game.fps = self.interface_setting.video.fps
