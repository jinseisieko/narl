import json
import sqlite3 as sql

import numpy as np

from Inventory.Items.ItemsPrototypes import ItemsPrototypes

# name value in array
x = 0
y = 1
size_x = 2
size_y = 3
hp = 4
_ = 5
vx = 6
vy = 7
max_velocity = 8
slowdown = 9
acceleration = 10
max_hp = 11
armor = 12
delay = 13
armor_piercing = 14
bullet_size_x = 15
bullet_size_y = 16
bullet_damage = 17
critical_coefficient = 18
critical_chance = 19
scatter = 20
life_time = 21


class Characteristics:
    def __init__(self, mods: (list, None) = None) -> None:
        super().__init__()

        if mods is None:
            self.mods = []
        else:
            self.mods: list = mods

        self.characteristics: np.array = np.array(
            [[1000, 1000, 40, 40, 0, 0, 0, 0, 500, 600, 1500, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5]],
            dtype=np.float_)
        self.item_names: list = []
        self.itemsPrototypes = ItemsPrototypes()
        self.init_prototype(["original.db"] + self.mods)

    def apply(self, name: str) -> None:
        new_characteristics: dict = self.itemsPrototypes.get(name).apply(x=self.characteristics[0][x],
                                                                         y=self.characteristics[0][y],
                                                                         size_x=self.characteristics[0][size_x],
                                                                         size_y=self.characteristics[0][size_y],
                                                                         hp=self.characteristics[0][hp],
                                                                         _=self.characteristics[0][_],
                                                                         vx=self.characteristics[0][vx],
                                                                         vy=self.characteristics[0][vy],
                                                                         max_velocity=self.characteristics[0][
                                                                             max_velocity],
                                                                         slowdown=self.characteristics[0][slowdown],
                                                                         acceleration=self.characteristics[0][
                                                                             acceleration],
                                                                         max_hp=self.characteristics[0][max_hp],
                                                                         armor=self.characteristics[0][armor],
                                                                         delay=self.characteristics[0][delay],
                                                                         armor_piercing=self.characteristics[0][
                                                                             armor_piercing],
                                                                         bullet_size_x=self.characteristics[0][
                                                                             bullet_size_x],
                                                                         bullet_size_y=self.characteristics[0][
                                                                             bullet_size_y],
                                                                         bullet_damage=self.characteristics[0][
                                                                             bullet_damage],
                                                                         critical_coefficient=self.characteristics[0][
                                                                             critical_coefficient],
                                                                         critical_chance=self.characteristics[0][
                                                                             critical_chance],
                                                                         scatter=self.characteristics[0][scatter],
                                                                         life_time=self.characteristics[0][life_time])

        for key, value in new_characteristics.items():
            exec(f"self.characteristics[0][{key}] = {value}")

    def init_prototype(self, db_names: list) -> None:
        for name_db in db_names:
            con = sql.connect(f"Inventory/ItemDatabase/{name_db}")
            cur = con.cursor()
            for name_, renewal_plus_, renewal_multiply_, renewal_super_, code_ in cur.execute(
                    """SELECT * FROM items"""):
                renewal_plus = json.loads(renewal_plus_)
                renewal_multiply = json.loads(renewal_multiply_)
                renewal_super = json.loads(renewal_super_)
                self.itemsPrototypes.add(name_, renewal_plus, renewal_multiply, renewal_super, code_)
