from abc import ABC, abstractmethod


class Data(ABC):
    """Data interface that is needed for pauses"""
    @abstractmethod
    def start(self):
        """"""
        ...
