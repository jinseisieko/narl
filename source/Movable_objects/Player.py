import pyganim as pga

from source.Constants import PLAYER_SLOWDOWN_FACTOR
from source.Image.Image import Image
from source.Inventory.Сharacteristics import Characteristics
from source.PlayerIndexes import *


class Player:
    def __init__(self, image, field) -> None:
        self.field = field
        self.characteristics = Characteristics()
        self.matrix = self.characteristics.characteristics
        self.image = Image(self.matrix[0][2], self.matrix[0][3], image)
        self.animate_damage = pga.PygAnimation((("resource/image/playerImages/damage1.png", 100),
                                                ("resource/image/playerImages/damage2.png", 100),
                                                ("resource/image/playerImages/damage3.png", 100),
                                                ("resource/image/playerImages/damage4.png", 100),
                                                ("resource/image/playerImages/damage5.png", 100)), loop=0)

    def draw(self) -> None:
        self.field.field.blit(self.image.img, (
            self.matrix[0, 0] - self.matrix[0, 2], self.matrix[0, 1] - self.matrix[0, 3]))
        self.animate_damage.blit(self.field.field, (
            self.matrix[0, 0] - self.matrix[0, 2], self.matrix[0, 1] - self.matrix[0, 3]))

    def add_item(self, name: str, rank: int) -> None:
        self.characteristics.apply(name, rank)
        self.update_characteristics()

    def update_characteristics(self):
        self.image.resize(self.matrix[0][size_x], self.matrix[0][size_y])
        self.matrix[0][delay] = max(0.01, self.matrix[0][delay])
        self.matrix[0][slowdown] = self.matrix[0][acceleration] * PLAYER_SLOWDOWN_FACTOR
        self.animate_damage.scale(*self.matrix[..., 2:4] * 2)

    def animate_damage_play(self):
        self.animate_damage.play()
