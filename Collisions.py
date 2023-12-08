import math

import pygame

from Constants import *


class Chunks:
    def __init__(self) -> None:
        super().__init__()
        self.chunks = [[[] for _ in range(CHUNK_N_X)] for _ in range(CHUNK_N_Y)]

    def add(self, obj, ind) -> None:
        self.chunks[ind[0]][ind[1]].append(obj)

    def move(self, obj, last_ind, new_ind) -> None:
        self.chunks[last_ind[0]][last_ind[1]].remove(obj)
        self.chunks[new_ind[0]][new_ind[1]].append(obj)

    def calculate_collisions(self, ind) -> None:
        chunk = self.chunks[ind[0]][ind[1]]

        for i, obj1 in enumerate(chunk):
            for obj2 in chunk[i+1:]:
                if obj1.get_name() == "Enemy" and obj2.get_name() == "Enemy":
                    if obj2.rect.colliderect(obj1.rect):
                        size_1 = obj1.size // 2
                        size_2 = obj2.size // 2
                        real_dist = size_1 + size_2
                        dist_x = obj1.x - obj2.x
                        dist_y = obj1.y - obj2.y
                        dist = math.hypot(dist_x, dist_y)
                        if dist < real_dist:
                            if dist_x == 0:
                                obj2.x -= 1e-6
                                continue
                            if dist_y == 0:
                                obj2.y -= 1e-6
                                continue
                            obj1.dx += real_dist / dist_x * COLLISIONS_REPELLING
                            obj2.dx -= real_dist / dist_x * COLLISIONS_REPELLING
                            obj1.dy += real_dist / dist_y * COLLISIONS_REPELLING
                            obj2.dy -= real_dist / dist_y * COLLISIONS_REPELLING
