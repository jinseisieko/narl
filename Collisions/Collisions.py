import numpy as np
from Constants import MAX_ENEMIES, MAX_BULLETS, MAX_OBSTACLES

enemies = np.tile(np.array([-100, -100, 0, 0, 0, 0, 0, 0, 1, 0], dtype=np.float_), (MAX_ENEMIES, 1))
bullets = np.tile(np.array([-200, -200, 0, 0, 0, 0, 0, 0, 1, 0, 1], dtype=np.float_), (MAX_BULLETS, 1))
obstacles = np.tile(np.array([-300, -300, 0, 0], dtype=np.float_), (MAX_OBSTACLES, 1))
player = np.zeros((1, 22), dtype=np.float_)

entity_ids = set(range(MAX_ENEMIES))
bullet_ids = set(range(MAX_BULLETS))
obstacles_ids = set(range(MAX_OBSTACLES))


def calc_enemy_direction(entity: np.ndarray, x: np.float_, y: np.float_) -> None:
    k = 10
    k_2 = k / 2
    x = x + np.random.rand(*entity[..., 6].shape) * k - k_2
    y = y + np.random.rand(*entity[..., 7].shape) * k - k_2

    angle = np.arctan2(y - entity[..., 1], x - entity[..., 0])
    entity[..., 6] = np.cos(angle) * entity[..., 9]
    entity[..., 7] = np.sin(angle) * entity[..., 9]


def calc_movements(objects: np.ndarray, dt: np.float_) -> None:
    objects[..., 0] += objects[..., 6] * dt
    objects[..., 1] += objects[..., 7] * dt


def calc_bullet_movements(bullet: np.ndarray, dt: np.float_):
    bullet[..., 0] += bullet[..., 6] * dt
    bullet[..., 1] += bullet[..., 7] * dt
    bullet[..., 9] += dt

    indices = np.where(bullet[..., 9] >= bullet[..., 10])
    bullet[indices] = np.array([-100, -100, 0, 0, 0, 0, 0, 0, 1, 0, 1])


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


def calc_dist(first: np.ndarray, second: np.ndarray) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
    real_dist: np.ndarray = first[..., 2] + second[..., 2][..., np.newaxis]
    dist_x: np.ndarray = first[..., 0] - second[..., 0][..., np.newaxis]
    dist_y: np.ndarray = first[..., 1] - second[..., 1][..., np.newaxis]

    return real_dist, dist_x, dist_y


def calc_collisions(entity: np.ndarray, COLLISIONS_REPELLING: np.float_, dt: np.float_) -> None:
    real_dist: np.ndarray
    dist_x: np.ndarray
    dist_y: np.ndarray
    dist: np.ndarray

    real_dist = entity[..., 2] + entity[..., 2][..., np.newaxis]
    dist_x = entity[..., 0] - entity[..., 0][..., np.newaxis]
    dist_y = entity[..., 1] - entity[..., 1][..., np.newaxis]

    dist = np.hypot(dist_x, dist_y)

    delta_x: np.ndarray = np.where(dist < real_dist,
                                   (1 - np.abs(dist_x) / real_dist) * COLLISIONS_REPELLING * np.copysign(1, dist_x),
                                   0) * dt
    delta_y: np.ndarray = np.where(dist < real_dist,
                                   (1 - np.abs(dist_y) / real_dist) * COLLISIONS_REPELLING * np.copysign(1, dist_y),
                                   0) * dt

    delta_x = np.triu(delta_x)
    delta_y = np.triu(delta_y)

    entity[..., 0] -= np.sum(delta_x, axis=1)  # * np.random.uniform(0.6, 1, size=entity[..., 0].shape)
    entity[..., 0] += np.sum(delta_x, axis=0)  # * np.random.uniform(0.6, 1, size=entity[..., 0].shape)
    entity[..., 1] -= np.sum(delta_y, axis=1)  # * np.random.uniform(0.6, 1, size=entity[..., 1].shape)
    entity[..., 1] += np.sum(delta_y, axis=0)  # * np.random.uniform(0.6, 1, size=entity[..., 1].shape)


def calc_damage(entity: np.ndarray, bullets: np.ndarray) -> None:
    real_dist: np.ndarray
    dist_x: np.ndarray
    dist_y: np.ndarray

    real_dist = entity[..., 2] + bullets[..., 2][..., np.newaxis]
    dist_x = entity[..., 0] - bullets[..., 0][..., np.newaxis]
    dist_y = entity[..., 1] - bullets[..., 1][..., np.newaxis]

    dist = np.hypot(dist_x, dist_y)

    bullet_indices = np.unique(np.where(dist < real_dist)[0])
    indices = np.argmax(np.where(dist < real_dist, 1, 0), axis=1)[bullet_indices]
    indices, damage = np.unique(indices, return_counts=True)
    entity[indices, 4] -= damage

    entity[np.where(entity[..., 4] <= 0)] = np.array([-100, -100, 0, 0, 0, 0, 0, 0, 1, 0])
    bullets[bullet_indices] = np.array([-100, -100, 0, 0, 0, 0, 0, 0, 1, 0, 1])


def calc_obstacles(entity: np.ndarray, obstacles: np.ndarray, kill: bool = False) -> None:
    real_dist_x: np.ndarray
    real_dist_y: np.ndarray
    dist_x: np.ndarray
    dist_y: np.ndarray

    real_dist_x = entity[..., 2] + obstacles[..., 2][..., np.newaxis]
    real_dist_y = entity[..., 3] + obstacles[..., 3][..., np.newaxis]
    dist_x = entity[..., 0] - obstacles[..., 0][..., np.newaxis]
    dist_y = entity[..., 1] - obstacles[..., 1][..., np.newaxis]

    angle: np.ndarray = np.arctan2(dist_y, dist_x)
    ind_x: np.ndarray = np.array(np.where(
        (np.abs(np.cos(angle)) >= real_dist_x / np.hypot(real_dist_y, real_dist_x)) & (np.abs(dist_x) < real_dist_x) & (
                np.abs(dist_y) < real_dist_y)))
    ind_y: np.ndarray = np.array(np.where(
        (np.abs(np.cos(angle)) < real_dist_x / np.hypot(real_dist_y, real_dist_x)) & (np.abs(dist_x) < real_dist_x) & (
                np.abs(dist_y) < real_dist_y)))

    delta_x: np.ndarray = np.maximum(0, (real_dist_x - np.abs(dist_x))) * np.copysign(1, dist_x)
    delta_y: np.ndarray = np.maximum(0, (real_dist_y - np.abs(dist_y))) * np.copysign(1, dist_y)

    entity[ind_x[1], 0] += delta_x[*ind_x]
    entity[ind_y[1], 1] += delta_y[*ind_y]
    entity[ind_x[1], 6] = 0
    entity[ind_y[1], 7] = 0

    if kill:
        indices: np.ndarray = np.where((np.abs(dist_x) < real_dist_x) & (np.abs(dist_y) < real_dist_y))[1]
        entity[indices, :10] = np.array([-100, -100, 0, 0, 0, 0, 0, 0, 1, 0])