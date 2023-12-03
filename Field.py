import random

import numba
import pygame

import Constants
import ImageSprites
from Constants import *


@numba.jit(nopython=True, fastmath=True)
def calculate_screen_movement(screen_centre_x: float, screen_centre_y: float, player_centerx: float,
                              player_centery: float,
                              player_max_speed: float, player_dx, player_dy, MOVE_SCREEN_RECT_X: int,
                              MOVE_SCREEN_RECT_Y: int) -> tuple[
    float, float]:
    speed: float = max(player_max_speed, (player_dx ** 2 + player_dy ** 2) ** 0.5)
    speed_x: float = speed * ((player_centerx - screen_centre_x) / MOVE_SCREEN_RECT_X)
    speed_y: float = speed * ((player_centery - screen_centre_y) / MOVE_SCREEN_RECT_Y)

    return screen_centre_x + speed_x, screen_centre_y + speed_y



class Field:
    def __init__(self) -> None:
        # values
        self.field: pygame.surface = pygame.Surface((FIELD_WIDTH, FIELD_HEIGHT))
        self.screen_centre: tuple[float, float] = 0.0, 0.0

        self.background = pygame.surface = pygame.Surface((FIELD_WIDTH, FIELD_HEIGHT))
        # self.background.fill((158, 240, 144))
        # self.background.fill((200, 200, 200))

        for i in range(FIELD_WIDTH // BACKGROUND_PICTURE_SIZE + 1):
            for j in range(FIELD_HEIGHT // BACKGROUND_PICTURE_SIZE + 1):
                self.background.blit(ImageSprites.sprites[f'texture_grass_{random.randint(0, 8)}'],
                                     (i * BACKGROUND_PICTURE_SIZE, j * BACKGROUND_PICTURE_SIZE))
        self.field.blit(self.background, (0, 0))

    def draw(self, *groups: pygame.sprite.Group, player=None) -> None:
        """draw groups in the sequence in which they are presented """
        x: int = max(0, min(FIELD_WIDTH - WIDTH, int(self.screen_centre[0]) - WIDTH // 2))
        y: int = max(0, min(FIELD_HEIGHT - HEIGHT, int(self.screen_centre[1]) - HEIGHT // 2))

        subsurface_rect: pygame.Rect = pygame.Rect(x, y, WIDTH, HEIGHT)
        self.field.blit(self.background, (x, y), subsurface_rect)

        for group in groups:
            group.draw(self.field)

        self.field.blit(ImageSprites.sprites["hat"],
                        (player.rect.x + Constants.PLAYER_SIZE // 2 - Constants.PLAYER_SIZE // 4, player.rect.y - 15))

        # pygame.draw.ellipse(self.field, (255, 0, 0), (self.screen_centre[0] - MOVE_SCREEN_RECT_X,
        #                                               self.screen_centre[1] - MOVE_SCREEN_RECT_Y,
        #                                               MOVE_SCREEN_RECT_X * 2, MOVE_SCREEN_RECT_Y * 2), 5)
        # pygame.draw.line(self.field, (255, 255, 255), (self.screen_centre[0] - WIDTH, self.screen_centre[1] - HEIGHT),
        #                  (self.screen_centre[0] + WIDTH, self.screen_centre[1] + HEIGHT), 3)
        # pygame.draw.line(self.field, (255, 255, 255), (self.screen_centre[0] - WIDTH, self.screen_centre[1] + HEIGHT),
        #                  (self.screen_centre[0] + WIDTH, self.screen_centre[1] - HEIGHT), 3)

    def move_screen_relative_player(self, player):
        self.screen_centre = calculate_screen_movement(*self.screen_centre, player.rect.centerx, player.rect.centery,
                                                       player.max_speed, player.dx, player.dy,
                                                       MOVE_SCREEN_RECT_X, MOVE_SCREEN_RECT_Y)
