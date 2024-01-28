from abc import ABC, abstractmethod

from pygame import Surface


class Data(ABC):

    @abstractmethod
    def start(self):
        ...