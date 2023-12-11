"""classes Projectiles and additional functions"""
import math
import random

import numba
import pygame

import ImageSprites
from Collisions import Chunks
from Constants import *


@numba.njit(nopython=True, fastmath=True)
def calculate_angle(x1: float, y1: float, cursor_x: float, cursor_y: float) -> float:
    """angle calculation is necessary for DefaultPlayerProjectile class"""
    return math.atan2(cursor_y - y1, cursor_x - x1)


@numba.njit(nopython=True, fastmath=True)
def calculate_speed(angle: float, speed: float, player_dx: float, player_dy: float) -> tuple[float, float]:
    """speed calculation is necessary for DefaultPlayerProjectile class"""
    return speed * math.cos(angle) + player_dx, speed * math.sin(angle) + player_dy


class DefaultProjectile(pygame.sprite.Sprite):
    def __init__(self, player, target: tuple[float, float], chunks) -> None:
        super().__init__()
        self.hp: int = 0
        self.damage: int = 0

        # values
        self.player = player

        self.size: int = self.player.projectile_size

        self.image: pygame.Surface = pygame.Surface([self.size, self.size])
        self.color = self.player.projectile_color
        self.image.fill(self.color)
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
        self.index_trajectory: int = 0

        self.dx: float
        self.dy: float

        self.name = "Projectile"

        self.dx, self.dy = calculate_speed(self.angle, self.speed, self.player.dx, self.player.dy)
        self.player_dx = self.player.dx
        self.player_dy = self.player.dy

        self.chunks: Chunks = chunks
        self.ind1 = [int((self.y + (self.size / 2)) // CHUNK_SIZE), int((self.x + (self.size / 2)) // CHUNK_SIZE)]
        self.last_ind1 = self.ind1
        self.ind2 = [int((self.y - (self.size / 2)) // CHUNK_SIZE), int((self.x + (self.size / 2)) // CHUNK_SIZE)]
        self.last_ind2 = self.ind2
        self.ind3 = [int((self.y - (self.size / 2)) // CHUNK_SIZE), int((self.x - (self.size / 2)) // CHUNK_SIZE)]
        self.last_ind3 = self.ind3
        self.ind4 = [int((self.y + (self.size / 2)) // CHUNK_SIZE), int((self.x - (self.size / 2)) // CHUNK_SIZE)]
        self.last_ind4 = self.ind4
        self.chunks.add(self, self.ind1)
        self.chunks.add(self, self.ind2)
        self.chunks.add(self, self.ind3)
        self.chunks.add(self, self.ind4)

    def coordinate_calculation(self):
        self.distant += self.speed * TICKS / (CLOCK.get_fps() + 1e-10)
        self.x += self.dx * TICKS / (CLOCK.get_fps() + 1e-10)
        self.y += self.dy * TICKS / (CLOCK.get_fps() + 1e-10)

    def speed_calculation(self):
        self.dx, self.dy = calculate_speed(self.angle, self.speed, self.player_dx, self.player_dy)

    def get_name(self) -> str:
        return self.__class__.__name__

    def add_angle_ITEMS(self):
        dangle = 0
        if self.index_trajectory == 0:
            dangle += random.uniform(-(math.pi / 25 * self.player.buckshot_scatter_count),
                                     (math.pi / 25 * self.player.buckshot_scatter_count))

        dangle += -((math.pi / 100 * self.index_trajectory ** 0.4) / (
                (self.player.projectile_range / self.player.projectile_speed) / 10)) * self.player.red_gecko_count

        dangle += ((math.pi / 100 * self.index_trajectory ** 0.4) / (
                (self.player.projectile_range / self.player.projectile_speed) / 10)) * self.player.green_gecko_count

        dangle /= (1.3 * self.player.scope_count) + 1e-10
        self.angle += dangle

    def update(self):
        if self.x > FIELD_WIDTH - self.size:
            self.kill()
            return
        if self.y > FIELD_HEIGHT - self.size:
            self.kill()
            return
        if self.x < 0:
            self.kill()
            return
        if self.y < 0:
            self.kill()
            return

        self.ind1 = [int((self.y + (self.size / 2)) // CHUNK_SIZE), int((self.x + (self.size / 2)) // CHUNK_SIZE)]
        if self.ind1[0] != self.last_ind1[0] or self.ind1[1] != self.last_ind1[1]:
            self.chunks.move(self, self.last_ind1, self.ind1)
            self.last_ind1 = self.ind1

        self.ind2 = [int((self.y - (self.size / 2)) // CHUNK_SIZE), int((self.x + (self.size / 2)) // CHUNK_SIZE)]
        if self.ind2[0] != self.last_ind2[0] or self.ind2[1] != self.last_ind2[1]:
            self.chunks.move(self, self.last_ind2, self.ind2)
            self.last_ind2 = self.ind2

        self.ind3 = [int((self.y - (self.size / 2)) // CHUNK_SIZE), int((self.x - (self.size / 2)) // CHUNK_SIZE)]
        if self.ind3[0] != self.last_ind3[0] or self.ind3[1] != self.last_ind3[1]:
            self.chunks.move(self, self.last_ind3, self.ind3)
            self.last_ind3 = self.ind3

        self.ind4 = [int((self.y + (self.size / 2)) // CHUNK_SIZE), int((self.x - (self.size / 2)) // CHUNK_SIZE)]
        if self.ind4[0] != self.last_ind4[0] or self.ind4[1] != self.last_ind4[1]:
            self.chunks.move(self, self.last_ind4, self.ind4)
            self.last_ind4 = self.ind4

        self.add_angle_ITEMS()

        self.speed_calculation()
        self.coordinate_calculation()

        self.rect.x = round(self.x)
        self.rect.y = round(self.y)

        if self.distant >= self.range:
            self.kill()

        self.index_trajectory += 1

    def kill(self) -> None:
        self.chunks.del_(self, self.ind1)
        self.chunks.del_(self, self.ind2)
        self.chunks.del_(self, self.ind3)
        self.chunks.del_(self, self.ind4)
        super().kill()
