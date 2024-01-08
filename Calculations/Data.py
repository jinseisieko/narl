from Constants import *

enemies = np.tile(np.array([-100, -100, 0, 0, 0, 0, 0, 0, 1, 0], dtype=np.float_), (MAX_ENEMIES, 1))
bullets = np.tile(np.array([-200, -200, 0, 0, 0, 0, 0, 0, 1, 0, 1], dtype=np.float_), (MAX_BULLETS, 1))
obstacles = np.tile(np.array([-300, -300, 0, 0], dtype=np.float_), (MAX_OBSTACLES, 1))
player = np.array([[1000, 1000, PLAYER_HALF_SIZE_X, PLAYER_HALF_SIZE_Y, PLAYER_MAX_HP, 0, 0, 0, PLAYER_MAX_VELOCITY,
                    PLAYER_SLOWDOWN, PLAYER_ACCELERATION, PLAYER_MAX_HP, PLAYER_ARMOR, PLAYER_DELAY,
                    PLAYER_ARMOR_PIERCING, PLAYER_BULLET_SIZE_X, PLAYER_BULLET_SIZE_Y, PLAYER_BULLET_DAMAGE,
                    PLAYER_CRITICAL_COEFFICIENT, PLAYER_CRITICAL_CHANCE, PLAYER_SCATTER, PLAYER_BULLET_LIVE_TIME,
                    PLAYER_BULLET_VELOCITY, PLAYER_DAMAGE_DELAY]], dtype=np.float_)

entity_ids = set(range(MAX_ENEMIES))
bullet_ids = set(range(MAX_BULLETS))
obstacles_ids = set(range(MAX_OBSTACLES))