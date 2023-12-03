import pygame
import sys

import ImageSprites

# Инициализация Pygame
pygame.init()

# Размеры экрана
screen_width, screen_height = 800, 600

# Создание окна
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Часть поля")

# Загрузка изображения поля (предположим, что у вас есть изображение "field.jpg")
field_image = ImageSprites.sprites[f'texture_grass_{1}']

# Размеры поля
field_width, field_height = field_image.get_size()

# Область, которую вы хотите отобразить (пример: от (100, 100) до (500, 400))
crop_rect = pygame.Rect(100, 100, 300, 200)

# Основной цикл
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Очистка экрана
    screen.fill((255, 255, 255))

    # Отображение только части изображения поля
    screen.blit(field_image, (0, 0), crop_rect)

    # Обновление экрана
    pygame.display.flip()

# Завершение программы
pygame.quit()
sys.exit()
