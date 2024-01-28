"""classes Obstacles"""
from source.Movable_objects.Entity import *


class Obstacle(Entity):
    def __init__(self, matrix: np.ndarray, Id: int, image: str, field, free_Ids: set, data=None):
        if data is not None:
            matrix[Id] = data
        super().__init__(matrix, Id, image, field, free_Ids)

        self.image.fill(image)
