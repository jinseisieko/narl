"""Soft collisions calculation"""
import numba
import numpy as np


@numba.jit(nopython=True, fastmath=True, parallel=True)
def calculate_soft_collision(player_data, enemy_data, projectiles_data, CHUNK_N_X, CHUNK_N_Y):
    enemies_positions = np.zeros((CHUNK_N_X, CHUNK_N_Y, 20, 7))
    projectiles_positions = np.zeros((CHUNK_N_X, CHUNK_N_Y, 40, 7))

    num_enemies = len(enemy_data)
    for i in numba.prange(num_enemies):
        num_enemy_instances = len(enemy_data[i])
        for j in numba.prange(num_enemy_instances):
            pass

    return player_data, enemy_data, projectiles_data
