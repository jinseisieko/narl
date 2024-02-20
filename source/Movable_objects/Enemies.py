"""classes Enemy"""
from source.Image.Image import Image
from source.Image.InitializationForGame import get_images_for_game
from source.Movable_objects.Entity import *


class Enemy(Entity):
    def __init__(self, matrix: np.ndarray, Id: int, image: str, free_Ids: set):
        super().__init__(matrix, Id, image, free_Ids)
        self.image: Image = Image(int(self.matrix[self.Id, 2]), int(self.matrix[self.Id, 3]),
                                  get_images_for_game()[int(self.matrix[self.Id, 12])])

    def draw(self, field) -> None:
        field.blit(self.image.img, (
            self.matrix[self.Id, 0] - self.matrix[self.Id, 2],
            self.matrix[self.Id, 1] - self.matrix[self.Id, 3]))