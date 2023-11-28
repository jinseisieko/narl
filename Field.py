import pygame

from Constants import GRAY, FIELD_WIDTH, FIELD_HEIGHT


class Field:
    def __init__(self) -> None:
        # values
        self.field: pygame.surface = pygame.Surface((FIELD_WIDTH, FIELD_HEIGHT))
        self.field.fill(GRAY)
        # сделать его красивым

    def draw(self, *groups: pygame.sprite.Group) -> None:
        """draw groups in the sequence in which they are presented """

        self.field.fill(GRAY)
        for group in groups:
            group.draw(self.field)
