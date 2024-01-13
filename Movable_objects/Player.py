from Image import Image
from Inventory.Сharacteristics import Characteristics
from PlayerIndexes import *


class Player:
    def __init__(self, image: str, field) -> None:
        self.image: str = image
        self.field = field
        self.characteristics = Characteristics()
        self.matrix = self.characteristics.characteristics
        self.image = Image(self.matrix[0][2], self.matrix[0][3], self.image)
        print(self.matrix[0][2], self.matrix[0][3])

    def draw(self) -> None:
        self.field.field.blit(self.image.img, (
            self.matrix[0, 0] - self.matrix[0, 2], self.matrix[0, 1] - self.matrix[0, 3]))

    def add_item(self, name, rang):
        self.characteristics.apply(name, rang)
        self.image.resize(self.matrix[0][size_x], self.matrix[0][size_y])
