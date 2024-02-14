"""classes Obstacles"""
from source.Image.InitializationForGame import get_images_for_game
from source.Movable_objects.Entity import *


class Obstacle(Entity):
    def __init__(self, matrix: np.ndarray, Id: int, image, free_Ids: set, data=None):
        if data is not None:
            matrix[Id] = data
        super().__init__(matrix, Id, image, free_Ids)
        if image != "red":
            self.image = pg.transform.scale(get_images_for_game()[image], (int(matrix[Id][2] * 2), int(matrix[Id][3] * 2)))
        else:
            self.image.fill(image)
