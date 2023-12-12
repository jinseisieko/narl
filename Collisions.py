import numba

from Constants import *


@numba.njit(fastmath=True)
def calculate_Enemies(obj1size, obj2size, obj1x, obj1y, obj2x, obj2y, COLLISIONS_REPELLING):
    size_1 = obj1size // 2
    size_2 = obj2size // 2
    real_dist = size_1 + size_2
    repelling_factor = COLLISIONS_REPELLING

    dist_x = obj1x - obj2x
    dist_y = obj1y - obj2y
    dist_sq = dist_x ** 2 + dist_y ** 2

    if dist_sq < real_dist ** 2:
        factor_x = (1 - abs(dist_x) / real_dist) * repelling_factor
        factor_y = (1 - abs(dist_y) / real_dist) * repelling_factor

        obj1x += factor_x * math.copysign(1, dist_x)
        obj2x -= factor_x * math.copysign(1, dist_x)
        obj1y += factor_y * math.copysign(1, dist_y)
        obj2y -= factor_y * math.copysign(1, dist_y)

    return obj2x, obj2y


class Chunks:
    def __init__(self) -> None:
        super().__init__()
        self.chunks = [[[] for _ in range(CHUNK_N_X)] for _ in range(CHUNK_N_Y)]

    def add(self, obj, ind) -> None:
        self.chunks[ind[0]][ind[1]].append(obj)

    def del_(self, obj, ind) -> None:
        if obj in self.chunks[ind[0]][ind[1]]:
            self.chunks[ind[0]][ind[1]].remove(obj)

    def move(self, obj, last_ind, new_ind) -> None:
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
                                obj2.hp -= obj1.damage
                                if obj2.hp < 0:
                                    obj2.kill()

                        if obj1.name == "Enemy" and obj2.name == "Projectile":
                            if obj1.rect.colliderect(obj2.rect):
                                obj2.kill()
                                obj1.hp -= obj2.damage
                                if obj1.hp < 0:
                                    obj1.kill()

