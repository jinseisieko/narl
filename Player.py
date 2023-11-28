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


def calculate_speed(speed: float, max_speed: float, smoothness: int, sign: bool) -> float:
    dx: float = max_speed / smoothness
    if sign:
        speed -= dx
        speed = max(speed, -max_speed)
    else:
        speed += dx
        speed = min(speed, max_speed)
    print(speed)
    return speed


def calculate_movement(x: float, y: float, dx: float, dy: float, max_speed: float, acceleration: float, smoothness: int,
                       upward_movement: bool, downward_movement: bool,
                       rightward_movement: bool, leftward_movement: bool) -> tuple[float, float]:
    if upward_movement:
        dy = calculate_speed(dy, max_speed, smoothness, True)
    if downward_movement:
        dy = calculate_speed(dy, max_speed, smoothness, False)

    if rightward_movement:
        dx = calculate_speed(dx, max_speed, smoothness, False)

    if leftward_movement:
        dx = calculate_speed(dx, max_speed, smoothness, True)

    if not upward_movement and not downward_movement:
        if dy > 0:
            dy -= acceleration
        elif dy < 0:
            dy += acceleration
            dy /= 1.03

    if not rightward_movement and not leftward_movement:
        if dx > 0:
            dx -= acceleration
            dx /= 1.03
        elif dx < 0:
            dx += acceleration
            dx /= 1.03




    return dx, dy


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
        self.acceleration: float = self.max_speed / SMOOTHNESS

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

    def speed_calculation(self) -> None:
        """calculation of speed using directional values"""
        self.dx, self.dy = calculate_movement(self.x, self.y, self.dx, self.dy, self.max_speed, self.acceleration,
                                              SMOOTHNESS, self.upward_movement, self.downward_movement,
                                              self.rightward_movement, self.leftward_movement)

    def coordinate_calculation(self) -> None:
        """coordinates calculation"""
        dx = self.dx
        dy = self.dy
        dx = math.cos(math.atan2(abs(dy), abs(dx))) * dx
        dy = math.cos(math.atan2(abs(dx), abs(dy))) * dy
        self.x += dx
        self.y += dy

        self.x, self.y = field_boundary_collision(self.x, self.y)

    def update(self) -> None:
        keys = pygame.key.get_pressed()
        self.upward_movement = keys[pygame.K_w]
        self.downward_movement = keys[pygame.K_s]
        self.rightward_movement = keys[pygame.K_d]
        self.leftward_movement = keys[pygame.K_a]

        self.speed_calculation()
        self.coordinate_calculation()

        self.rect.x = round(self.x)
        self.rect.y = round(self.y)

    def shot(self) -> list:  # test
        return [DefaultPlayerProjectile(self, pygame.mouse.get_pos())]
