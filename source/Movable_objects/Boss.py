"""classes Enemy"""
from source.Image.Image import Image
from source.Image.InitializationForGame import get_images_for_game
from source.Movable_objects.Entity import *


class Boss:
    def __init__(self, matrix: np.ndarray, image: str) -> None:
        self.matrix: np.ndarray = matrix
        self.image: pg.Surface = pg.Surface((2 * matrix[0, 2], 2 * matrix[0, 3]))
        self.image: Image = Image(int(self.matrix[0, 2]), int(self.matrix[0, 3]),
                                  get_images_for_game()[image])

    def draw(self, field) -> None:
        field.blit(self.image.img, (
            self.matrix[0, 0] - self.matrix[0, 2],
            self.matrix[0, 1] - self.matrix[0, 3]))
