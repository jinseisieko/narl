"""class Player and additional functions"""

import pygame.sprite

import ImageSprites
import Items
from Projectiles import *


def field_boundary_collision(x: float, y: float) -> tuple[float, float]:
    """function is designed to change coordinates when colliding with a boundary"""

    if x > FIELD_WIDTH - PLAYER_SIZE:
        x = FIELD_WIDTH - PLAYER_SIZE
    elif x < 0:
        x = 0.

    if y > FIELD_HEIGHT - PLAYER_SIZE:
        y = FIELD_HEIGHT - PLAYER_SIZE
    elif y < 0:
        y = 0

    return x, y


def calculate_speed(speed: float, max_speed: float, sign: bool) -> float:
    dx: float = max_speed / ACCELERATION_SMOOTHNESS
    if sign:
        speed -= dx
        speed = max(speed, -max_speed)
    else:
        speed += dx
        speed = min(speed, max_speed)
    return speed


def calculate_movement(x: float, y: float, dx: float, dy: float, max_speed: float, acceleration: float,
                       upward_movement: bool, downward_movement: bool,
                       rightward_movement: bool, leftward_movement: bool) -> tuple[float, float, float, float]:
    if dx < 0:
        dx = min(0.0, dx + max_speed / SLOWDOWN_SMOOTHNESS)
    else:
        dx = max(0.0, dx - max_speed / SLOWDOWN_SMOOTHNESS)

    if dy < 0:
        dy = min(0.0, dy + max_speed / SLOWDOWN_SMOOTHNESS)
    else:
        dy = max(0.0, dy - max_speed / SLOWDOWN_SMOOTHNESS)

    if upward_movement:
        dy = calculate_speed(dy, max_speed, True)
    if downward_movement:
        dy = calculate_speed(dy, max_speed, False)
    if rightward_movement:
        dx = calculate_speed(dx, max_speed, False)
    if leftward_movement:
        dx = calculate_speed(dx, max_speed, True)

    x += dx
    y += dy

    x, y = field_boundary_collision(x, y)
    return x, y, dx, dy


class Player(pygame.sprite.Sprite):
    """class Player"""

    def __init__(self) -> None:
        super().__init__()

        # values
        self.size: int = PLAYER_SIZE
        self.image: pygame.image = pygame.image.load(ImageSprites.sprites["player"])
        self.rect: pygame.Rect = self.image.get_rect()

        self.x: float = FIELD_WIDTH / 2
        self.y: float = FIELD_HEIGHT / 2

        self.rect.x = self.x
        self.rect.y = self.y

        self.dx: float = 0.
        self.dy: float = 0.

        self.max_speed: float = DEFAULT_PLAYER_SPEED
        self.acceleration: float = self.max_speed / ACCELERATION_SMOOTHNESS

        self.max_hp: int = DEFAULT_PLAYER_HP
        self.hp: int = DEFAULT_PLAYER_HP
        self.period: int = DEFAULT_PROJECTILE_PERIOD
        self.projectile_range: float = DEFAULT_PROJECTILE_RANGE
        self.projectile_speed: float = DEFAULT_PROJECTILE_SPEED
        self.projectile_size: int = DEFAULT_PROJECTILE_SIZE
        self.projectile_damage: int = DEFAULT_PROJECTILE_DAMAGE
        self.projectile_name_sprite: str = DEFAULT_PROJECTILE_TYPE
        self.projectile_color: tuple[int, int, int] = RED

        self.projectile_ticks: int = math.ceil(self.projectile_range / self.projectile_speed) + 2
        self.projectile_trajectory: list[float] = [0.] * self.projectile_ticks

        self.items: list[Items.Item] = []

        # additional values
        self.upward_movement: bool = False
        self.downward_movement: bool = False
        self.rightward_movement: bool = False
        self.leftward_movement: bool = False

    def movements(self) -> None:
        """calculation of speed using directional values"""
        self.x, self.y, self.dx, self.dy = calculate_movement(self.x, self.y, self.dx, self.dy, self.max_speed,
                                                              self.acceleration, self.upward_movement,
                                                              self.downward_movement,
                                                              self.rightward_movement, self.leftward_movement)

    def update(self) -> None:
        keys = pygame.key.get_pressed()
        self.upward_movement = keys[pygame.K_w]
        self.downward_movement = keys[pygame.K_s]
        self.rightward_movement = keys[pygame.K_d]
        self.leftward_movement = keys[pygame.K_a]
        self.movements()
        self.rect.x = round(self.x)
        self.rect.y = round(self.y)

    def shot(self) -> list:  # test
        return [DefaultPlayerProjectile(self, pygame.mouse.get_pos())]
