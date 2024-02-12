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
        self.catalog_blocked_blocking: dict = {}
        self.catalog_blocked_not_blocking: dict = {}

    def add_rank_1(self, id_: str, renewal_plus: dict, renewal_multiply: dict, renewal_super: dict, name: str = None,
                   description: str = None, code: str = '') -> Item:
        """method for adding an object"""
        if id_ in self.catalog_rank_1:
            raise ExceptionRepeatingName('this id_ already exists in the directory')
        item = Item(description=description, name=name, renewal_plus=renewal_plus,
                    renewal_multiply=renewal_multiply,
                    renewal_super=renewal_super, code=code, id_=id_)
        self.catalog_rank_1[id_] = item
        return item

    def add_rank_2(self, id_: str, renewal_plus: dict, renewal_multiply: dict, renewal_super: dict, name: str = None,
                   description: str = None, code: str = '') -> Item:
        """method for adding an object"""
        if id_ in self.catalog_rank_2:
            raise ExceptionRepeatingName('this id_ already exists in the directory')
        item = Item(description=description, name=name, renewal_plus=renewal_plus,
                    renewal_multiply=renewal_multiply,
                    renewal_super=renewal_super, code=code, id_=id_)
        self.catalog_rank_2[id_] = item
        return item

    def add_rank_3(self, id_: str, renewal_plus: dict, renewal_multiply: dict, renewal_super: dict, name: str = None,
                   description: str = None, code: str = '') -> Item:
        """method for adding an object"""
        if name in self.catalog_rank_3:
            raise ExceptionRepeatingName('this id_ already exists in the directory')
        item = Item(description=description, name=name, renewal_plus=renewal_plus,
                    renewal_multiply=renewal_multiply,
                    renewal_super=renewal_super, code=code, id_=id_)
        self.catalog_rank_3[id_] = item
        return item

    def add_blocked(self, id_: str, renewal_plus: dict, renewal_multiply: dict, renewal_super: dict, name: str = None,
                    description: str = None, code: str = '', blocking: bool = False):
        if blocking:
            if id_ in self.catalog_blocked_blocking:
                raise ExceptionRepeatingName('this id_ already exists in the directory')
            item = Item(description=description, name=name, renewal_plus=renewal_plus,
                        renewal_multiply=renewal_multiply,
                        renewal_super=renewal_super, code=code, id_=id_, blocking=blocking)
            self.catalog_blocked_blocking[id_] = item
        else:
            if id_ in self.catalog_blocked_not_blocking:
                raise ExceptionRepeatingName('this id_ already exists in the directory')
            item = Item(description=description, name=name, renewal_plus=renewal_plus,
                        renewal_multiply=renewal_multiply,
                        renewal_super=renewal_super, code=code, id_=id_, blocking=blocking)
            self.catalog_blocked_not_blocking[id_] = item

    def add(self, rank, id_: str, renewal_plus: dict, renewal_multiply: dict, renewal_super: dict, name: str = None,
            description: str = None, code: str = '', blocking: bool = False):
        if rank == 1:
            return self.add_rank_1(id_, renewal_plus, renewal_multiply, renewal_super, name, description, code)
        if rank == 2:
            return self.add_rank_2(id_, renewal_plus, renewal_multiply, renewal_super, name, description, code)
        if rank == 3:
            return self.add_rank_3(id_, renewal_plus, renewal_multiply, renewal_super, name, description, code)
        if rank == -1:
            return self.add_blocked(id_, renewal_plus, renewal_multiply, renewal_super, name, description, code,
                                    blocking)

    def get(self, id_, rank) -> Item:
        """a method for retrieving an object based on a given object"""
        if rank == 1:
            if not (id_ in self.catalog_rank_1):
                raise ExceptionNotFoundName(f'this id_ is not found in the catalog_rank_1: {id_}')

            return copy.deepcopy(self.catalog_rank_1[id_])

        if rank == 2:
            if not (id_ in self.catalog_rank_2):
                raise ExceptionNotFoundName(f'this id_ is not found in the catalog_rank_2: {id_}')

            return copy.deepcopy(self.catalog_rank_2[id_])

        if rank == 3:
            if not (id_ in self.catalog_rank_3):
                raise ExceptionNotFoundName(f'this id_ is not found in the catalog_rank_3: {id_}')

            return copy.deepcopy(self.catalog_rank_3[id_])
