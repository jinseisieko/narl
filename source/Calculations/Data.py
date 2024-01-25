from source.Constants import *

enemies = np.tile(np.array([-1000, -1000, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], dtype=np.float_), (MAX_ENEMIES, 1))
bullets = np.tile(np.array([-2000, -2000, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0], dtype=np.float_), (MAX_BULLETS, 1))
obstacles = np.tile(np.array([-3000, -3000, 0, 0], dtype=np.float_), (MAX_OBSTACLES, 1))
player = np.array([[1000, 1000, PLAYER_HALF_SIZE_X, PLAYER_HALF_SIZE_Y, PLAYER_MAX_HP, 0, 0, 0, PLAYER_MAX_VELOCITY,
                    PLAYER_SLOWDOWN, PLAYER_ACCELERATION, PLAYER_MAX_HP, PLAYER_ARMOR, PLAYER_DELAY,
                    PLAYER_ARMOR_PIERCING, PLAYER_BULLET_SIZE_X, PLAYER_BULLET_SIZE_Y, PLAYER_BULLET_DAMAGE,
                    PLAYER_CRITICAL_COEFFICIENT, PLAYER_CRITICAL_CHANCE, PLAYER_SCATTER, PLAYER_BULLET_LIVE_TIME,
                    PLAYER_BULLET_VELOCITY, PLAYER_DAMAGE_DELAY, 0, 0, 1]], dtype=np.float_)
field = np.array(
    [0, 0, MOVE_SCREEN_RECT_X, MOVE_SCREEN_RECT_Y, 0, 0,
     FIELD_WIDTH, FIELD_HEIGHT, WIDTH, HEIGHT, SPAWN_LINE, KILL_LINE],
    dtype=np.float_)
wave = np.array([0, 0.1, 0, 0, 100, 0, 3, 100, 0], dtype=np.float_)
types = np.array([
    [25, 25, 10, 1, 0, 0, 0, 300, 3, 0.0, 0],
    [40, 40, 20, 1, 0, 0, 0, 500, 3, 0.2, 1],
    [15, 15, 10, 1, 0, 0, 0, 150, 3, 0.2, 2],
    [25, 25, 10, 1, 0, 0, 0, 400, 3, 0.8, 3],
])

entity_ids = set(range(MAX_ENEMIES))
bullet_ids = set(range(MAX_BULLETS))
obstacles_ids = set(range(MAX_OBSTACLES))