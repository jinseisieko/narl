import math

import numba

from Constants import *


@numba.jit(nopython=True, fastmath=True)
def calculate(obj1dx, obj1dy, obj2dx, obj2dy, obj1size, obj2size, obj1x, obj1y, obj2x, obj2y):
    size_1 = obj1size // 2
    size_2 = obj2size // 2
    real_dist = size_1 + size_2
    dist_x = obj1x - obj2x
    dist_y = obj1y - obj2y
    dist = math.hypot(dist_x, dist_y)
    if dist < real_dist:
        if dist < real_dist:
            if dist_x == 0:
                return obj1dx, obj1dy, obj2dx, obj2dy, obj2x, obj2y
            if dist_y == 0:
                return obj1dx, obj1dy, obj2dx, obj2dy, obj2x, obj2y
            obj1dx += real_dist / dist_x * COLLISIONS_REPELLING
            obj2dx -= real_dist / dist_x * COLLISIONS_REPELLING
            obj1dy += real_dist / dist_y * COLLISIONS_REPELLING
            obj2dy -= real_dist / dist_y * COLLISIONS_REPELLING
    return obj1dx, obj1dy, obj2dx, obj2dy, obj2x, obj2y


class Chunks:
    def __init__(self) -> None:
        super().__init__()
        self.chunks = [[[] for _ in range(CHUNK_N_X)] for _ in range(CHUNK_N_Y)]

    def add(self, obj, ind) -> None:
        self.chunks[ind[0]][ind[1]].append(obj)

    def move(self, obj, last_ind, new_ind) -> None:
        self.chunks[last_ind[0]][last_ind[1]].remove(obj)
        self.chunks[new_ind[0]][new_ind[1]].append(obj)

    def calculate_collisions(self) -> None:
        for line in self.chunks:
            for chunk in line:
                for i, obj1 in enumerate(chunk):
                    for obj2 in chunk[i + 1:]:
                        obj1.dx, obj1.dy, obj2.dx, obj2.dy, obj2.x, obj2.y = calculate(obj1.dx, obj1.dy, obj2.dx,
                                                                                       obj2.dy, obj1.size, obj2.size,
                                                                                       obj1.x, obj1.y, obj2.x, obj2.y)
                        # size_1 = obj1.size // 2
                        # size_2 = obj2.size // 2
                        # real_dist = size_1 + size_2
                        # dist_x = obj1.x - obj2.x
                        # dist_y = obj1.y - obj2.y
                        # dist = math.hypot(dist_x, dist_y)
                        # if dist < real_dist:
                        #     if dist < real_dist:
                        #         if dist_x == 0:
                        #             obj2.x -= 1e-6
                        #             return
                        #         if dist_y == 0:
                        #             obj2.y -= 1e-6
                        #             return
                        #         obj1.dx += real_dist / dist_x * COLLISIONS_REPELLING
                        #         obj2.dx -= real_dist / dist_x * COLLISIONS_REPELLING
                        #         obj1.dy += real_dist / dist_y * COLLISIONS_REPELLING
                        #         obj2.dy -= real_dist / dist_y * COLLISIONS_REPELLING
