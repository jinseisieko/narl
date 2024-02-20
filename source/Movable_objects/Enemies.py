"""classes Enemy"""
from source.Image.Image import Image
from source.Image.InitializationForGame import get_images_for_game
from source.Movable_objects.Entity import *


class Enemy(Entity):
    def __init__(self, matrix: np.ndarray, Id: int, image: str, free_Ids: set):
        super().__init__(matrix, Id, image, free_Ids)
        self.image: Image = Image(int(self.matrix[self.Id, 2]), int(self.matrix[self.Id, 3]),
                                  get_images_for_game()["test_enemy"])

    def draw(self, field) -> None:
        field.blit(self.image.img, (
            self.matrix[self.Id, X] - self.matrix[self.Id, SIZE_X],
            self.matrix[self.Id, Y] - self.matrix[self.Id, SIZE_Y]))