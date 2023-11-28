"""class Player and additional functions"""
import math

import pygame.sprite

import ImageSprites
import Items
from Constants import *


def field_boundary_collision(x: float, y: float) -> tuple[float, float]:
    """function is designed to change coordinates when colliding with a boundary"""

    if x > FIELD_WIDTH - PLAYER_SIZE:
        x = FIELD_WIDTH - PLAYER_SIZE
    elif x < 0:
        x = 0.

    if y > FIELD_HEIGHT - PLAYER_SIZE:
        y = FIELD_HEIGHT - PLAYER_SIZE
    elif y < 0:
        y = 0

    return x, y


class Player(pygame.sprite.Sprite):
    """class Player"""

    def __init__(self) -> None:
        super().__init__()

        # values
        self.size: int = PLAYER_SIZE
        self.image: pygame.image = pygame.image.load(ImageSprites.sprites["player"])
        self.rect: pygame.Rect = self.image.get_rect()

        self.x: float = FIELD_WIDTH / 2
        self.y: float = FIELD_HEIGHT / 2

        self.rect.x = self.x
        self.rect.y = self.y

        self.dx: float = 0.
        self.dy: float = 0.

        self.max_speed: float = DEFAULT_PLAYER_SPEED
        self.speed_change: float = self.max_speed / SMOOTHNESS

        self.max_hp: int = DEFAULT_PLAYER_HP
        self.hp: int = DEFAULT_PLAYER_HP
        self.period: int = DEFAULT_PROJECTILE_PERIOD
        self.projectile_range: float = DEFAULT_PROJECTILE_RANGE
        self.projectile_speed: float = DEFAULT_PROJECTILE_SPEED
        self.projectile_size: int = DEFAULT_PROJECTILE_SIZE
        self.projectile_damage: int = DEFAULT_PROJECTILE_DAMAGE
        self.projectile_name_sprite: str = DEFAULT_PROJECTILE_TYPE

        self.projectile_ticks: int = math.ceil(self.projectile_range / self.projectile_speed) + 2
        self.projectile_trajectory: list[float] = [0.] * self.projectile_ticks

        self.items: list[Items.Item] = []

        # additional values
        self.upward_movement: bool = False
        self.downward_movement: bool = False
        self.rightward_movement: bool = False
        self.leftward_movement: bool = False

    def speed_calculation(self) -> None:
        """calculation of speed using directional values"""

        if self.upward_movement:
            if -self.dy < self.max_speed:
                self.dy -= self.speed_change

        if self.downward_movement:
            if self.dy < self.max_speed:
                self.dy += self.speed_change

        if self.rightward_movement:
            if self.dx < self.max_speed:
                self.dx += self.speed_change

        if self.leftward_movement:
            if -self.dx < self.max_speed:
                self.dx -= self.speed_change

        if not self.upward_movement and not self.downward_movement:
            if self.dy > 0:
                self.dy -= self.speed_change
                self.dy /= 1.01  # это нужно чтобы при остановки ты не двигался на маленькие дробные числа
            elif self.dy < 0:
                self.dy += self.speed_change
                self.dy /= 1.01

        if not self.rightward_movement and not self.leftward_movement:
            if self.dx > 0:
                self.dx -= self.speed_change
                self.dx /= 1.01
            elif self.dx < 0:
                self.dx += self.speed_change
                self.dx /= 1.01

    def coordinate_calculation(self) -> None:
        """coordinates calculation"""
        self.x += self.dx
        self.y += self.dy

        self.x, self.y = field_boundary_collision(self.x, self.y)

    def update(self) -> None:
        keys = pygame.key.get_pressed()
        self.upward_movement = keys[pygame.K_w]
        self.downward_movement = keys[pygame.K_s]
        self.rightward_movement = keys[pygame.K_d]
        self.leftward_movement = keys[pygame.K_a]

        self.speed_calculation()
        self.coordinate_calculation()

        self.rect.x = round(self.x)
        self.rect.y = round(self.y)
