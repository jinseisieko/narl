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

        self.characteristics: np.array = np.array([[1000, 1000, 40, 40, 0, 0, 0, 0, 500, 600, 1500, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 5]],
                               dtype=np.float_)
        self.item_names: list = []
        self.itemsPrototypes = ItemsPrototypes()
        self.init_prototype(["original.db"] + self.mods)

    def apply(self, name: str) -> None:
        new_characteristics: dict = self.itemsPrototypes.get(name).apply(x=self.characteristics[x],
                                                                         y=self.characteristics[y],
                                                                         size_x=self.characteristics[size_x],
                                                                         size_y=self.characteristics[size_y],
                                                                         hp=self.characteristics[hp],
                                                                         vx=self.characteristics[vx],
                                                                         vy=self.characteristics[vy],
                                                                         max_velocity=self.characteristics[
                                                                             max_velocity],
                                                                         slowdown=self.characteristics[slowdown],
                                                                         acceleration=self.characteristics[
                                                                             acceleration],
                                                                         max_hp=self.characteristics[max_hp],
                                                                         armor=self.characteristics[armor],
                                                                         delay=self.characteristics[delay],
                                                                         armor_piercing=self.characteristics[
                                                                             armor_piercing],
                                                                         bullet_size_x=self.characteristics[
                                                                             bullet_size_x],
                                                                         bullet_size_y=self.characteristics[
                                                                             bullet_size_y],
                                                                         bullet_damage=self.characteristics[
                                                                             bullet_damage],
                                                                         critical_coefficient=self.characteristics[
                                                                             critical_coefficient],
                                                                         critical_chance=self.characteristics[
                                                                             critical_chance],
                                                                         scatter=self.characteristics[scatter],
                                                                         life_time=self.characteristics[life_time])

        for key, value in new_characteristics.items():
            print(key, value)
            exec(f"self.characteristics[{key}] = {value}")

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


