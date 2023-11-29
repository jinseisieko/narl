"""constants"""
from ctypes import *

FIELD_WIDTH: int = 3000
FIELD_HEIGHT: int = 3000

WIDTH: int = windll.user32.GetSystemMetrics(0)
HEIGHT: int = windll.user32.GetSystemMetrics(1)

MOVE_SCREEN_RECT_X: float = WIDTH // 8
MOVE_SCREEN_RECT_Y: float = HEIGHT // 8

PLAYER_SIZE: int = 50  # matches the size of the player's image
TICKS: int = 120
FPS: tuple[int, int] = (60, 120)
DEFAULT_FPS: int = 0
ACCELERATION_SMOOTHNESS: int = 25
SLOWDOWN_SMOOTHNESS: int = ACCELERATION_SMOOTHNESS * 2
DASH_TIME = 10

DEFAULT_PLAYER_SPEED: float = 4
DEFAULT_PLAYER_HP: int = 10
DEFAULT_PROJECTILE_PERIOD: int = TICKS // 2
DEFAULT_PROJECTILE_SPEED: float = 5
DEFAULT_PROJECTILE_RANGE: float = 250
DEFAULT_PROJECTILE_DAMAGE: int = 1
DEFAULT_PROJECTILE_SIZE: int = 30
DEFAULT_PROJECTILE_TYPE: str = "default_projectile"

RED: tuple[int, int, int] = (255, 0, 0)
GREEN: tuple[int, int, int] = (0, 255, 0)
BLUE: tuple[int, int, int] = (0, 0, 255)
GRAY: tuple[int, int, int] = (200, 200, 200)

# вместо TYPE писарь реальное название типа врага
DEFAULT_TYPE_ENEMY_SIZE: int = 0
DEFAULT_TYPE_ENEMY_HP: int = 0
DEFAULT_TYPE_ENEMY_SPEED: float = 0
DEFAULT_TYPE_ENEMY_DAMAGE: int = 0
