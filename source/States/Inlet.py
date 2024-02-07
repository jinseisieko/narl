import numpy as np
import pygame as pg

from source.Interface.InletInterface import InletInterface
from source.States.InterfaceState import InterfaceState
from source.States.MainMenu import MainMenu


class Inlet(InterfaceState):
    def begin(self):
        pg.mouse.set_visible(True)
        self.main_window.fps = self.inlet_interface.video.fps

    def __init__(self, screen, game) -> None:
        super().__init__(screen, game)

        self.inlet_interface: InletInterface = InletInterface(self.screen)
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
                if self.inlet_interface.buttons["SignIn"].update(mouse_pos):
                    self.main_window.meta_player.register(self.inlet_interface.text_input1.get(),
                                                          self.inlet_interface.text_input2.get())
                    self.main_window.set_state(MainMenu(self.screen, self.main_window))
                # if self.title_screen.buttons["ContinueButton"].update(mouse_pos):
                #     self.game.change_state("MainGameMode", data=1)
                # if self.title_screen.buttons["StartButton"].update(mouse_pos):
                #     self.game.change_state("MainGameMode", data=0)
                # if self.title_screen.buttons["ArcadeButton"].update(mouse_pos):
                #     pass
                # if self.title_screen.buttons["SettingsButton"].update(mouse_pos):
                #     self.game.set_state(Settings(self.screen, self.game))
                # if self.title_screen.buttons["ExitButton"].update(mouse_pos):
                #     self.game.running = False
                #     time.sleep(0.2)
