import numpy as np
import pygame as pg


class Entity:
    def __init__(self, matrix: np.ndarray, Id: int, image: str, free_Ids: set) -> None:
        self.matrix: np.ndarray = matrix
        self.Id: int = Id
        self.image: pg.Surface = pg.Surface((2 * matrix[Id, 2], 2 * matrix[Id, 3]))
        self.free_Ids = free_Ids

    def draw(self, field) -> None:
        field.blit(self.image, (
            self.matrix[self.Id, 0] - self.matrix[self.Id, 2],
            self.matrix[self.Id, 1] - self.matrix[self.Id, 3]))

    def kill(self) -> None:
        self.free_Ids.add(self.Id)
