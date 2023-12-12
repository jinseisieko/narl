"""classes Enemies and additional functions"""
import random

import pygame.sprite

from Collisions import Chunks
from Constants import *






class Enemy(pygame.sprite.Sprite):
    def __init__(self, player, x: float, y: float, chunks: Chunks):
        super().__init__()

        self.hp: int = DEFAULT_ENEMY_ENEMY_HP
        self.damage: int = DEFAULT_ENEMY_ENEMY_DAMAGE
        self.size: int = DEFAULT_ENEMY_ENEMY_SIZE
        self.hp: int = DEFAULT_ENEMY_ENEMY_HP
        self.mhp: int = self.hp

        self.image = pygame.Surface((self.size, self.size))
        self.image.fill([random.randint(5, 200) for _ in range(3)])
        pygame.draw.rect(self.image, 0, (0, 0, self.size, self.size), width=4)
        pygame.draw.rect(self.image, 0, (self.size // 4, self.size // 3, self.size // 7, self.size // 5), width=4)
        pygame.draw.rect(self.image, 0, (self.size // 5 * 3, self.size // 3, self.size // 7, self.size // 5), width=4)
        self.speed: float = DEFAULT_ENEMY_ENEMY_SPEED

        self.rect = self.image.get_rect()
        self.x: float = x - DEFAULT_ENEMY_ENEMY_SIZE // 2
        self.y: float = y - DEFAULT_ENEMY_ENEMY_SIZE // 2

        self.dx: float = 0.
        self.dy: float = 0.

        self.name: str = "Enemy"

        self.player = player
        self.angle: float = 0.

        self.chunks: Chunks = chunks
        self.ind: list[int, int] = [int(self.y // CHUNK_SIZE), int(self.x // CHUNK_SIZE)]
        self.last_ind: list[int, int] = self.ind
        self.chunks.add(self, self.ind)

    def angle_calculation(self):
        self.angle = math.atan2(self.player.y - self.y,
                                self.player.x - self.x)

    def speed_calculation(self):
        self.dx = self.speed * math.cos(self.angle)
        self.dy = self.speed * math.sin(self.angle)

    def coordinate_calculation(self):
        self.x += self.dx * TICKS / (CLOCK.get_fps() + 1e-10)
        self.y += self.dy * TICKS / (CLOCK.get_fps() + 1e-10)

    def update(self) -> None:
        self.image.fill((255, math.ceil(255 / self.mhp * self.hp), math.ceil(255 / self.mhp * self.hp)))
        pygame.draw.rect(self.image, 0, (0, 0, self.size, self.size), width=4)
        pygame.draw.rect(self.image, 0, (self.size // 4, self.size // 3, self.size // 7, self.size // 5), width=4)
        pygame.draw.rect(self.image, 0, (self.size // 5 * 3, self.size // 3, self.size // 7, self.size // 5), width=4)

        self.x = max(0, min(FIELD_WIDTH - self.size // 2, self.x))
        self.y = max(0, min(FIELD_HEIGHT - self.size // 2, self.y))

        self.ind = [int(self.y // CHUNK_SIZE), int(self.x // CHUNK_SIZE)]
        if self.ind[0] != self.last_ind[0] or self.ind[1] != self.last_ind[1]:
            self.chunks.move(self, self.last_ind, self.ind)
        self.last_ind = self.ind

        self.angle_calculation()
        self.speed_calculation()
        self.coordinate_calculation()

        self.rect.x = round(self.x) - DEFAULT_ENEMY_ENEMY_SIZE // 2
        self.rect.y = round(self.y) - DEFAULT_ENEMY_ENEMY_SIZE // 2

    def get_name(self) -> str:
        return self.__class__.__name__

    def kill(self) -> None:
        self.chunks.del_(self, self.ind)
        super().kill()
