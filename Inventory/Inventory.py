import numpy as np

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


class Inventory:
    def __init__(self) -> None:
        super().__init__()

        characteristics = np.zeros(12)


