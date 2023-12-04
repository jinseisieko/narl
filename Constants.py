"""constants"""
from ctypes import windll

CHUNK_SIZE = 100
CHUNK_N_X = 50
CHUNK_N_Y = 50

FIELD_WIDTH: int = CHUNK_N_X * CHUNK_SIZE
FIELD_HEIGHT: int = CHUNK_N_Y * CHUNK_SIZE

WIDTH: int = windll.user32.GetSystemMetrics(0)
HEIGHT: int = windll.user32.GetSystemMetrics(1)

MOVE_SCREEN_RECT_X: int = WIDTH // 8
MOVE_SCREEN_RECT_Y: int = HEIGHT // 8

BACKGROUND_PICTURE_SIZE = 400

PLAYER_SIZE: int = 50  # matches the size of the player's image
TICKS: int = 120  # any integer from 30 to 120 that is a divisor of 120
FPS: tuple[int, int] = (60, 120)
COEFFICIENT: float = 120 / TICKS
DEFAULT_FPS: int = 1
DOUBLE_CLICK_INTERVAL: int = 200
ACCELERATION_SMOOTHNESS: int = 25
SLOWDOWN_SMOOTHNESS: int = ACCELERATION_SMOOTHNESS * 2

DEFAULT_PLAYER_SPEED: float = 4 * COEFFICIENT
DEFAULT_PLAYER_HP: int = 10
DASH_DELAY: int = TICKS * 2
DASH_COEFFICIENT: float = 2.2 / (COEFFICIENT ** 0.5)

DEFAULT_PROJECTILE_PERIOD: int = TICKS# не больше 20
MAX_PROJECTILE_PERIOD = TICKS // 20
DEFAULT_PROJECTILE_SPEED: float = 5 * COEFFICIENT
DEFAULT_PROJECTILE_RANGE: float = 250
DEFAULT_PROJECTILE_DAMAGE: int = 1
DEFAULT_PROJECTILE_SIZE: int = 15
DEFAULT_PROJECTILE_TYPE: str = "default_projectile"

RED: tuple[int, int, int] = (255, 0, 0)
GREEN: tuple[int, int, int] = (0, 255, 0)
BLUE: tuple[int, int, int] = (0, 0, 255)
GRAY: tuple[int, int, int] = (200, 200, 200)
BLACK: tuple[int, int, int] = (0, 0, 0)

# fonts
FONT_CONSOLE = (None, 27)
FONT_PAUSE = (None, 46)
FONT_FPS = (None, 27)

W: str = "W"
A: str = "A"
S: str = "S"
D: str = "D"

# вместо TYPE писарь реальное название типа врага
DEFAULT_TYPE_ENEMY_SIZE: int = 0
DEFAULT_TYPE_ENEMY_HP: int = 0
DEFAULT_TYPE_ENEMY_SPEED: float = 0
DEFAULT_TYPE_ENEMY_DAMAGE: int = 0

DEFAULT_ENEMY_ENEMY_SIZE: int = 40
DEFAULT_ENEMY_ENEMY_HP: int = 0
DEFAULT_ENEMY_ENEMY_SPEED: float = 3 * COEFFICIENT
DEFAULT_ENEMY_ENEMY_DAMAGE: int = 0
