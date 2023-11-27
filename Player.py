"""class Player and additional functions"""
import math

import pygame.sprite

import ImageSprites
from Constants import *

import Items


class Player(pygame.sprite.Sprite):
    """class Player"""

    def __init__(self) -> None:
        super().__init__()

        # values
        self.size: int = PLAYER_SIZE
        self.image: pygame.image = ImageSprites.sprites["player"]
        self.rect: pygame.Rect = self.image.get_rect()

        self.x: float = FIELD_HEIGHT / 2
        self.y: float = FIELD_WIDTH / 2

        self.dx: float = 0.
        self.dy: float = 0.

        self.max_speed: float = DEFAULT_PLAYER_SPEED
        self.max_hp: int = DEFAULT_PLAYER_HP
        self.hp: int = DEFAULT_PLAYER_HP

        self.period: int = DEFAULT_PROJECTILE_PERIOD
        self.projectile_range: float = DEFAULT_PROJECTILE_RANGE
        self.projectile_speed: float = DEFAULT_PROJECTILE_SPEED
        self.projectile_size: int = DEFAULT_PROJECTILE_SIZE
        self.projectile_damage: int = DEFAULT_PROJECTILE_DAMAGE
        self.projectile_name_sprite: str = "default_projectile"

        self.projectile_ticks: int = math.ceil(self.projectile_range / self.projectile_speed) + 2
        self.projectile_trajectory: list[float] = [0.] * self.projectile_ticks

        self.items: list[Items.Item] = []

        # additional values
        ...
