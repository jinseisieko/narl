import pygame as pg

from Inventory.Сharacteristics import Characteristics


class Player:
    def __init__(self, image: str, field) -> None:
        self.image: str = image
        self.field = field
        self.characteristics = Characteristics()
        self.matrix = self.characteristics.characteristics
        self.image = pg.Surface((2 * self.matrix[0, 2], 2 * self.matrix[0, 3]))
        self.image.fill((0, 0, 255))

    def draw(self) -> None:
        self.field.field.blit(self.image, (
            self.matrix[0, 0] - self.matrix[0, 2], self.matrix[0, 1] - self.matrix[0, 3]))
