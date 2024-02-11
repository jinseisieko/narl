import pygame as pg

from source.Interface.SettingsInterfaceFirst import SettingsInterfaceFirst
from source.Interface.Video import Video
from source.Settings.SettingsContainer import SettingsContainer
from source.States.InterfaceState import InterfaceState


class SettingsFirst(InterfaceState):

    def __init__(self, screen, main_window, settings_container=SettingsContainer(),
                 video=Video("resource/video/gameplay1.mov")) -> None:
        super().__init__(screen, main_window)
        self.main_window = main_window
        self.interface_setting = SettingsInterfaceFirst(screen, container=settings_container, video=video)
        self.settings_container = settings_container
        self.begin()

    def update(self):
        self.interface_setting.update()
        self.interface_setting.draw()

    def check_events(self, event):
        self.interface_setting.check_event(event)

        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                if self.interface_setting.button_next.update(pg.mouse.get_pos()):
                    self.main_window.change_state("SettingsSecond",
                                                  (self.settings_container, self.interface_setting.video))
                if self.interface_setting.button_exit.update(pg.mouse.get_pos()):
                    self.main_window.change_state("MainMenu")
                if self.interface_setting.button_apply.update(pg.mouse.get_pos()):
                    # source.Settings.SettingsData.update(
                    #     self.interface_setting.text_input1.get(),
                    #     self.interface_setting.text_input2.get(),
                    #     self.interface_setting.text_input3.get(),
                    #     self.interface_setting.text_input4.get()
                    # )
                    self.main_window.change_state("MainMenu")

    def begin(self):
        pg.mouse.set_visible(True)
        self.main_window.fps = self.interface_setting.video.fps
