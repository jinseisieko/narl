import numpy as np
import pygame as pg

X = 0
Y = 1
SIZE_X = 2
SIZE_Y = 3
VX = 4
VY = 5
HP = 6
DAMAGE = 7


class Entity:
    def __init__(self, data: np.array, matrix: np.ndarray, Id: int, image: str, field,
                 free_Ids: set) -> None:
        self.matrix: np.ndarray = matrix
        self.Id: int = Id
        self.matrix[Id] = data
        self.image: pg.Surface = pg.Surface((2 * data[2], 2 * data[3]))
        self.image.fill(image)
        self.field = field
        self.free_Ids = free_Ids

    def draw(self) -> None:
        self.field.field.blit(self.image, (
            self.matrix[self.Id, 0] - self.matrix[self.Id, 2],
            self.matrix[self.Id, 1] - self.matrix[self.Id, 3]))

    def kill(self) -> None:
        self.free_Ids.add(self.Id)
