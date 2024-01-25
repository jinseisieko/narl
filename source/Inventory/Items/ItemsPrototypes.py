import copy

from source.Inventory.Exception.ExceptionNotFoundName import ExceptionNotFoundName
from source.Inventory.Exception.ExceptionRepeatingName import ExceptionRepeatingName
from source.Inventory.Items.Item import Item


class ItemsPrototypes:
    """item prototype catalog object"""

    def __init__(self) -> None:
        """init"""
        super().__init__()
        self.catalog_rank_1: dict = {}
        self.catalog_rank_2: dict = {}
        self.catalog_rank_3: dict = {}

    def add_rank_1(self, name, renewal_plus: dict, renewal_multiply: dict, renewal_super: dict, code: str) -> Item:
        """method for adding an object"""
        if name in self.catalog_rank_1:
            raise ExceptionRepeatingName('this name already exists in the directory')
        item = Item(name=name, renewal_plus=renewal_plus, renewal_multiply=renewal_multiply,
                    renewal_super=renewal_super, code=code)
        self.catalog_rank_1[name] = item
        return item

    def add_rank_2(self, name, renewal_plus: dict, renewal_multiply: dict, renewal_super: dict, code: str) -> Item:
        """method for adding an object"""
        if name in self.catalog_rank_2:
            raise ExceptionRepeatingName('this name already exists in the directory')
        item = Item(name=name, renewal_plus=renewal_plus, renewal_multiply=renewal_multiply,
                    renewal_super=renewal_super, code=code)
        self.catalog_rank_2[name] = item
        return item

    def add_rank_3(self, name, renewal_plus: dict, renewal_multiply: dict, renewal_super: dict, code: str) -> Item:
        """method for adding an object"""
        if name in self.catalog_rank_3:
            raise ExceptionRepeatingName('this name already exists in the directory')
        item = Item(name=name, renewal_plus=renewal_plus, renewal_multiply=renewal_multiply,
                    renewal_super=renewal_super, code=code)
        self.catalog_rank_3[name] = item
        return item

    def add(self, name, rank, renewal_plus: dict, renewal_multiply: dict, renewal_super: dict, code: str):
        if rank == 1:
            return self.add_rank_1(name, renewal_plus, renewal_multiply, renewal_super, code)
        if rank == 2:
            return self.add_rank_2(name, renewal_plus, renewal_multiply, renewal_super, code)
        if rank == 3:
            return self.add_rank_3(name, renewal_plus, renewal_multiply, renewal_super, code)

    def get(self, name, rank) -> Item:
        """a method for retrieving an object based on a given object"""
        if rank == 1:
            if not (name in self.catalog_rank_1):
                raise ExceptionNotFoundName(f'this name is not found in the catalog_rank_1: {name}')

            return copy.deepcopy(self.catalog_rank_1[name])

        if rank == 2:
            if not (name in self.catalog_rank_2):
                raise ExceptionNotFoundName(f'this name is not found in the catalog_rank_2: {name}')

            return copy.deepcopy(self.catalog_rank_2[name])

        if rank == 3:
            if not (name in self.catalog_rank_3):
                raise ExceptionNotFoundName(f'this name is not found in the catalog_rank_3: {name}')

            return copy.deepcopy(self.catalog_rank_3[name])
