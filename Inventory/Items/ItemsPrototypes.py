from Inventory.Exception.ExceptionNotFoundName import ExceptionNotFoundName
from Inventory.Exception.ExceptionRepeatingName import ExceptionRepeatingName
import copy

from Inventory.Items.Item import Item


class ItemsPrototypes:
    """item prototype catalog object"""

    def __init__(self) -> None:
        """init"""
        super().__init__()
        self.catalog: dict = {}

    def add(self, name, renewal_plus: dict, renewal_multiply: dict, renewal_super: dict, code: str) -> None:
        """method for adding an object"""
        if name in self.catalog:
            raise ExceptionRepeatingName('this name already exists in the directory')

        self.catalog[name] = Item(name=name, renewal_plus=renewal_plus, renewal_multiply=renewal_multiply,
                                  renewal_super=renewal_super, code=code)

    def get(self, name) -> Item:
        """a method for retrieving an object based on a given object"""
        if not (name in self.catalog):
            raise ExceptionNotFoundName('this name is not found in the catalog')

        return copy.deepcopy(self.catalog[name])
