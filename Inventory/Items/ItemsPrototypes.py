from Inventory.Exception.ExceptionNotFoundName import ExceptionNotFoundName
from Inventory.Exception.ExceptionRepeatingName import ExceptionRepeatingName
import copy


class ItemsPrototypes:
    """item prototype catalog object"""

    def __init__(self) -> None:
        """init"""
        super().__init__()
        self.catalog: dict = {}

    def add(self, name, obj):
        """method for adding an object"""
        if name in self.catalog:
            raise ExceptionRepeatingName('this name already exists in the directory')

        self.catalog[name] = obj

    def get(self, name):
        """a method for retrieving an object based on a given object"""
        if not (name in self.catalog):
            raise ExceptionNotFoundName('this name is not found in the catalog')

        return copy.deepcopy(self.catalog[name])
