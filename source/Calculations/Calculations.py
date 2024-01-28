import numpy as np
from numba import njit


def calc_enemy_direction(enemies: np.ndarray, x: np.float_, y: np.float_) -> None:
    k = 10
    k_2 = k / 2
    x = x + np.random.rand(*enemies[..., 6].shape) * k - k_2
    y = y + np.random.rand(*enemies[..., 7].shape) * k - k_2

    angle = np.arctan2(y - enemies[..., 1], x - enemies[..., 0])
    enemies[..., 6] = np.cos(angle) * enemies[..., 9]
    enemies[..., 7] = np.sin(angle) * enemies[..., 9]


def calc_movements(objects: np.ndarray, dt: np.float_) -> None:
    objects[..., 0:2] += objects[..., 6:8] * dt


def calc_bullet_movements(bullet: np.ndarray, dt: np.float_):
    bullet[..., 0:2] += bullet[..., 6:8] * dt
    bullet[..., 9] += dt

    bullet[np.where(bullet[..., 9] >= bullet[..., 10])] = np.array([-2000, -2000, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0],
                                                                   dtype=np.float_)


def calc_player_movement(player: np.ndarray, direction: np.ndarray, dt: np.float_) -> None:
    vx: np.float_
    vy: np.float_
    max_velocity: np.float_
    slowdown: np.float_
    acceleration: np.float_
    current_velocity: np.float_
    vx, vy, max_velocity, slowdown, acceleration = player[..., 6:11][0]

    vx = np.maximum(0, np.abs(vx) - slowdown * dt) * np.copysign(1, vx)
    vy = np.maximum(0, np.abs(vy) - slowdown * dt) * np.copysign(1, vy)

    vx += acceleration * direction[0] * dt
    vy += acceleration * direction[1] * dt

    current_velocity = np.hypot(vx, vy)
    if current_velocity > max_velocity:
        scale = max_velocity / current_velocity
        vx *= scale
        vy *= scale

    player[..., 6] = vx
    player[..., 7] = vy
    player[..., 0] += player[..., 6] * dt
    player[..., 1] += player[..., 7] * dt


def calc_collisions(enemies: np.ndarray, COLLISIONS_REPELLING: np.float_, dt: np.float_) -> None:
    max_dist_x: np.ndarray
    real_dist_y: np.ndarray
    dist_x: np.ndarray
    dist_y: np.ndarray
    dist: np.ndarray

    COLLISIONS_REPELLING = COLLISIONS_REPELLING * (1 / dt) / 120

    max_dist_x = enemies[..., 2] + enemies[..., 2][..., np.newaxis]
    real_dist_y = enemies[..., 3] + enemies[..., 3][..., np.newaxis]
    dist_x = enemies[..., 0] - enemies[..., 0][..., np.newaxis]
    dist_y = enemies[..., 1] - enemies[..., 1][..., np.newaxis]

    angle: np.ndarray = np.arctan2(dist_y, dist_x)

    min_dist = np.minimum(np.maximum(0, (max_dist_x - np.abs(dist_x))), np.maximum(0, (real_dist_y - np.abs(dist_y))))

    delta_x = min_dist * np.cos(angle) * COLLISIONS_REPELLING * dt
    delta_y = min_dist * np.sin(angle) * COLLISIONS_REPELLING * dt

    delta_x = np.triu(delta_x)
    delta_y = np.triu(delta_y)

    enemies[..., 0] -= np.sum(delta_x, axis=1)  # * np.random.uniform(0.6, 1, size=enemies[..., 0].shape)
    enemies[..., 0] += np.sum(delta_x, axis=0)  # * np.random.uniform(0.6, 1, size=enemies[..., 0].shape)
    enemies[..., 1] -= np.sum(delta_y, axis=1)  # * np.random.uniform(0.6, 1, size=enemies[..., 1].shape)
    enemies[..., 1] += np.sum(delta_y, axis=0)  # * np.random.uniform(0.6, 1, size=enemies[..., 1].shape)


def calc_damage(enemies: np.ndarray, bullets: np.ndarray, player: np.ndarray) -> None:
    max_dist_x: np.ndarray
    real_dist_y: np.ndarray
    dist_x: np.ndarray
    dist_y: np.ndarray

    max_dist_x = enemies[..., 2] + bullets[..., 2][..., np.newaxis]
    real_dist_y = enemies[..., 3] + bullets[..., 3][..., np.newaxis]
    dist_x = enemies[..., 0] - bullets[..., 0][..., np.newaxis]
    dist_y = enemies[..., 1] - bullets[..., 1][..., np.newaxis]

    dist = np.abs(dist_x / max_dist_x) + np.abs(dist_y / real_dist_y)
    bullet_indices = np.unique(np.where((np.abs(dist_x) < max_dist_x) & (np.abs(dist_y) < real_dist_y))[0])
    if len(bullet_indices):
        pass
    indices = np.argmin(dist, axis=1)[bullet_indices]
    counter = np.bincount(indices)[indices]

    damage = bullets[bullet_indices, 5] * counter
    damage = np.where(np.random.rand(*damage.shape) <= player[0, 19], damage * player[0, 18], damage)
    damage = np.maximum(0, damage - np.maximum(0, enemies[indices, 10] - bullets[bullet_indices, 11] * counter))
    enemies[indices, 4] -= damage

    enemies[np.setdiff1d(np.where(enemies[..., 4] <= 0), np.where(enemies[..., 8] > 0))] = np.array(
        [-1000, -1000, 0, 0, 0, 0, 0, 0, 2, 0, 0, 0, 0], dtype=np.float_)
    bullets[bullet_indices] = np.array([-2000, -2000, 0, 0, 0, 0, 0, 0, 1, 0, 1, 0], dtype=np.float_)


