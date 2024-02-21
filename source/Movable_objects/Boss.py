"""classes Enemy"""
import pygame

from source.Image.Image import Image
from source.Movable_objects.Entity import *


class Boss:
    def __init__(self, matrix: np.ndarray, image: str) -> None:
        self.matrix: np.ndarray = matrix
        self.image: Image = pygame.Surface((int(self.matrix[0, 2] * 2), int(self.matrix[0, 3] * 2)))
        self.image.fill("red")

    def draw(self, field) -> None:
        print("BOSS")
        pygame.draw.rect(field, "red", (
            self.matrix[0, 0] - self.matrix[0, 2], self.matrix[0, 1] - self.matrix[0, 3], self.matrix[0, 3] * 2,
            self.matrix[0, 3] * 2))
