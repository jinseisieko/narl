"""classes Enemies and additional functions"""
import numba
import numpy as np
import pygame.sprite

from Collisions import Chunks
from Constants import *


@numba.njit(fastmath=True, nogil=True, parallel=True)
def calculate_movement(player_x: float, player_y: float, enemy_data: np.array, speed: float, TICKS: int, fps: float, CHUNK_SIZE, FIELD_WIDTH, FIELD_HEIGHT):
    chunks = np.zeros((CHUNK_SIZE, CHUNK_SIZE, 20))
    for i in numba.prange(1, len(enemy_data)):
        x, y, half_size = enemy_data[i]

        x = max(0, min(FIELD_WIDTH - half_size, x))
        y = max(0, min(FIELD_HEIGHT - half_size, y))

        ind = int(y / CHUNK_SIZE), int(x / CHUNK_SIZE)
        chunks[*ind][np.where(chunks[*ind] == 0)] = i

        angle = np.arctan2(player_y - y, player_x - x)

        dx = speed * np.cos(angle)
        dy = speed * np.sin(angle)
        if fps != 0:
            x += dx * TICKS / (fps + 1e-10)
            y += dy * TICKS / (fps + 1e-10)

        enemy_data[i] = np.array([x, y])

    return enemy_data, chunks


class Enemy(pygame.sprite.Sprite):
    def __init__(self, player, x: float, y: float, chunks: Chunks, i: int):
        super().__init__()

        self.hp: int = DEFAULT_ENEMY_ENEMY_HP
        self.damage: int = DEFAULT_ENEMY_ENEMY_DAMAGE
        self.size: int = DEFAULT_ENEMY_ENEMY_SIZE
        self.hp: int = DEFAULT_ENEMY_ENEMY_HP
        self.mhp: int = self.hp

        self.image = pygame.Surface((self.size, self.size))
        # self.image.fill([random.randint(5, 200) for _ in range(3)])
        # pygame.draw.rect(self.image, 0, (self.size // 5, self.size // 3, self.size // 7, self.size // 5), width=4)
        self.speed: float = DEFAULT_ENEMY_ENEMY_SPEED

        self.rect = self.image.get_rect()
        self.x: float = x - DEFAULT_ENEMY_ENEMY_SIZE // 2
        self.y: float = y - DEFAULT_ENEMY_ENEMY_SIZE // 2

        self.outlines_rect = (0, 0, self.size, self.size)
        self.left_eye_rect = (self.size // 4, self.size // 3, self.size // 7, self.size // 5)
        self.right_eye_rect = (self.size // 5 * 3, self.size // 3, self.size // 7, self.size // 5)
        self.half_size = self.size // 2

        self.image.fill((255, int(255 / self.mhp * self.hp), int(255 / self.mhp * self.hp)))
        pygame.draw.rect(self.image, 0, self.outlines_rect, width=4)
        pygame.draw.rect(self.image, 0, self.left_eye_rect)
        pygame.draw.rect(self.image, 0, self.right_eye_rect)

        self.dx: float = 0.
        self.dy: float = 0.

        self.name: str = "Enemy"

        self.player = player
        self.angle: float = 0.

        self.chunks: Chunks = chunks
        self.ind: list[int, int] = [int(self.y // CHUNK_SIZE), int(self.x // CHUNK_SIZE)]
        self.last_ind: list[int, int] = self.ind
        self.chunks.add(self, self.ind)
        self.i = i

    def get_damage(self, damage):
        self.hp -= damage
        if self.hp < 0:
            self.kill()
        else:
            self.image.fill((255, int(255 / self.mhp * self.hp), int(255 / self.mhp * self.hp)))
            pygame.draw.rect(self.image, 0, self.outlines_rect, width=4)
            pygame.draw.rect(self.image, 0, self.left_eye_rect)
            pygame.draw.rect(self.image, 0, self.right_eye_rect)

    def update(self, arr) -> None:
        self.x, self.y = arr[self.i]

        #self.x = max(0, min(FIELD_WIDTH - self.half_size, self.x))
        #self.y = max(0, min(FIELD_HEIGHT - self.half_size, self.y))
        #self.ind = [int(self.y / CHUNK_SIZE), int(self.x / CHUNK_SIZE)]
        #if self.ind[0] != self.last_ind[0] or self.ind[1] != self.last_ind[1]:
        #    self.chunks.move(self, self.last_ind, self.ind)
        #    self.last_ind = self.ind


        self.rect.x = self.x - self.half_size
        self.rect.y = self.y - self.half_size

    def get_name(self) -> str:
        return self.__class__.__name__

    def kill(self) -> None:
        self.chunks.del_(self, self.ind)
        super().kill()
