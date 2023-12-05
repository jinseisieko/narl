"""Soft collisions calculation"""

import numba
import numpy as np


@numba.jit(nopython=True, fastmath=True, parallel=True)
def calculate_soft_collision(player_data: np.zeros, enemy_data: np.zeros, projectiles_data: np.zeros,
                             positions: np.array, CHUNK_N_X: int,
                             CHUNK_N_Y: int, REPELLING: float):
    """Soft collisions calculation"""
    enemies_new_data = np.zeros((CHUNK_N_X, CHUNK_N_Y, 20, 9))
    projectiles_positions = np.zeros((CHUNK_N_X, CHUNK_N_Y, 40, 9))

    # print(positions)

    for pos in positions:
        enemy_chunk = enemy_data[pos[0]][pos[1]]
        for i in numba.prange(len(enemy_chunk)):
            for j in numba.prange(i + 1, len(enemy_chunk)):
                enemy_first = enemy_chunk[i]
                enemy_second = enemy_chunk[j]
                if enemy_first[8] == 0 or enemy_second[8] == 0:
                    break

                size = max(enemy_first[6], enemy_second[6]) /2
                distance_x = enemy_first[0] - enemy_second[0]
                distance_y = enemy_first[1] - enemy_second[1]

                opposite_ratio_x = 1 - distance_x / size
                opposite_ratio_y = 1 - distance_y / size

                v1x = enemy_first[2]
                v1y = enemy_first[3]

                v2x = enemy_second[2]
                v2y = enemy_second[3]

                if abs(distance_x) < size and abs(distance_y) < size:
                    # Update velocities based on soft collision

                    v1x += REPELLING * distance_x
                    v1y += REPELLING * distance_y

                    v2x -= REPELLING * distance_x
                    v2y -= REPELLING * distance_y

                    enemies_new_data[pos[0]][pos[1]][i][2] += enemy_first[2] + v1x
                    enemies_new_data[pos[0]][pos[1]][i][3] += enemy_first[3] * v1y

                    enemies_new_data[pos[0]][pos[1]][j][2] += enemy_second[2] + v2x
                    enemies_new_data[pos[0]][pos[1]][j][3] += enemy_second[3] + v2y

                enemies_new_data[pos[0]][pos[1]][i][8] = enemy_first[8]
                enemies_new_data[pos[0]][pos[1]][j][8] = enemy_second[8]

    # num_enemies = len(enemy_data)
    # for i in numba.prange(num_enemies):
    #     num_enemy_instances = len(enemy_data[i])
    #     for j in numba.prange(num_enemy_instances):
    #         pass

    return player_data, enemies_new_data, projectiles_data
