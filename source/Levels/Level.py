import numpy as np
import pygame as pg


class Portal:
    def __init__(self, matrix: np.ndarray):
        self.matrix: np.ndarray = matrix
        self.sprite = ...

    def draw(self, field):
        pg.draw.rect(field, "gold", (self.matrix[0], self.matrix[1], 2 * self.matrix[2], 2 * self.matrix[3]))


class Level:
    def __init__(self) -> None:
        self.background = []
        self.obstacles = None
        self.number = -1
        self.difficulty = 0
        self.enemies_types = (0, 1)
        self.count_waves = 1
        self.next = None
        self.name = None
        self.end = False


class Level1(Level):
    def __init__(self) -> None:
        super().__init__()

        self.background = ["grass1",
                           "grass2",
                           "grass3",
                           "grass4", ]
        self.number = 1
        self.difficulty = 1
        self.enemies_types = (0, 7)
        self.count_waves = 1
        self.next = Level2


class Level2(Level):
    def __init__(self) -> None:
        super().__init__()

        self.background = ['forest2'] * 20 + ['forest1',
                                              'forest2',
                                              'forest3',
                                              'forest4',
                                              'forest5',
                                              'forest6',
                                              'forest7',
                                              'forest8',
                                              'forest9',
                                              'forest10',
                                              'forest11',
                                              'forest12',
                                              'forest13',
                                              'forest14',
                                              'forest15',
                                              ]
        self.number = 2
        self.difficulty = 3
        self.enemies_types = (3, 5)
        self.count_waves = 10
        self.name = "forest"

        with open(f"resource/data/1414211.npy", "rb") as f:
            self.obstacles = np.load(f)

        self.next = Level3


class Level3(Level):
    def __init__(self) -> None:
        super().__init__()

        self.background = ["level3"]
        self.number = 2
        self.difficulty = 5
        self.enemies_types = (3, 5)
        self.count_waves = 17
        self.name = "red"

        with open(f"resource/data/2332311.npy", "rb") as f:
            self.obstacles = np.load(f)

        self.next = Level4


class Level4(Level):
    def __init__(self) -> None:
        super().__init__()

        self.background = ["level4"]
        self.number = 2
        self.difficulty = 6
        self.enemies_types = (3, 5)
        self.count_waves = 22

        self.next = Level5


class Level5(Level):
    def __init__(self) -> None:
        super().__init__()

        self.background = ['forest2']
        self.number = 2
        self.difficulty = 1
        self.enemies_types = (3, 5)
        self.count_waves = 1e99

        self.end = True
