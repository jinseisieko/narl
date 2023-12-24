import numpy as np

# to CONSTS

MAX_ENTITIES = 1000
MAX_BULLETS = 1000
MAX_OBSTACLES = 1000

entity = np.zeros((MAX_ENTITIES, 10), dtype=np.float_)
bullets = np.zeros((MAX_BULLETS, 8), dtype=np.float_)
player = np.zeros(20, dtype=np.float_)
obstacles = np.zeros((MAX_OBSTACLES, 5), dtype=np.float_)

entity_ids = set(range(MAX_ENTITIES))
bullet_ids = set(range(MAX_BULLETS))
obstacles_ids = set(range(MAX_OBSTACLES))


def calc_dist(first: np.ndarray, second: np.ndarray) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray]:
    dist_x_all: np.ndarray = first[:, 0] - second[:, 0][:, np.newaxis]
    dist_y_all: np.ndarray = first[:, 1] - second[:, 1][:, np.newaxis]

    real_dist_x: np.ndarray = first[:, 2] - second[:, 2][:, np.newaxis]
    real_dist_y: np.ndarray = first[:, 3] - second[:, 3][:, np.newaxis]

    dist_x: np.ndarray = np.where((np.abs(dist_y_all) <= real_dist_y) & (np.abs(dist_x_all) <= real_dist_x),
                                  real_dist_x, dist_x_all)
    dist_y: np.ndarray = np.where((np.abs(dist_x_all) <= real_dist_x) & (np.abs(dist_y_all) <= real_dist_y),
                                  real_dist_y, dist_y_all)

    return real_dist_x, real_dist_y, dist_x, dist_y


def calc_enemy_direction(entity: np.ndarray, x: np.float_, y: np.float_) -> None:
    angle = np.arctan2(entity[..., 0] - x, entity[..., 1] - y)
    # entity[:, 8] = angle
    entity[..., 6] = np.cos(angle) * entity[..., 9]
    entity[..., 7] = np.sin(angle) * entity[..., 9]


def calc_movements(objects: np.ndarray, dt: np.float_) -> None:
    objects[:0] += objects[:6] * dt
    objects[:1] += objects[:7] * dt


def calc_player_movement(player: np.ndarray, direction: np.ndarray, dt: np.float_) -> None:
    vx: np.float_
    vy: np.float_
    max_velocity: np.float_
    slowdown: np.float_
    acceleration: np.float_
    vx, vy, max_velocity, slowdown, acceleration = player[6:11]

    vx = np.maximum(0, np.abs(vx) - slowdown * dt) * np.sign(vx)
    vy = np.maximum(0, np.abs(vy) - slowdown * dt) * np.sign(vy)

    vx += acceleration * direction[0] * dt
    vy += acceleration * direction[1] * dt

    current_velocity_magnitude: np.float_ = np.hypot(vx, vy)
    if current_velocity_magnitude > max_velocity:
        scale = max_velocity / current_velocity_magnitude
        vx *= scale
        vy *= scale

    player[6] = vx
    player[7] = vy

    player[0] += player[6] * dt
    player[1] += player[7] * dt



def calc_collisions(entity: np.ndarray, COLLISIONS_REPELLING: np.float_) -> None:
    real_dist_x: np.ndarray
    real_dist_y: np.ndarray
    dist_x: np.ndarray
    dist_y: np.ndarray
    real_dist_x, real_dist_y, dist_x, dist_y = calc_dist(entity, entity)

    delta_x: np.ndarray = (1 - np.abs(dist_x) / real_dist_x) * COLLISIONS_REPELLING * np.sign(dist_x)
    delta_y: np.ndarray = (1 - np.abs(dist_y) / real_dist_y) * COLLISIONS_REPELLING * np.sign(dist_y)

    entity[:, 0] += np.sum(delta_x, axis=1)
    entity[:, 0] -= np.sum(delta_x, axis=0)
    entity[:, 1] += np.sum(delta_y, axis=1)
    entity[:, 1] -= np.sum(delta_y, axis=0)

    # rows, cols = np.indices(entity.shape)
    #
    # entity[rows, 0] += delta_x
    # entity[cols, 0] -= delta_x
    # entity[rows, 0] += delta_y
    # entity[cols, 0] -= delta_y


def calc_obstacles(entity: np.ndarray, obstacles: np.ndarray) -> None:
    real_dist_x: np.ndarray
    real_dist_y: np.ndarray
    dist_x: np.ndarray
    dist_y: np.ndarray
    real_dist_x, real_dist_y, dist_x, dist_y = calc_dist(entity, obstacles)

    delta_x: np.ndarray = (real_dist_x - np.abs(dist_x)) * np.sign(dist_x)
    delta_y: np.ndarray = (real_dist_y - np.abs(dist_y)) * np.sign(dist_y)

    entity[:, 0] += delta_x
    entity[:, 1] += delta_y


def calc_damage(entity: np.ndarray, bullets: np.ndarray) -> None:
    real_dist_x: np.ndarray
    real_dist_y: np.ndarray
    dist_x: np.ndarray
    dist_y: np.ndarray
    real_dist_x, real_dist_y, dist_x, dist_y = calc_dist(entity, bullets)

    dist = np.hypot(dist_x, dist_y)
    damage = np.argmin(dist, axis=1)

    entity[:, 4] = np.where(dist[damage] < np.max(dist), entity[:, 4], entity[:, 4] - bullets[:, 5])
    bullets[:, 4] = np.where(dist[damage] < np.max(dist), 1.0, 0.0)

    # damage_x: np.ndarray = np.argmin(dist_x, axis=1)
    # damage_y: np.ndarray = np.argmin(dist_y, axis=1)
    #
    # damage_x = np.where[dist_x[damage_x] <= real_dist_x[damage_x], -1, bullets[damage_x, 5]]
    #
    # damage_x = np.where[entity[:, damage_x] <= real_dist_x[:, damage_x], -1, damage_x]
    # entity[:, 4] -=
