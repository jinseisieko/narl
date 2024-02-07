from source.Interface.NewItemInterface import NewItemInterface
from source.States.InterfaceState import InterfaceState
import pygame as pg
import numpy as np


class NewItem(InterfaceState):
    def begin(self):
        pg.mouse.set_visible(True)

    def check_events(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                mouse_pos = np.array(pg.mouse.get_pos())
                if self.new_item_pause.buttons["ItemButton1"].update(mouse_pos):
                    self.data.player.characteristics.apply(self.new_item_pause.random_item1, self.new_item_pause.rank1)
                    self.data.start()
                    self.main_window.set_state(self.data)

                if self.new_item_pause.buttons["ItemButton2"].update(mouse_pos):
                    self.data.player.characteristics.apply(self.new_item_pause.random_item2, self.new_item_pause.rank2)
                    self.data.start()
                    self.main_window.set_state(self.data)
                if self.new_item_pause.buttons["ItemButton3"].update(mouse_pos):
                    self.data.player.characteristics.apply(self.new_item_pause.random_item3, self.new_item_pause.rank3)
                    self.data.start()
                    self.main_window.set_state(self.data)
                self.data.player.update_characteristics()

    def update(self):
        self.new_item_pause.update()
        self.new_item_pause.draw()

    def __init__(self, screen, game, last_, last_frame) -> None:
        super().__init__(screen, game)
        self.data = last_
        self.new_item_pause = NewItemInterface(self.screen, last_frame, last_)
        self.begin()
