import numba
import numpy as np

from Constants import *


@numba.njit(fastmath=True, nogil=True, parallel=True)
def calculate_Enemies(enemy_data, chunks_data, COLLISIONS_REPELLING):
    for i in numba.prange(len(chunks_data)):
        data_i = chunks_data[i]
        for j in numba.prange(len(data_i)):
            data_j = data_i[j]
            for k in numba.prange(len(data_j)):
                Id1 = int(data_j[k])
                x1, y1, half_size1 = enemy_data[Id1]
                for a in numba.prange(k + 1, len(data_j)):
                    Id2 = int(data_j[k])
                    x2, y2, half_size2 = enemy_data[Id2]

                    real_dist = half_size1 ** 2 + half_size2 ** 2
                    real_dist = np.sqrt(real_dist)

                    dist_x = x1 - x2
                    dist_y = y1 - y2
                    dist_sq = dist_x ** 2 + dist_y ** 2

                    if dist_sq < real_dist:
                        factor_x = (1 - abs(dist_x) / real_dist) * COLLISIONS_REPELLING
                        factor_y = (1 - abs(dist_y) / real_dist) * COLLISIONS_REPELLING

                        x1 += factor_x * math.copysign(1, dist_x)
                        x2 -= factor_x * math.copysign(1, dist_x)
                        y1 += factor_y * math.copysign(1, dist_y)
                        y2 -= factor_y * math.copysign(1, dist_y)

                enemy_data[Id1] = np.array([x1, y1, half_size1])
    return enemy_data


class Chunks:
    def __init__(self) -> None:
        super().__init__()
        self.chunks = [[[] for _ in range(CHUNK_N_X)] for _ in range(CHUNK_N_Y)]

    def add(self, obj, ind) -> None:
        if not (obj in self.chunks[ind[0]][ind[1]]):
            self.chunks[ind[0]][ind[1]].append(obj)

    def del_(self, obj, ind) -> None:
        if obj in self.chunks[ind[0]][ind[1]]:
            self.chunks[ind[0]][ind[1]].remove(obj)

    def move(self, obj, last_ind, new_ind) -> None:
        if obj in self.chunks[last_ind[0]][last_ind[1]]:
            self.chunks[last_ind[0]][last_ind[1]].remove(obj)
        self.chunks[new_ind[0]][new_ind[1]].append(obj)

    def calculate_collisions(self) -> None:
        for line in self.chunks:
            for chunk in line:
                for i, obj1 in enumerate(chunk):
                    for obj2 in chunk[i + 1:]:
                        if obj1.name == "Enemy" and obj2.name == "Enemy":
                            obj2.x, obj2.y = calculate_Enemies(obj1.size,
                                                               obj2.size,
                                                               obj1.x, obj1.y,
                                                               obj2.x, obj2.y, COLLISIONS_REPELLING)

                        if obj1.name == "Projectile" and obj2.name == "Enemy":
                            if obj1.rect.colliderect(obj2.rect):
                                obj1.kill()
                                obj2.get_damage(obj1.damage)

                        if obj1.name == "Enemy" and obj2.name == "Projectile":
                            if obj1.rect.colliderect(obj2.rect):
                                obj2.kill()
                                obj1.get_damage(obj2.damage)
