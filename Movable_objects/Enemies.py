"""classes Enemy"""
from Image import Image
from Movable_objects.Entity import *


class Enemy(Entity):
    def __init__(self, data: np.array, matrix: np.ndarray, Id: int, image: str, field, free_Ids: set):
        super().__init__(matrix, Id, image, field, free_Ids)
        self.matrix[Id] = data
        self.image: Image = Image(int(self.matrix[self.Id, 2]), int(self.matrix[self.Id, 3]), r"image/test_enemy.png")

    def draw(self) -> None:
        self.field.field.blit(self.image.img, (
            self.matrix[self.Id, X] - self.matrix[self.Id, SIZE_X],
            self.matrix[self.Id, Y] - self.matrix[self.Id, SIZE_Y]))

# class Enemy(pygame.sprite.Sprite):
#     def __init__(self, player, x: float, y: float, chunks: Chunks, i: int):
#         super().__init__()
#         self.image = pygame.Surface((self.size, self.size))
#         # self.image.fill([random.randint(5, 200) for _ in range(3)])
#         # pygame.draw.rect(self.image, 0, (self.size // 5, self.size // 3, self.size // 7, self.size // 5), width=4)
#         self.speed: float = DEFAULT_ENEMY_ENEMY_SPEED
#
#         self.rect = self.image.get_rect()
#         self.x: float = x - DEFAULT_ENEMY_ENEMY_SIZE // 2
#         self.y: float = y - DEFAULT_ENEMY_ENEMY_SIZE // 2
#
#         self.outlines_rect = (0, 0, self.size, self.size)
#         self.left_eye_rect = (self.size // 4, self.size // 3, self.size // 7, self.size // 5)
#         self.right_eye_rect = (self.size // 5 * 3, self.size // 3, self.size // 7, self.size // 5)
#         self.half_size = self.size // 2
#
#         self.image.fill((255, int(255 / self.mhp * self.hp), int(255 / self.mhp * self.hp)))
#         pygame.draw.rect(self.image, 0, self.outlines_rect, width=4)
#         pygame.draw.rect(self.image, 0, self.left_eye_rect)
#         pygame.draw.rect(self.image, 0, self.right_eye_rect)
#
#         self.dx: float = 0.
#         self.dy: float = 0.
#
#         self.name: str = "Enemy"
#
#         self.player = player
#         self.angle: float = 0.
#
#         self.chunks: Chunks = chunks
#         self.ind: list[int, int] = [int(self.y // CHUNK_SIZE), int(self.x // CHUNK_SIZE)]
#         self.last_ind: list[int, int] = self.ind
#         self.chunks.add(self, self.ind)
#         self.i = i
#
#     def update(self, arr) -> None:
#         self.x, self.y, _ = arr[self.i]
#
#         # self.x = max(0, min(FIELD_WIDTH - self.half_size, self.x))
#         # self.y = max(0, min(FIELD_HEIGHT - self.half_size, self.y))
#         # self.ind = [int(self.y / CHUNK_SIZE), int(self.x / CHUNK_SIZE)]
#         # if self.ind[0] != self.last_ind[0] or self.ind[1] != self.last_ind[1]:
#         #    self.chunks.move(self, self.last_ind, self.ind)
#         #    self.last_ind = self.ind
#
#         self.rect.x = self.x - self.half_size
#         self.rect.y = self.y - self.half_size
