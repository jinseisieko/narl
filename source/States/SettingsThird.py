from source.Functions.Functions import *
from source.Interface.SettingsInterfaceThird import SettingsInterfaceThird
from source.Interface.Video import Video
from source.States.InterfaceState import InterfaceState


class SettingsThird(InterfaceState):

    def __init__(self, screen, main_window, settings_container, video=Video("resource/video/gameplay1.mp4")) -> None:
        super().__init__(screen, main_window)
        self.main_window = main_window
        self.interface_setting = SettingsInterfaceThird(screen, video=video, container=settings_container)
        self.settings_container = settings_container
        self.begin()
        self.btn = -1

    def update(self):
        self.interface_setting.update()
        self.interface_setting.draw()

    def check_events(self, event):
        self.interface_setting.check_event(event)
        if self.btn != -1:
            if event.type == pg.KEYDOWN:
                x = event.key
                if get_key_code(x) is not None:
                    if self.btn == 0:
                        self.settings_container.buttons["MENU"] = x
                        self.interface_setting.menu_change_button.update_text(
                            get_key_code(x).replace("K_", "").upper())
                        self.btn = -1
                    if self.btn == 1:
                        self.settings_container.buttons["SHOOT"] = x
                        self.interface_setting.shoot_change_button.update_text(
                            get_key_code(x).replace("K_", "").upper())
                        self.btn = -1
                    if self.btn == 2:
                        self.settings_container.buttons["OPEN_CONSOLE"] = x
                        self.interface_setting.console_change_button.update_text(
                            get_key_code(x).replace("K_", "").upper())
                        self.btn = -1

        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                if self.interface_setting.button_back.update(pg.mouse.get_pos()):
                    self.main_window.change_state("SettingsSecond",
                                                  (self.settings_container, self.interface_setting.video))
                if self.interface_setting.button_exit.update(pg.mouse.get_pos()):
                    self.main_window.change_state("MainMenu")
                if self.interface_setting.button_apply.update(pg.mouse.get_pos()):
                    self.settings_container.update_settings()
                    self.main_window.change_state("MainMenu")
                if self.interface_setting.menu_change_button.update(pg.mouse.get_pos()):
                    self.btn = 0
                if self.interface_setting.shoot_change_button.update(pg.mouse.get_pos()):
                    self.btn = 1
                if self.interface_setting.console_change_button.update(pg.mouse.get_pos()):
                    self.btn = 2

    def begin(self):
        pg.mouse.set_visible(True)
        self.main_window.fps = self.interface_setting.video.fps
