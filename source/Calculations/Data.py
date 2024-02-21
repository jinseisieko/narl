from source.Constants import *

default_enemy = np.array([-1000, -1000, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], dtype=np.float_)
default_bullet = np.array([-2000, -2000, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0], dtype=np.float_)
default_obstacle = np.array([-3000, -3000, 0, 0], dtype=np.float_)
default_boss = np.array([[-1000, -1000, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0, 0]], dtype=np.float_)
default_player = np.array(
    [[1000, 1000, PLAYER_HALF_SIZE_X, PLAYER_HALF_SIZE_Y, PLAYER_MAX_HP, 0, 0, 0, PLAYER_MAX_VELOCITY,
      PLAYER_SLOWDOWN, PLAYER_ACCELERATION, PLAYER_MAX_HP, PLAYER_ARMOR, PLAYER_DELAY,
      PLAYER_ARMOR_PIERCING, PLAYER_BULLET_SIZE_X, PLAYER_BULLET_SIZE_Y, PLAYER_BULLET_DAMAGE,
      PLAYER_CRITICAL_COEFFICIENT, PLAYER_CRITICAL_CHANCE, PLAYER_SCATTER, PLAYER_BULLET_LIVE_TIME,
      PLAYER_BULLET_VELOCITY, PLAYER_DAMAGE_DELAY, 0, 0, 0, 0, 0, PLAYER_NEED_EXP]], dtype=np.float_)

enemies = np.tile(default_enemy, (MAX_ENEMIES, 1))
player_bullets = np.tile(default_bullet, (MAX_PLAYER_BULLETS, 1))
enemy_bullets = np.tile(default_bullet, (MAX_ENEMY_BULLETS, 1))
obstacles = np.tile(default_obstacle, (MAX_OBSTACLES, 1))
player = default_player.copy()

field = np.array(
    [0, 0, MOVE_SCREEN_RECT_X, MOVE_SCREEN_RECT_Y, 0, 0,
     FIELD_WIDTH, FIELD_HEIGHT, WIDTH, HEIGHT, SPAWN_LINE, KILL_LINE],
    dtype=np.float_)
wave = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0], dtype=np.float_)
portal = np.array([-4000, -4000, 0, 0], dtype=np.float_)
boss = default_boss

enemy_types = np.array([
    [25, 25, 1, 1, 0, 0, 0, 200, 0, 0.001, 0],
    [40, 40, 5, 1, 0, 0, 0, 100, 1, 0.01, 1],
    [30, 30, 10, 5, 0, 0, 0, 300, 0, 0.01, 2],
    [25, 25, 10, 2, 0, 0, 0, 600, 0, 0.01, 3],
    [50, 25, 40, 9, 0, 0, 0, 500, 0, 0.01, 4],
    [50, 50, 20, 11, 0, 0, 0, 600, 0, 0.01, 5],
    [25, 25, 50, 17, 0, 0, 0, 700, 0, 0.01, 6],
    [50, 50, 40, 30, 0, 0, 0, 500, 0, 0.01, 7],
])

boss_types = np.array([
    [200, 200, 200, 50, 0, 0, 0, 100, 10, 0.0, 0.33, 0, 0]
])

entity_ids = set(range(MAX_ENEMIES))
player_bullets_ids = set(range(MAX_PLAYER_BULLETS))
enemy_bullets_ids = set(range(MAX_ENEMY_BULLETS))
obstacles_ids = set(range(MAX_OBSTACLES))


def update_data(new_arrays, new_sets):
    global enemies, player_bullets, enemy_bullets, obstacles, player, field, wave, entity_ids, player_bullets_ids, enemy_bullets_ids, obstacles_ids
    enemies[...] = np.array(new_arrays[0], dtype=np.float_)
    player_bullets[...] = np.array(new_arrays[1], dtype=np.float_)
    obstacles[...] = np.array(new_arrays[2], dtype=np.float_)
    player[...] = np.array(new_arrays[3], dtype=np.float_)
    field[...] = np.array(new_arrays[4], dtype=np.float_)
    field[0:2] = player[0, 0:2]
    wave[...] = np.array(new_arrays[5], dtype=np.float_)
    enemy_bullets[...] = np.array(new_arrays[6], dtype=np.float_)
    entity_ids.clear()
    player_bullets_ids.clear()
    enemy_bullets_ids.clear()
    obstacles_ids.clear()
    entity_ids |= set(map(int, new_sets[0]))
    player_bullets_ids |= set(map(int, new_sets[1]))
    obstacles_ids |= set(map(int, new_sets[2]))
    enemy_bullets_ids |= set(map(int, new_sets[3]))


