"""classes Enemies and additional functions"""
import math

import pygame.sprite

from Constants import *


class Enemy(pygame.sprite.Sprite):
    def __init__(self, player, x: float, y: float, ID: int, IDs: set):
        super().__init__()
        self.ID: int = ID
        self.IDs: set = IDs
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

    def angle_calculation(self):
        self.angle = math.atan2(self.player.y - self.y,
                                self.player.x - self.x)

    def speed_calculation(self):
        self.dx, self.dy = self.speed * math.cos(self.angle), self.speed * math.sin(self.angle)

    def coordinate_calculation(self):
        self.x += self.dx
        self.y += self.dy

    def update(self, array, positions: set[tuple[int, int]]) -> None:
        self.angle_calculation()
        self.coordinate_calculation()
        self.speed_calculation()

        self.rect.x = round(self.x) - DEFAULT_ENEMY_ENEMY_SIZE // 2
        self.rect.y = round(self.y) - DEFAULT_ENEMY_ENEMY_SIZE // 2

        i: int = int(math.floor(self.x / CHUNK_SIZE))
        j: int = int(math.floor(self.y / CHUNK_SIZE))
        if 0 <= i < CHUNK_N_X and 0 <= j < CHUNK_N_Y:
            for k in range(len(array[i][j])):
                if array[i][j][k][8] == 0:
                    array[i][j][k] = [self.x, self.y, self.dx, self.dy, self.hp, self.damage, self.size, 0, self.ID]
                    positions.add((i, j))
                    break
            else:
                print(2)
