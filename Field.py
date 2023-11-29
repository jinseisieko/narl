import math
import random

import numba
import pygame

import Constants
import ImageSprites
from Constants import *


def calculate_screen_movement(screen_centre: list[float, float], player_centerx: float, player_centery: float,
                              speed: float) -> \
        list[float, float]:
    speed_x: float = speed * ((player_centerx - screen_centre[0]) / MOVE_SCREEN_RECT_X)
    speed_y: float = speed * ((player_centery - screen_centre[1]) / MOVE_SCREEN_RECT_Y)

    screen_centre[0] += speed_x
    screen_centre[1] += speed_y

    return screen_centre


class Field:
    def __init__(self) -> None:
        # values
        self.field: pygame.surface = pygame.Surface((FIELD_WIDTH, FIELD_HEIGHT))
        self.screen_centre: list[float, float] = [0., 0.]

        self.background = pygame.surface = pygame.Surface((FIELD_WIDTH, FIELD_HEIGHT))
        self.background.fill((158, 240, 144))
        # self.background.fill((200, 200, 200))
        for i in range(FIELD_WIDTH // 400 + 1):
            for j in range(FIELD_HEIGHT // 400 + 1):
                number_texture_grass = random.randint(0, 8)
                self.background.blit(ImageSprites.sprites[f'texture_grass_{number_texture_grass}'], (i * 400, j * 400))

        self.field.blit(self.background, (0, 0))
        # сделать его красивым

    def draw(self, *groups: pygame.sprite.Group, player=None) -> None:
        """draw groups in the sequence in which they are presented """
        self.field.blit(self.background, (0, 0))
        for group in groups:
            group.draw(self.field)

        self.field.blit(ImageSprites.sprites["hat"],
                        (player.rect.x + Constants.PLAYER_SIZE // 2 - Constants.PLAYER_SIZE // 4, player.rect.y - 15))

        # pygame.draw.rect(self.field, (255, 0, 0), (self.screen_centre[0] - MOVE_SCREEN_RECT_X,
        #                                            self.screen_centre[1] - MOVE_SCREEN_RECT_Y,
        #                                            MOVE_SCREEN_RECT_X * 2, MOVE_SCREEN_RECT_Y * 2), 5)

    def move_screen_relative_player(self, player):
        self.screen_centre = calculate_screen_movement(self.screen_centre,
                                                       player.rect.centerx,
                                                       player.rect.centery, player.max_speed)
