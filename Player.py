"""class Player and additional functions"""
import random

import pygame.sprite

import Field
from Constants import *
from Inventory import Inventory
from Items import Item
from Projectiles import *


@numba.jit(nopython=True, fastmath=True)
def calculate_dash(velocity: float, max_speed: float, to_direction: int, DASH_COEFFICIENT: float) -> float:
    return velocity * (1 - abs(to_direction)) + DASH_COEFFICIENT * max_speed * to_direction


@numba.jit(nopython=True, fastmath=True)
def field_boundary_collision(x: float, y: float, dx: float, dy: float, FIELD_WIDTH: int, FIELD_HEIGHT: int,
                             PLAYER_SIZE: int) -> tuple[float, float, float, float]:
    """function is designed to change coordinates when colliding with a boundary"""

    if x > FIELD_WIDTH:
        x = FIELD_WIDTH
        dx = 0
    elif x < 0:
        x = 0.
        dx = 0

    if y > FIELD_HEIGHT:
        y = FIELD_HEIGHT
        dy = 0
    elif y < 0:
        y = 0.
        dy = 0

    return x, y, dx, dy


@numba.jit(nopython=True, fastmath=True)
def calculate_speed(speed: float, max_speed: float, dv: float, sign: bool) -> float:
    limit: float = max(abs(speed), max_speed)
    if sign:
        speed -= dv
        speed = max(speed, -limit)
    else:
        speed += dv
        speed = min(speed, limit)
    return speed


@numba.jit(nopython=True, fastmath=True)
def calculate_movement(x: float, y: float, dx: float, dy: float, max_speed: float, acceleration: float,
                       resistance_acceleration: float,
                       upward_movement: bool, downward_movement: bool,
                       rightward_movement: bool, leftward_movement: bool, FIELD_WIDTH: int, FIELD_HEIGHT: int,
                       PLAYER_SIZE: int) -> tuple[float, float, float, float]:
    # d = (dx ** 2 + dy ** 2) ** 0.5
    # if d > max_speed:
    #     dx *= max_speed / d
    #     dy *= max_speed / d

    if dx < 0:
        dx = min(0.0, dx + resistance_acceleration)
    else:
        dx = max(0.0, dx - resistance_acceleration)
    if dy < 0:
        dy = min(0.0, dy + resistance_acceleration)
    else:
        dy = max(0.0, dy - resistance_acceleration)

    if upward_movement:
        dy = calculate_speed(dy, max_speed, acceleration, True)
    if downward_movement:
        dy = calculate_speed(dy, max_speed, acceleration, False)
    if rightward_movement:
        dx = calculate_speed(dx, max_speed, acceleration, False)
    if leftward_movement:
        dx = calculate_speed(dx, max_speed, acceleration, True)

    x += dx
    y += dy

    return field_boundary_collision(x, y, dx, dy, FIELD_WIDTH, FIELD_HEIGHT, PLAYER_SIZE)


class Player(pygame.sprite.Sprite):
    """class Player"""

    def __init__(self, field: Field.Field, ID: int, IDs: set) -> None:
        super().__init__()
        self.field: Field.Field = field
        self.ID: int = ID
        self.IDs: set = IDs

        # values
        self.size: int = PLAYER_SIZE
        self.image: pygame.image = ImageSprites.sprites["player_nr"]
        self.rect: pygame.Rect = pygame.Surface((PLAYER_SIZE, PLAYER_SIZE)).get_rect()

        self.x: float = FIELD_WIDTH / 2
        self.y: float = FIELD_HEIGHT / 2

        self.rect.x = self.x - PLAYER_SIZE // 2
        self.rect.y = self.y - PLAYER_SIZE // 2

        self.dx: float = 0.
        self.dy: float = 0.

        self.max_speed: float = DEFAULT_PLAYER_SPEED
        self.acceleration: float = self.max_speed / ACCELERATION_SMOOTHNESS
        self.resistance_acceleration: float = self.max_speed / SLOWDOWN_SMOOTHNESS

        self.max_hp: int = DEFAULT_PLAYER_HP
        self.hp: int = DEFAULT_PLAYER_HP
        self.period: int = DEFAULT_PROJECTILE_PERIOD
        self.dash_timer: int = 0

        self.projectile_range: float = DEFAULT_PROJECTILE_RANGE
        self.projectile_speed: float = DEFAULT_PROJECTILE_SPEED
        self.projectile_size: int = DEFAULT_PROJECTILE_SIZE
        self.projectile_damage: int = DEFAULT_PROJECTILE_DAMAGE
        self.projectile_name_sprite: str = DEFAULT_PROJECTILE_TYPE
        self.projectile_color: tuple[int, int, int] = RED

        self.projectile_ticks: int = math.ceil(self.projectile_range / self.projectile_speed) + 2
        self.projectile_trajectory: list[float] = [0.] * self.projectile_ticks

        self.inventory: Inventory = Inventory(self)

        # additional values
        self.upward_movement: bool = False
        self.downward_movement: bool = False
        self.rightward_movement: bool = False
        self.leftward_movement: bool = False

        self.animation_frame: int = 0
        self.animation_number: int = 0
        self.animation_duration: int = 30

        self.field.screen_centre = [self.rect.centerx, self.rect.centery]

    def movements(self) -> None:
        self.x, self.y, self.dx, self.dy = calculate_movement(self.x, self.y, self.dx, self.dy, self.max_speed,
                                                              self.acceleration, self.resistance_acceleration,
                                                              self.upward_movement, self.downward_movement,
                                                              self.rightward_movement, self.leftward_movement,
                                                              FIELD_WIDTH, FIELD_HEIGHT, PLAYER_SIZE)

    def dash(self, to_x: int, to_y: int) -> None:
        if self.dash_timer == 0:
            self.dx = calculate_dash(self.dx, self.max_speed, to_x, DASH_COEFFICIENT)
            self.dy = calculate_dash(self.dy, self.max_speed, to_y, DASH_COEFFICIENT)
            self.dash_timer = DASH_DELAY

    def update(self) -> None:
        # animation once per animation_frame ticks and animation_duration ticks duration
        if self.animation_frame == 0 or self.animation_number >= 1:
            self.animation_frame = random.randint(35, 1000)

            self.animation_number = (self.animation_number + 1) % self.animation_duration
            if self.animation_number == 0:
                self.image = ImageSprites.sprites["player_nr"]
            else:
                self.image = ImageSprites.sprites["player_pd"]

        keys = pygame.key.get_pressed()
        self.upward_movement = keys[pygame.K_w]
        self.downward_movement = keys[pygame.K_s]
        self.rightward_movement = keys[pygame.K_d]
        self.leftward_movement = keys[pygame.K_a]

        self.movements()
        self.rect.x = round(self.x) - PLAYER_SIZE // 2
        self.rect.y = round(self.y) - PLAYER_SIZE // 2

        self.dash_timer = max(0, self.dash_timer - 1)

        if self.animation_frame > 0:
            self.animation_frame -= 1

    def shot(self, ID: int, IDs: set) -> list:  # test
        cursor_pos = pygame.mouse.get_pos()

        return [DefaultPlayerProjectile(self, (
            self.field.screen_centre[0] - WIDTH // 2 + cursor_pos[0],
            self.field.screen_centre[1] - HEIGHT // 2 + cursor_pos[1]), ID, IDs)]

    def add_item(self, item: Item):
        self.inventory.add_item(item)
