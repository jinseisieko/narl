"""classes Enemies and additional functions"""
import math

import pygame.sprite

from Collisions import Chunks
from Constants import *


class Enemy(pygame.sprite.Sprite):
    def __init__(self, player, x: float, y: float, chunks: Chunks):
        super().__init__()

        self.hp: int = DEFAULT_ENEMY_ENEMY_HP
        self.damage: int = DEFAULT_ENEMY_ENEMY_DAMAGE
        self.size = DEFAULT_ENEMY_ENEMY_SIZE

        self.image = pygame.Surface((DEFAULT_ENEMY_ENEMY_SIZE, DEFAULT_ENEMY_ENEMY_SIZE))
        self.speed = DEFAULT_ENEMY_ENEMY_SPEED

        self.image.fill(BLUE)

        self.rect = self.image.get_rect()
        self.x = x - DEFAULT_ENEMY_ENEMY_SIZE // 2
        self.y = y - DEFAULT_ENEMY_ENEMY_SIZE // 2

        self.player = player
        self.angle = 0
        self.dx = 0.
        self.dy = 0.

        self.chunks: Chunks = chunks
        self.ind = [int(self.y // CHUNK_SIZE), int(self.x // CHUNK_SIZE)]
        self.last_ind = self.ind
        self.chunks.add(self, self.ind)

    def angle_calculation(self):
        self.angle = math.atan2(self.player.y - self.y,
                                self.player.x - self.x)

    def speed_calculation(self):
        self.dx += self.speed * math.cos(self.angle)
        self.dy += self.speed * math.sin(self.angle)

    def normal_speed(self):
        self.dx = min(self.speed, self.dx)
        self.dy = min(self.speed, self.dy)

        d = (self.dx ** 2 + self.dy ** 2) ** 0.5
        if d > self.speed:
            self.dx *= self.speed / d
            self.dy *= self.speed / d

    def coordinate_calculation(self):
        self.x += self.dx
        self.y += self.dy

    def update(self) -> None:
        self.angle_calculation()
        self.speed_calculation()

        self.rect.x = round(self.x) - DEFAULT_ENEMY_ENEMY_SIZE // 2
        self.rect.y = round(self.y) - DEFAULT_ENEMY_ENEMY_SIZE // 2

        self.ind = [int(self.y // CHUNK_SIZE), int(self.x // CHUNK_SIZE)]
        if self.ind[0] != self.last_ind[0] or self.ind[1] != self.last_ind[1]:
            self.chunks.move(self, self.last_ind, self.ind)
            self.last_ind = self.ind

        self.chunks.calculate_collisions(self.ind)
        self.normal_speed()
        self.coordinate_calculation()
        # i: int = int(math.floor(self.x / CHUNK_SIZE))
        # j: int = int(math.floor(self.y / CHUNK_SIZE))
        # if 0 <= i < CHUNK_N_X and 0 <= j < CHUNK_N_Y:
        #     for k in range(len(array[i][j])):
        #         if array[i][j][k][8] == 0:
        #             array[i][j][k] = [self.x, self.y, self.dx, self.dy, self.hp, self.damage, self.size, 0, self.ID]
        #             positions.add((i, j))
        #             break
        #     else:
        #         print(2)

    def get_name(self) -> str:
        return self.__class__.__name__
