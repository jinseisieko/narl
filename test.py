from typing import Any

import pygame
import sys


pygame.init()


class Test(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load(r"image\player50x50.png")
        self.rect = self.image.get_rect(center=(view_width // 2, view_height // 2))

    def update(self, *args: Any, **kwargs: Any) -> None:
        super().update(*args, **kwargs)
        self.rect.x += 0.1
        print(self.rect.x)


# Определение размеров игрового поля
width, height = 800, 600
game_field = pygame.Surface((width, height))

# Определение размеров отображаемой области
view_width, view_height = 300, 300

# Создание окна
screen = pygame.display.set_mode((view_width, view_height))
pygame.display.set_caption("Отрисовка ограниченной области игрового поля")

# Определение цветов
white = (255, 255, 255)
red = (255, 0, 0)

# Заполнение игрового поля цветом
game_field.fill(white)
player = Test()
# Рисование красного квадрата на игровом поле
pygame.draw.rect(game_field, red, (50, 50, 50, 50))
gr = pygame.sprite.Group(player)
gr.add()
# Основной цикл игры
running = True
i = 0
while running:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    gr.update()
    game_field.fill(white)
    gr.draw(game_field)


    # Отображение части игрового поля на экране
    screen.blit(game_field, (0, 0), (0, 0, view_width, view_height))

    pygame.display.flip()
    pygame.time.Clock().tick(60)

pygame.quit()
sys.exit()
