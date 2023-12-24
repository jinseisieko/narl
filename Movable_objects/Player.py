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


class Player:
    def __init__(self, image: str, field) -> None:
        self.image: str = image
        self.field = field
        self.matrix = np.array([1000, 1000, 250, 100, 0, 0, 0, 0, 500, 600, 1500, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
                               dtype=np.float_)
        self.image = pg.Surface((2 * self.matrix[2], 2 * self.matrix[3]))
        self.image.fill((0, 0, 255))

    def draw(self) -> None:
        self.field.field.blit(self.image, (self.matrix[X] + self.matrix[SIZE_X], self.matrix[Y] + self.matrix[SIZE_Y]))
