from abc import ABC, abstractmethod


class InterfaceState(ABC):
    def __init__(self, screen, main_window) -> None:
        super().__init__()
        self.type = ""
        self.main_window = main_window
        self.screen = screen


    @abstractmethod
    def update(self):
        ...

    @abstractmethod
    def check_events(self, event):
        ...

    @abstractmethod
    def begin(self):
        ...