def calc_obstacles(entities: np.ndarray, obstacles: np.ndarray, kill: bool = False, bounce: bool = False) -> None:
    max_dist_x: np.ndarray
    real_dist_y: np.ndarray
    dist_x: np.ndarray
    dist_y: np.ndarray

    max_dist_x = entities[..., 2] + obstacles[..., 2][..., np.newaxis]
    real_dist_y = entities[..., 3] + obstacles[..., 3][..., np.newaxis]
    dist_x = entities[..., 0] - obstacles[..., 0][..., np.newaxis]
    dist_y = entities[..., 1] - obstacles[..., 1][..., np.newaxis]

    angle: np.ndarray = np.arctan2(dist_y, dist_x)
    ind_x: np.ndarray = np.array(np.where(
        (np.abs(np.cos(angle)) >= max_dist_x / np.hypot(real_dist_y, max_dist_x)) & (np.abs(dist_x) < max_dist_x) & (
                np.abs(dist_y) < real_dist_y)))
    ind_y: np.ndarray = np.array(np.where(
        (np.abs(np.cos(angle)) < max_dist_x / np.hypot(real_dist_y, max_dist_x)) & (np.abs(dist_x) < max_dist_x) & (
                np.abs(dist_y) < real_dist_y)))

    delta_x: np.ndarray = np.maximum(0, (max_dist_x - np.abs(dist_x))) * np.copysign(1, dist_x)
    delta_y: np.ndarray = np.maximum(0, (real_dist_y - np.abs(dist_y))) * np.copysign(1, dist_y)

    entities[ind_x[1], 0] += delta_x[ind_x[0], ind_x[1]]
    entities[ind_y[1], 1] += delta_y[ind_y[0], ind_y[1]]

    if kill:
        indices: np.ndarray = np.where((np.abs(dist_x) < max_dist_x) & (np.abs(dist_y) < real_dist_y))[1]
        entities[indices, :10] = np.array([-5000, -5000, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], dtype=np.float_)
    if bounce:
        entities[ind_x[1], 6] *= -1
        entities[ind_y[1], 7] *= -1
    else:
        entities[ind_x[1], 6] = 0
        entities[ind_y[1], 7] = 0


def calc_player_damage(enemies: np.ndarray, player: np.ndarray, dt: np.float_):
    max_dist_x = enemies[..., 2] + player[..., 2][..., np.newaxis]
    real_dist_y = enemies[..., 3] + player[..., 3][..., np.newaxis]
    dist_x = enemies[..., 0] - player[..., 0][..., np.newaxis]
    dist_y = enemies[..., 1] - player[..., 1][..., np.newaxis]
    player[..., 24] -= dt

    if player[0, 24] <= 0:
        indices = np.where((np.abs(dist_x) < max_dist_x) & (np.abs(dist_y) < real_dist_y))[1]
        indices = np.resize(indices, np.max(indices.shape[0]))
        damage = np.maximum(0, np.sum(enemies[indices, 5], axis=0) - player[0, 12])
        player[0, 4] -= damage
        player[..., 24] = player[..., 23]
        if player[0, 4] <= 0:
            exit()
        return damage > 0
    return 0


def calc_shooting(player: np.ndarray, bullets: np.ndarray, mouse_pos: np.ndarray, field: np.ndarray, Id: np.ndarray,
                  dt: np.float_):
    quotient, player[0, 25] = np.divmod(player[0, 25] + dt, player[0, 13])
    amount = np.int_(np.minimum(quotient, Id.shape[0]))
    arange = np.arange(amount, dtype=np.int_)

    if amount > 0:
        data = np.tile(np.array([player[0, 0], player[0, 1], player[0, 15], player[0, 16], 1, player[0, 17],
                                 0,
                                 0,
                                 0, 0, player[0, 21], player[0, 14]], dtype=np.float_), (amount, 1))

        mouse_pos = mouse_pos + field[0:2] - field[8:10] / 2
        angle = np.arctan2(mouse_pos[1] - player[0, 1], mouse_pos[0] - player[0, 0]) \
                + player[0, 20] * (np.random.random(amount) - 0.5) * 2

        data[..., 6] = player[0, 22] * np.cos(angle[...]) + player[0, 6]
        data[..., 7] = player[0, 22] * np.sin(angle[...]) + player[0, 7]

        rng = np.tile(arange[..., np.newaxis], (1, 2))
        data[..., 0:2] += data[..., 6:8] * player[..., 13] * rng

        indices = np.resize(Id, amount)

        bullets[indices] = data

        return indices
    return np.array([])


