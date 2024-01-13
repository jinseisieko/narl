from Inventory.Exception.ExceptionNotFoundName import ExceptionNotFoundName
from Inventory.Exception.ExceptionRepeatingName import ExceptionRepeatingName
import copy

from Inventory.Items.Item import Item


class ItemsPrototypes:
    """item prototype catalog object"""

    def __init__(self) -> None:
        """init"""
        super().__init__()
        self.catalog_rang_1: dict = {}
        self.catalog_rang_2: dict = {}
        self.catalog_rang_3: dict = {}

    def add_rang_1(self, name, renewal_plus: dict, renewal_multiply: dict, renewal_super: dict, code: str) -> None:
        """method for adding an object"""
        if name in self.catalog_rang_1:
            raise ExceptionRepeatingName('this name already exists in the directory')

        self.catalog_rang_1[name] = Item(name=name, renewal_plus=renewal_plus, renewal_multiply=renewal_multiply,
                                         renewal_super=renewal_super, code=code)

    def add_rang_2(self, name, renewal_plus: dict, renewal_multiply: dict, renewal_super: dict, code: str) -> None:
        """method for adding an object"""
        if name in self.catalog_rang_2:
            raise ExceptionRepeatingName('this name already exists in the directory')

        self.catalog_rang_2[name] = Item(name=name, renewal_plus=renewal_plus, renewal_multiply=renewal_multiply,
                                         renewal_super=renewal_super, code=code)

    def add_rang_3(self, name, renewal_plus: dict, renewal_multiply: dict, renewal_super: dict, code: str) -> None:
        """method for adding an object"""
        if name in self.catalog_rang_3:
            raise ExceptionRepeatingName('this name already exists in the directory')

        self.catalog_rang_3[name] = Item(name=name, renewal_plus=renewal_plus, renewal_multiply=renewal_multiply,
                                         renewal_super=renewal_super, code=code)

    def add(self, name, rang, renewal_plus: dict, renewal_multiply: dict, renewal_super: dict, code: str):
        if rang == 1:
            self.add_rang_1(name, renewal_plus, renewal_multiply, renewal_super, code)
        if rang == 2:
            self.add_rang_2(name, renewal_plus, renewal_multiply, renewal_super, code)
        if rang == 3:
            self.add_rang_3(name, renewal_plus, renewal_multiply, renewal_super, code)

    def get(self, name, rang) -> Item:
        """a method for retrieving an object based on a given object"""
        if rang == 1:
            if not (name in self.catalog_rang_1):
                raise ExceptionNotFoundName('this name is not found in the catalog')

            return copy.deepcopy(self.catalog_rang_1[name])

        if rang == 2:
            if not (name in self.catalog_rang_2):
                raise ExceptionNotFoundName('this name is not found in the catalog')

            return copy.deepcopy(self.catalog_rang_2[name])

        if rang == 3:
            if not (name in self.catalog_rang_3):
                raise ExceptionNotFoundName('this name is not found in the catalog')

            return copy.deepcopy(self.catalog_rang_3[name])
