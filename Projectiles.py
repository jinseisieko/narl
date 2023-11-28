"""classes Projectiles and additional functions"""
import math
from Constants import *

import pygame


def angle_calculation(x1, y1, cursor_x, cursor_y) -> float:
    """angle calculation is necessary for DefaultPlayerProjectile class"""
    print(((y1 - FIELD_HEIGHT) + cursor_y))
    return math.atan2(((y1 - HEIGHT) + cursor_y) - y1, ((x1 - WIDTH) + cursor_x) - x1)


def speed_calculation(angle: float, speed: float) -> tuple[float, float]:
    """speed calculation is necessary for DefaultPlayerProjectile class"""
    return speed * math.cos(angle), speed * math.sin(angle)


class DefaultPlayerProjectile(pygame.sprite.Sprite):
    def __init__(self, player, target: tuple[float, float]) -> None:
        super().__init__()
        print(1)
        self.player = player

        self.size: int = self.player.projectile_size

        self.image: pygame.Surface = pygame.Surface([self.size, self.size])  # пока просто цвет
        self.color = self.player.projectile_color
        self.image.fill(self.color)
        self.rect = self.image.get_rect()

        self.x: float = self.player.rect.centerx
        self.y: float = self.player.rect.centery

        self.range: float = self.player.projectile_range
        self.distant: float = 0
        self.speed: float = self.player.projectile_speed
        self.damage: int = self.player.projectile_damage
        self.angle: float = angle_calculation(self.player.rect.centerx, self.player.rect.centery, target[0], target[1])
        self.trajectory: list[float] = self.player.projectile_trajectory

        self.dx: float = 0.
        self.dy: float = 0.

        self.dx, self.dy = speed_calculation(self.angle, self.speed)

    def coordinate_calculation(self):
        self.x += self.dx
        self.y += self.dy

    def update(self):
        self.coordinate_calculation()

        self.rect.x = round(self.x)
        self.rect.y = round(self.y)

        self.distant += self.speed

        if self.distant >= self.range:
            self.kill()
