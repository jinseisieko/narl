"""classes Projectiles and additional functions"""
import math

import numba
import pygame

import ImageSprites
from Constants import *


@numba.jit(nopython=True, fastmath=True)
def calculate_angle(x1: float, y1: float, cursor_x: float, cursor_y: float) -> float:
    """angle calculation is necessary for DefaultPlayerProjectile class"""
    return math.atan2(cursor_y - y1, cursor_x - x1)


@numba.jit(nopython=True, fastmath=True)
def calculate_speed(angle: float, speed: float, player_dx: float, player_dy: float) -> tuple[float, float]:
    """speed calculation is necessary for DefaultPlayerProjectile class"""
    return speed * math.cos(angle) + player_dx, speed * math.sin(angle) + player_dy


@numba.jit(nopython=True, fastmath=True)
def coordinate_calculation(x: float, y: float, dx: float, dy: float, distant: float, speed: float) -> tuple[
    float, float, float]:
    """coordinate calculation for projectile"""
    return x + dx, y + dy, distant + speed


class DefaultPlayerProjectile(pygame.sprite.Sprite):
    def __init__(self, player, target: tuple[float, float], ID: int, IDs: set) -> None:
        super().__init__()
        self.ID: int = ID
        self.IDs: set = IDs
        self.hp: int = 0
        self.damage: int = 0

        # values
        self.player = player

        self.size: int = self.player.projectile_size

        self.image: pygame.Surface = ImageSprites.sprites["projectile30"]
        # self.color = self.player.projectile_color
        # self.image.fill(self.color)
        self.rect = self.image.get_rect()

        self.x: float = self.player.rect.centerx - self.size / 2
        self.y: float = self.player.rect.centery - self.size / 2

        self.range: float = self.player.projectile_range
        self.distant: float = 0
        self.speed: float = self.player.projectile_speed
        self.player_dx: float = self.player.dx
        self.player_dy: float = self.player.dy
        self.damage: int = self.player.projectile_damage
        self.angle: float = calculate_angle(self.player.rect.centerx, self.player.rect.centery, target[0], target[1])
        self.trajectory: list[float] = self.player.projectile_trajectory

        self.dx: float
        self.dy: float

        self.dx, self.dy = calculate_speed(self.angle, self.speed, self.player.dx, self.player.dy)

    def coordinate_calculation(self):
        self.x, self.y, self.distant = coordinate_calculation(self.x, self.y, self.dx, self.dy, self.distant,
                                                              self.speed)

    def update(self, array):
        self.coordinate_calculation()

        self.rect.x = round(self.x)
        self.rect.y = round(self.y)

        if self.distant >= self.range:
            self.IDs.add(self.ID)
            self.kill()

        x: int = int(math.ceil(self.x / CHUNK_SIZE))
        y: int = int(math.ceil(self.y / CHUNK_SIZE))
        for i in range(max(0, x - 1), min(CHUNK_N_X, x + 2)):
            for j in range(max(0, y - 1), min(CHUNK_N_Y, y + 2)):
                for k in range(len(array[i][j])):
                    if array[i][j][k][6] == 0:
                        array[i][j][k] = [self.x, self.y, self.hp, self.damage, self.size, 0, self.ID]
                        break
                else:
                    print(1)
