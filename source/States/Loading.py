from threading import Thread

import pygame as pg

from source.Interface.LoadingTitle import LoadingTitle
from source.States.InterfaceState import InterfaceState

next = None


def build_next(cls, args, kwargs):
    _ = cls(*args, **kwargs)
    _.update()
    global next
    next = _


class Loading(InterfaceState):
    def __init__(self, screen, game, cls, *args, **kwargs) -> None:
        global next
        next = None
        super().__init__(screen, game)
        self.type = "Loading"
        self.title_loading = LoadingTitle(screen)
        t1 = Thread(target=build_next, args=(cls, args, kwargs))
        t1.start()

    def begin(self):
        pg.mouse.set_visible(False)

    def check_events(self, event):
        pass

    def update(self):
        if next is None:
            self.title_loading.update()
            self.title_loading.draw()
        else:
            self.game.set_state(next)
