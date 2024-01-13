import json
import sqlite3 as sql

import numpy as np

from Calculations.Data import player
from Inventory.Items.ItemsPrototypes import ItemsPrototypes

from PlayerIndexes import *


class Characteristics:
    def __init__(self, mods: (list, None) = None) -> None:
        super().__init__()

        if mods is None:
            self.mods = []
        else:
            self.mods: list = mods

        self.characteristics: np.array = player
        self.item_names: list = []
        self.itemsPrototypes = ItemsPrototypes()
        self.init_prototype(["original.db"] + self.mods)

    def apply(self, name: str, rang: int) -> None:
        new_characteristics: dict = self.itemsPrototypes.get(name, rang).apply(x=self.characteristics[0][x],
                                                                               y=self.characteristics[0][y],
                                                                               size_x=self.characteristics[0][size_x],
                                                                               size_y=self.characteristics[0][size_y],
                                                                               hp=self.characteristics[0][hp],
                                                                               vx=self.characteristics[0][vx],
                                                                               vy=self.characteristics[0][vy],
                                                                               max_velocity=self.characteristics[0][
                                                                                   max_velocity],
                                                                               slowdown=self.characteristics[0][
                                                                                   slowdown],
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
                                                                               critical_coefficient=
                                                                               self.characteristics[0][
                                                                                   critical_coefficient],
                                                                               critical_chance=self.characteristics[0][
                                                                                   critical_chance],
                                                                               scatter=self.characteristics[0][scatter],
                                                                               bullet_life_time=self.characteristics[0][
                                                                                   bullet_life_time],
                                                                               bullet_velocity=self.characteristics[0][
                                                                                   bullet_velocity],
                                                                               damage_delay=self.characteristics[0][
                                                                                   damage_delay])

        for key, value in new_characteristics.items():
            exec(f"self.characteristics[0][{key}] = {value}")

    def init_prototype(self, db_names: list) -> None:
        for name_db in db_names:
            con = sql.connect(f"Inventory/ItemDatabase/{name_db}")
            cur = con.cursor()
            for i in range(1, 4):
                for name_, renewal_plus_, renewal_multiply_, renewal_super_, code_ in cur.execute(
                        f"""SELECT * FROM rang{i}"""):
                    renewal_plus = json.loads(renewal_plus_)
                    renewal_multiply = json.loads(renewal_multiply_)
                    renewal_super = json.loads(renewal_super_)
                    self.itemsPrototypes.add(name_, i, renewal_plus, renewal_multiply, renewal_super, code_)
