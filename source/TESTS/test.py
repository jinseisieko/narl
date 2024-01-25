import random

import numba
import numpy as np
import pygame as pg

from Constants import *


class Map:
    def __init__(self, data: np.ndarray) -> None:
        self.data: np.ndarray = data
        self.field: pygame.surface = pygame.Surface((0, 0))
        self.background: pygame.surface = pygame.Surface((FIELD_WIDTH, FIELD_HEIGHT))
        for i in numba.prange(FIELD_WIDTH // BACKGROUND_PICTURE_SIZE + 1):
            for j in numba.prange(FIELD_HEIGHT // BACKGROUND_PICTURE_SIZE + 1):
                self.background.blit(pygame.image.load(f"source/image/grasses/grass{random.randint(1, 4)}.png"),
                                     (i * BACKGROUND_PICTURE_SIZE, j * BACKGROUND_PICTURE_SIZE))

        self.background = pg.transform.scale(self.background.convert(), (FIELD_WIDTH, FIELD_HEIGHT))
        self.field = pg.transform.scale(self.field.convert(), (FIELD_WIDTH, FIELD_HEIGHT))

    def draw(self):
        self.field.blit(self.background, self.data[4:6], pygame.Rect(self.data[([4, 5, 8, 9])]))


@numba.njit(fastmath=True)
def calculate_screen_movement(screen_centre_x: float, screen_centre_y: float, player_centerx: float,
                              player_centery: float,
                              player_max_speed: float, player_dx, player_dy, MOVE_SCREEN_RECT_X: int,
                              MOVE_SCREEN_RECT_Y: int, dt: float) -> tuple[float, float]:
    speed: float = max(player_max_speed, (player_dx ** 2 + player_dy ** 2) ** 0.5)
    speed_x: float = speed * ((player_centerx - screen_centre_x) / MOVE_SCREEN_RECT_X) * dt
    speed_y: float = speed * ((player_centery - screen_centre_y) / MOVE_SCREEN_RECT_Y) * dt

    return screen_centre_x + speed_x, screen_centre_y + speed_y


class Field:
    def __init__(self) -> None:
        # values
        self.field: pygame.surface = pygame.Surface((FIELD_WIDTH, FIELD_HEIGHT))
        self.screen_centre: tuple[float, float] = 0.0, 0.0

        self.background = pygame.surface = pygame.Surface((FIELD_WIDTH, FIELD_HEIGHT))
        self.background.fill((255, 255, 255))
        for i in range(FIELD_WIDTH // BACKGROUND_PICTURE_SIZE + 1):
            for j in range(FIELD_HEIGHT // BACKGROUND_PICTURE_SIZE + 1):
                self.background.blit(pygame.image.load(f"source/image/grasses/grass{random.randint(1, 4)}.png"),
                                     (i * BACKGROUND_PICTURE_SIZE, j * BACKGROUND_PICTURE_SIZE))
        self.field.blit(self.background, (0, 0))

    def draw(self) -> None:
        """draw groups in the sequence in which they are presented """
        x: int = max(0, min(FIELD_WIDTH - WIDTH, int(self.screen_centre[0]) - WIDTH // 2))
        y: int = max(0, min(FIELD_HEIGHT - HEIGHT, int(self.screen_centre[1]) - HEIGHT // 2))

        subsurface_rect: pygame.Rect = pygame.Rect(x, y, WIDTH, HEIGHT)
        self.field.blit(self.background, (x, y), subsurface_rect)

        # for group in groups:
        #     group.draw(self.field)

        # self.field.blit(ImageSprites.sprites["phat"],
        #                 (player.rect.x + PLAYER_SIZE // 2 - PLAYER_SIZE // 4, player.rect.y - 15))

    def move_screen_relative_player(self, player, dt) -> None:
        self.screen_centre = calculate_screen_movement(*self.screen_centre, player[..., 0][0],
                                                       player[..., 1][0], player[..., 8][0], player[..., 6][0],
                                                       player[..., 7][0], MOVE_SCREEN_RECT_X, MOVE_SCREEN_RECT_Y, dt)
