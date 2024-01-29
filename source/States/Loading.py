from source.States.InterfaceState import InterfaceState
import pygame as pg
from source.Interface.LoadingTitle import LoadingTitle


class Loading(InterfaceState):
    def begin(self):
        pg.mouse.set_visible(False)

    def check_events(self, event):
        pass

    def update(self):
        self.title_loading.update()
        self.title_loading.draw()
        if not self.title_loading.video.active:
            self.game.set_state(self.next)

    def __init__(self, screen, game, next) -> None:
        super().__init__(screen, game)
        self.type = "Loading"
        self.title_loading = LoadingTitle(screen)
        self.next = next
        self.next.update()


