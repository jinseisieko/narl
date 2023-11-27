"""class Player and additional functions"""
import math

import pygame.sprite

import Items


class Player(pygame.sprite.Sprite):
    """class Player"""

    def __init__(self) -> None:
        super().__init__()

        # values
        self.size: int = ...
        self.image: pygame.image = ...
        self.rect: pygame.Rect = self.image.get_rect()

        self.x: float = ...
        self.y: float = ...

        self.dx: float = 0.
        self.dy: float = 0.

        self.max_speed: float = ...
        self.max_hp: int = ...
        self.hp: int = ...

        self.period: int = ...
        self.projectile_range: float = ...
        self.projectile_speed: float = ...
        self.projectile_name_sprite: str = ...  # ключ от словаря спрайтов
        self.projectile_size: int = ...
        self.projectile_damage: int = ...

        self.projectile_ticks: int = math.ceil(self.projectile_range / self.projectile_speed) + 2
        self.projectile_trajectory: list[float] = [0.] * self.projectile_ticks

        self.items: list[Items.Item] = []

        # additional values
        ...

