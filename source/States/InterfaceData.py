from abc import ABC, abstractmethod


class Data(ABC):

    @abstractmethod
    def start(self):
        ...
