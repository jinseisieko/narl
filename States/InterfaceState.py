from abc import ABC, abstractmethod


class InterfaceState(ABC):
    def __init__(self, screen, game) -> None:
        super().__init__()
        self.type = ""
        self.game = game
        self.screen = screen

    @abstractmethod
    def update(self):
        ...

    @abstractmethod
    def check_events(self):
        ...

    @abstractmethod
    def start(self):
        ...
