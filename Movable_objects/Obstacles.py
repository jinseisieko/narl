"""classes Obstacles"""
from Movable_objects.Entity import *


class Obstacle(Entity):
    def __init__(self, data: np.array, matrix: np.ndarray, Id: int, image: str, field,
                 free_Ids: set):
        super().__init__(data, matrix, Id, image, field, free_Ids)
