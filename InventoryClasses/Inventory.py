import json

import numpy as np
import sqlite3 as sql
from InventoryClasses.Items.ItemsPrototypes import ItemsPrototypes

size = 0
speed = 1
hp_max = 2
hp = 3
armor = 4
pierce_armor = 5
period = 6
bullet_size = 7
bullet_damage = 8
bullet_speed = 9
critical_damage_multiplier = 10
chance_critical_damage = 11
scatter = 12


class Inventory:
    def __init__(self, mods: (list, None) = None) -> None:
        super().__init__()

        if mods is None:
            self.mods = []
        else:
            self.mods: list = mods

        self.characteristics: np.array = np.zeros(13)
        self.item_names: list = []
        self.itemsPrototypes = ItemsPrototypes()
        self.init_prototype(["original.db"] + self.mods)

    def apply(self, name: str) -> None:
        ...

    def init_prototype(self, db_names: list) -> None:
        for name_db in db_names:
            con = sql.connect(f"ItemDatabase/{name_db}")
            cur = con.cursor()
            for name_, renewal_plus_, renewal_multiply_, renewal_super_, code_ in cur.execute(
                    """SELECT * FROM items"""):
                renewal_plus = json.loads(renewal_plus_)
                renewal_multiply = json.loads(renewal_multiply_)
                renewal_super = json.loads(renewal_super_)
                self.itemsPrototypes.add(name_, renewal_plus, renewal_multiply, renewal_super, code_)


if __name__ == '__main__':
    a = Inventory()
    print(a.itemsPrototypes.catalog)