def clear_obstacles_ids():
    global obstacles_ids
    obstacles_ids.clear()
    obstacles_ids |= set(range(MAX_OBSTACLES))


def clear_bullets():
    global player_bullets_ids, enemy_bullets_ids
    player_bullets_ids.clear()
    enemy_bullets_ids.clear()

    player_bullets_ids |= set(range(MAX_PLAYER_BULLETS))
    enemy_bullets_ids |= set(range(MAX_ENEMY_BULLETS))

    player_bullets[...] = np.tile(default_bullet, (MAX_PLAYER_BULLETS, 1))
    enemy_bullets[...] = np.tile(default_bullet, (MAX_ENEMY_BULLETS, 1))


def get_data(old_data, old_sets):
    global enemies, player_bullets, enemy_bullets, obstacles, player, field, wave, entity_ids, player_bullets_ids, enemy_bullets_ids, obstacles_ids
    old_data[0] = enemies.tolist()
    old_data[1] = player_bullets.tolist()
    old_data[2] = obstacles.tolist()
    old_data[3] = player.tolist()
    old_data[4] = field.tolist()
    old_data[5] = wave.tolist()
    old_data[6] = enemy_bullets.tolist()
    # !!!!!!!!!!!!!!!!!! как сделать это с еще одним массивом

    old_sets[0] = np.array(list(entity_ids), dtype=np.float_).tolist()
    old_sets[1] = np.array(list(player_bullets_ids), dtype=np.float_).tolist()
    old_sets[2] = np.array(list(obstacles_ids), dtype=np.float_).tolist()
    old_sets[3] = np.array(list(enemy_bullets_ids), dtype=np.float_).tolist()
    # !!!!!!!!!!!!!!!!!!!!!!!! как сделать это с еще одним сетом


def clear_data():
    global enemies, player_bullets, enemy_bullets, obstacles, player, field, wave, entity_ids, player_bullets_ids, enemy_bullets_ids, obstacles_ids
    enemies[...] = np.tile(default_enemy, (MAX_ENEMIES, 1))
    player_bullets[...] = np.tile(default_bullet, (MAX_PLAYER_BULLETS, 1))
    enemy_bullets[...] = np.tile(default_bullet, (MAX_ENEMY_BULLETS, 1))
    obstacles[...] = np.tile(default_obstacle, (MAX_OBSTACLES, 1))
    player[...] = np.array(
        [[FIELD_WIDTH / 2, FIELD_HEIGHT / 2, PLAYER_HALF_SIZE_X, PLAYER_HALF_SIZE_Y, PLAYER_MAX_HP, 0, 0, 0,
          PLAYER_MAX_VELOCITY,
          PLAYER_SLOWDOWN, PLAYER_ACCELERATION, PLAYER_MAX_HP, PLAYER_ARMOR, PLAYER_DELAY,
          PLAYER_ARMOR_PIERCING, PLAYER_BULLET_SIZE_X, PLAYER_BULLET_SIZE_Y, PLAYER_BULLET_DAMAGE,
          PLAYER_CRITICAL_COEFFICIENT, PLAYER_CRITICAL_CHANCE, PLAYER_SCATTER, PLAYER_BULLET_LIVE_TIME,
          PLAYER_BULLET_VELOCITY, PLAYER_DAMAGE_DELAY, 0, 0, 0, 0, 0, PLAYER_NEED_EXP]], dtype=np.float_)
    field[...] = np.array(
        [player[0, 0], player[0, 1], MOVE_SCREEN_RECT_X, MOVE_SCREEN_RECT_Y, 0, 0,
         FIELD_WIDTH, FIELD_HEIGHT, WIDTH, HEIGHT, SPAWN_LINE, KILL_LINE],
        dtype=np.float_)
    wave[...] = np.array([0, 0, 0, 0, 0, 0, 0, 0, 0], dtype=np.float_)

    entity_ids.clear()
    player_bullets_ids.clear()
    enemy_bullets_ids.clear()
    obstacles_ids.clear()
    entity_ids |= set(range(MAX_ENEMIES))
    player_bullets_ids |= set(range(MAX_PLAYER_BULLETS))
    enemy_bullets_ids |= set(range(MAX_ENEMY_BULLETS))
    obstacles_ids |= set(range(MAX_OBSTACLES))
