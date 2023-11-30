"""classes Enemies and additional functions"""
import math

import pygame.sprite
from Constants import *


class Enemy(pygame.sprite.Sprite):
    def __init__(self, player, x, y):
        super().__init__()

        self.image = pygame.Surface((DEFAULT_ENEMY_ENEMY_SIZE, DEFAULT_ENEMY_ENEMY_SIZE))
        self.speed = DEFAULT_ENEMY_ENEMY_SPEED

        self.image.fill(BLUE)

        self.rect = self.image.get_rect()
        self.x = x
        self.y = y

        self.player = player
        self.angle = 0
        self.dx = 0.
        self.dy = 0.

    def angle_calculation(self):
        self.angle = math.atan2(self.player.y + PLAYER_SIZE / 2 - self.y - DEFAULT_ENEMY_ENEMY_SIZE / 2,
                                self.player.x + PLAYER_SIZE / 2- self.x - DEFAULT_ENEMY_ENEMY_SIZE / 2)

    def speed_calculation(self):
        self.dx, self.dy = self.speed * math.cos(self.angle), self.speed * math.sin(self.angle)

    def coordinate_calculation(self):
        self.x += self.dx
        self.y += self.dy

    def update(self) -> None:
        self.angle_calculation()
        self.speed_calculation()
        self.coordinate_calculation()

        self.rect.x = round(self.x)
        self.rect.y = round(self.y)
