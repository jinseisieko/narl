import json

import numpy as np

from source.Calculations.Data import player
from source.Constants import NUMBER_OF_ITEMS
from source.Inventory.GetItem import GetItems
from source.Inventory.Items.ItemModel import DB, ItemsRank1, ItemsRank2, ItemsRank3, ItemsBlocked
from source.Inventory.Items.ItemsPrototypes import ItemsPrototypes
from source.PlayerIndexes import *


class Characteristics:
    def __init__(self, mods: (list, None) = None) -> None:
        super().__init__()

        if mods is None:
            self.mods = []
        else:
            self.mods: list = mods

        self.characteristics: np.array = player
        self.item_names: list = []
        self.array_draw: list = []
        self.itemsPrototypes = ItemsPrototypes()
        self.getitem = GetItems()
        self.init_prototype()

    def update_array_draw(self):
        self.array_draw: list[str] = []
        for i in range(len(self.item_names) // NUMBER_OF_ITEMS):
            self.array_draw += [self.item_names[i * NUMBER_OF_ITEMS:i * NUMBER_OF_ITEMS + NUMBER_OF_ITEMS]]
        if len(self.item_names) % NUMBER_OF_ITEMS != 0:
            self.array_draw += [self.item_names[-(len(self.item_names) % NUMBER_OF_ITEMS):]]

    def apply(self, id_: str, rank: int) -> None:
        self.item_names.append(id_)
        self.update_array_draw()
        new_characteristics: dict = self.itemsPrototypes.get(id_, rank).apply(x=self.characteristics[0][x],
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
                                                                                   damage_delay],
                                                                              bullet_bouncing=self.characteristics[0][
                                                                                   bullet_bouncing])

        for key, value in new_characteristics.items():
            exec(f"self.characteristics[0][{key}] = {value}")

        print(id_)

    def init_prototype(self) -> None:
        with DB.atomic():
            select_ = ItemsRank1.select()
            for item in select_:
                self.getitem.add(item.id, 1)
                self.itemsPrototypes.add(1, item.id, renewal_plus=json.loads(item.renewal_plus),
                                         renewal_multiply=json.loads(item.renewal_multiply),
                                         renewal_super=json.loads(item.renewal_super), name=item.name,
                                         description=item.description, code=item.code, blocking=False)

            select_ = ItemsRank2.select()
            for item in select_:
                self.getitem.add(item.id, 2)
                self.itemsPrototypes.add(2, item.id, renewal_plus=json.loads(item.renewal_plus),
                                         renewal_multiply=json.loads(item.renewal_multiply),
                                         renewal_super=json.loads(item.renewal_super), name=item.name,
                                         description=item.description, code=item.code, blocking=False)

            select_ = ItemsRank3.select()
            for item in select_:
                self.getitem.add(item.id, 3)
                self.itemsPrototypes.add(3, item.id, renewal_plus=json.loads(item.renewal_plus),
                                         renewal_multiply=json.loads(item.renewal_multiply),
                                         renewal_super=json.loads(item.renewal_super), name=item.name,
                                         description=item.description, code=item.code, blocking=False)

            select_ = ItemsBlocked.select()
            for item in select_:
                self.getitem.add(item.id, -1)
                self.itemsPrototypes.add(-1, item.id, renewal_plus=json.loads(item.renewal_plus),
                                         renewal_multiply=json.loads(item.renewal_multiply),
                                         renewal_super=json.loads(item.renewal_super), name=item.name,
                                         description=item.description, code=item.code, blocking=item.blocking)
