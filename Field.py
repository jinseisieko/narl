import random

import numba

import ImageSprites
from Constants import *


@numba.njit(fastmath=True)
def calculate_screen_movement(screen_centre_x: float, screen_centre_y: float, player_centerx: float,
                              player_centery: float,
                              player_max_speed: float, player_dx, player_dy, MOVE_SCREEN_RECT_X: int,
                              MOVE_SCREEN_RECT_Y: int, fps: float) -> tuple[float, float]:
    speed: float = max(player_max_speed, (player_dx ** 2 + player_dy ** 2) ** 0.5)
    speed_x: float = speed * ((player_centerx - screen_centre_x) / MOVE_SCREEN_RECT_X) * TICKS / (fps + 1e-10)
    speed_y: float = speed * ((player_centery - screen_centre_y) / MOVE_SCREEN_RECT_Y) * TICKS / (fps + 1e-10)

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
                self.background.blit(pygame.image.load(f"image/grasses/grass{random.randint(1, 4)}.png"),
                                     (i * BACKGROUND_PICTURE_SIZE, j * BACKGROUND_PICTURE_SIZE))
        self.field.blit(self.background, (0, 0))

    def draw(self, groups: tuple, FIELD_WIDTH, FIELD_HEIGHT, WIDTH, HEIGHT, PLAYER_SIZE, player) -> None:
        """draw groups in the sequence in which they are presented """
        x: int = max(0, min(FIELD_WIDTH - WIDTH, int(self.screen_centre[0]) - WIDTH // 2))
        y: int = max(0, min(FIELD_HEIGHT - HEIGHT, int(self.screen_centre[1]) - HEIGHT // 2))

        subsurface_rect: pygame.Rect = pygame.Rect(x, y, WIDTH, HEIGHT)
        self.field.blit(self.background, (x, y), subsurface_rect)

        for group in groups:
            group.draw(self.field)

        self.field.blit(ImageSprites.sprites["phat"],
                        (player.rect.x + PLAYER_SIZE // 2 - PLAYER_SIZE // 4, player.rect.y - 15))

    def move_screen_relative_player(self, player) -> None:
        self.screen_centre = calculate_screen_movement(*self.screen_centre, player.rect.centerx, player.rect.centery,
                                                       player.max_speed, player.dx, player.dy,
                                                       MOVE_SCREEN_RECT_X, MOVE_SCREEN_RECT_Y, CLOCK.get_fps())