def calc_waves(wave: np.ndarray, enemy: np.ndarray, field: np.ndarray, Id: np.ndarray,
               dt: np.float_, types: np.ndarray):
    quotient, wave[2] = np.divmod(wave[2] + dt, wave[1])
    if quotient > 0:
        pass
    amount = np.int_(np.minimum(np.minimum(quotient, wave[4] - wave[3]), np.minimum(wave[4] - wave[3], Id.shape[0])))

    if amount > 0:
        data = np.tile(np.array([0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0, 0, 0], dtype=np.float_),
                       (amount, 1))
        data[..., 2:13] = types[np.random.randint(0, 4, size=amount)]
        data[..., 2:11] *= (
                1 - np.tile(data[..., 11][..., np.newaxis], (1, 9)) + np.tile(data[..., 11][..., np.newaxis],
                                                                              (1, 9)) * 2 * np.random.rand(amount, 9))

        lines = np.array((np.clip(field[0] - field[8] / 2 - field[10], 0, field[6]),
                          np.clip(field[0] + field[8] / 2 + field[10], 0, field[6]),
                          np.clip(field[1] - field[9] / 2 - field[10], 0, field[7]),
                          np.clip(field[1] + field[9] / 2 + field[10], 0, field[7])), dtype=np.int_)
        able_inds = np.intersect1d(np.where(lines > 0),
                                   np.union1d(np.where(lines[0:2] < field[6])[0],
                                              np.where(lines[2:4] < field[7])[0] + 2))
        inds = np.random.choice(able_inds, size=amount)
        able_segments = np.array([[lines[2], lines[3]],
                                  [lines[2], lines[3]],
                                  [lines[0], lines[1]],
                                  [lines[0], lines[1]], ])
        inds_x = np.where((inds == 0) | (inds == 1))[0]
        inds_y = np.where((inds == 2) | (inds == 3))[0]

        if inds_x.shape[0] > 0:
            data[inds_x, 1] = np.random.randint(able_segments[inds[inds_x]][0][0], able_segments[inds[inds_x]][0][1],
                                                size=inds_x.shape[0])
            data[inds_x, 0] = lines[inds[inds_x]]

        if inds_y.shape[0] > 0:
            data[inds_y, 0] = np.random.randint(able_segments[inds[inds_y]][0][0], able_segments[inds[inds_y]][0][1],
                                                size=inds_y.shape[0])
            data[inds_y, 1] = lines[inds[inds_y]]

        indices = np.resize(Id, amount)
        enemy[indices] = data
        wave[3] += amount
        return indices
    return np.array([])


def calc_creation_wave(wave, difficulty):
    if wave[7] <= wave[8]:
        number = wave[0] + 1
        print("update", number)
        spawn_delay_factor = (number / 9 + 1) * 2 * difficulty
        spawn_delay = 1 / spawn_delay_factor
        max_enemies = min(100, ((number / 7 + 1) * 10 * difficulty))
        need_to_kill = (number / 5 + 1) * 50 * difficulty
        wave[...] = np.array([number, spawn_delay, 0, 0, max_enemies, 0, 3, need_to_kill, 0], dtype=np.float_)
        print(wave)


def calc_killing_enemies(enemy: np.ndarray, field: np.ndarray):
    max_dist_x = field[8] / 2 + field[11]
    max_dist_y = field[9] / 2 + field[11]

    dist_x = enemy[..., 0] - field[..., 0]
    dist_y = enemy[..., 1] - field[..., 1]

    indices = np.setdiff1d(np.where((np.abs(dist_x) >= max_dist_x) | (np.abs(dist_y) >= max_dist_y))[0],
                           np.where(enemy[..., 8] > 0)[0])

    enemy[indices] = np.array([-1000, -1000, 0, 0, 0, 0, 0, 0, 5, 0, 0, 0, 0], dtype=np.float_)


@njit(fastmath=True)
def calc_cameraman(player: np.ndarray, filed: np.ndarray, dt: np.float_):
    speed = np.maximum(player[0, 8], np.hypot(player[0, 6], player[0, 7]))
    filed[0:2] += speed * ((player[0, 0:2] - filed[0:2]) / filed[2:4]) * dt
    filed[4:6] = np.clip(filed[0:2] - filed[8:10] / 2, 0, filed[6:8] - filed[8:10])
