"""Soft collisions calculation"""
import numba
import numpy as np


@numba.jit(nopython=True, fastmath=True, parallel=True)
def calculate_soft_collision(player_data: np.zeros, enemy_data: np.zeros, projectiles_data: np.zeros,
                             positions: np.array, CHUNK_N_X: int,
                             CHUNK_N_Y: int, collision_speed: float):
    """Soft collisions calculation"""
    enemies_new_data = np.zeros((CHUNK_N_X, CHUNK_N_Y, 20, 9))
    projectiles_positions = np.zeros((CHUNK_N_X, CHUNK_N_Y, 40, 9))

    # print(positions)

    for pos in positions:
        for i in range(len(enemy_data[pos[0]][pos[1]])):
            for j in range(len(enemy_data[pos[0]][pos[1]])):
                if i == j:
                    continue
                else:
                    enemy_first = enemy_data[pos[0]][pos[1]][i]
                    enemy_second = enemy_data[pos[0]][pos[1]][j]
                    size: int = max(enemy_first[6], enemy_second[6])
                    distance_x: float = enemy_first[0] - enemy_second[0]
                    distance_y: float = enemy_first[1] - enemy_second[1]
                    if abs(distance_x) < size and abs(distance_y) < size:
                        enemies_new_data[pos[0]][pos[1]][i][0] = enemy_first[0] - collision_speed * (
                                1 - distance_x / size)
                        enemies_new_data[pos[0]][pos[1]][j][0] = enemy_second[0] + collision_speed * (
                                1 - distance_x / size)
                        enemies_new_data[pos[0]][pos[1]][i][1] = enemy_first[1] + collision_speed * (
                                1 - distance_y / size)
                        enemies_new_data[pos[0]][pos[1]][j][1] = enemy_second[1] - collision_speed * (
                                1 - distance_y / size)

                        enemies_new_data[pos[0]][pos[1]][i][8] = enemy_first[8]
                        enemies_new_data[pos[0]][pos[1]][j][8] = enemy_second[8]

                    pass

    # num_enemies = len(enemy_data)
    # for i in numba.prange(num_enemies):
    #     num_enemy_instances = len(enemy_data[i])
    #     for j in numba.prange(num_enemy_instances):
    #         pass

    return player_data, enemies_new_data, projectiles_data
