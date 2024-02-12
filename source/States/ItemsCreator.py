import pygame as pg

from source.Interface.ItemsCreatorInterface import ItemsCreatorInterface
from source.States.InterfaceState import InterfaceState


class ItemsCreator(InterfaceState):

    def begin(self):
        pg.mouse.set_visible(True)

    def __init__(self, screen, main_window) -> None:
        super().__init__(screen, main_window)
        self.screen = screen
        self.main_window = main_window
        self.itemsCreator_interface = ItemsCreatorInterface(screen)

    def update(self):
        self.itemsCreator_interface.update()
        self.itemsCreator_interface.draw()

    def check_events(self, event):
        self.itemsCreator_interface.check_event(event)
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                if self.itemsCreator_interface.button_exit.update(pg.mouse.get_pos()):
                    self.main_window.change_state("MainMenu")
