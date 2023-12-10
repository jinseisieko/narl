"""classes Enemies and additional functions"""
import math

import pygame.sprite

from Collisions import Chunks
from Constants import *

class Storage:

    def __init__(self, x, y, size) -> None:
        super().__init__()
        self.x, self.y = x, y
        self.dx = 0
        self.dy = 0
        self.angle = 0
        self.size = size


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
        self.storage = Storage(x - DEFAULT_ENEMY_ENEMY_SIZE // 2, y - DEFAULT_ENEMY_ENEMY_SIZE // 2, DEFAULT_ENEMY_ENEMY_SIZE)

        self.player = player

        self.chunks: Chunks = chunks
        self.ind = [int(self.storage.y // CHUNK_SIZE), int(self.storage.x // CHUNK_SIZE)]
        self.last_ind = self.ind
        self.chunks.add(self.storage, self.ind)

    def angle_calculation(self):
        self.storage.angle = math.atan2(self.player.y - self.storage.y,
                                self.player.x - self.storage.x)

    def speed_calculation(self):
        self.storage.dx += self.speed * math.cos(self.storage.angle)
        self.storage.dy += self.speed * math.sin(self.storage.angle)

    def normal_speed(self):
        self.storage.dx = min(self.speed, self.storage.dx)
        self.storage.dy = min(self.speed, self.storage.dy)

        d = (self.storage.dx ** 2 + self.storage.dy ** 2) ** 0.5
        if d > self.speed:
            self.storage.dx *= self.speed / d
            self.storage.dy *= self.speed / d

    def coordinate_calculation(self):
        self.storage.x += self.storage.dx
        self.storage.y += self.storage.dy

    def update(self) -> None:
        self.angle_calculation()
        self.speed_calculation()

        self.rect.x = round(self.storage.x) - DEFAULT_ENEMY_ENEMY_SIZE // 2
        self.rect.y = round(self.storage.y) - DEFAULT_ENEMY_ENEMY_SIZE // 2

        self.ind = [int(self.storage.y // CHUNK_SIZE), int(self.storage.x // CHUNK_SIZE)]
        if self.ind[0] != self.last_ind[0] or self.ind[1] != self.last_ind[1]:
            self.chunks.move(self.storage, self.last_ind, self.ind)
            self.last_ind = self.ind

        self.normal_speed()
        self.coordinate_calculation()

    def get_name(self) -> str:
        return self.__class__.__name__
