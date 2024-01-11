import random

import numba
import pygame as pg

from Constants import *


class Field:
    def __init__(self, data: np.ndarray) -> None:
        self.data: np.ndarray = data
        self.field: pygame.surface = pygame.Surface((0, 0))
        self.background: pygame.surface = pygame.Surface((FIELD_WIDTH, FIELD_HEIGHT))
        for i in numba.prange(FIELD_WIDTH // BACKGROUND_PICTURE_SIZE + 1):
            for j in numba.prange(FIELD_HEIGHT // BACKGROUND_PICTURE_SIZE + 1):
                self.background.blit(pygame.image.load(f"image/grasses/grass{random.randint(1, 4)}.png"),
                                     (i * BACKGROUND_PICTURE_SIZE, j * BACKGROUND_PICTURE_SIZE))

        self.background = pg.transform.scale(self.background.convert(), (FIELD_WIDTH, FIELD_HEIGHT))
        self.field = pg.transform.scale(self.field.convert(), (FIELD_WIDTH, FIELD_HEIGHT))

    def draw(self):
        self.field.blit(self.background, self.data[4:6], pygame.Rect(self.data[([4, 5, 8, 9])]))
