import random

import pygame

import ImageSprites
from Constants import GRAY, FIELD_WIDTH, FIELD_HEIGHT, GREEN


class Field:
    def __init__(self) -> None:
        # values
        self.field: pygame.surface = pygame.Surface((FIELD_WIDTH, FIELD_HEIGHT))

        self.background = pygame.surface = pygame.Surface((FIELD_WIDTH, FIELD_HEIGHT))
        self.background.fill((158, 240, 144))
        for _ in range(500000):
            if random.choice([True] * 5 + [False]):
                number_image_grass = random.randint(1, 5)
                self.background.blit(ImageSprites.sprites[f"grass{number_image_grass}"],
                                     (random.randint(-15, FIELD_WIDTH +15), random.randint(-15, FIELD_HEIGHT +15)))
            else:
                number_image_stone = random.randint(1, 1)
                self.background.blit(ImageSprites.sprites[f"stone{number_image_stone}"],
                                     (random.randint(-15, FIELD_WIDTH + 15), random.randint(-15, FIELD_HEIGHT +15)))

        self.field.blit(self.background, (0, 0))
        # сделать его красивым

    def draw(self, *groups: pygame.sprite.Group) -> None:
        """draw groups in the sequence in which they are presented """
        self.field.blit(self.background, (0, 0))
        for group in groups:
            group.draw(self.field)
