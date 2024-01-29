import pygame
import sys

# Инициализация Pygame
pygame.init()

# Размеры окна
width, height = 800, 600

# Создание окна
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Прозрачная поверхность Pygame")

# Прозрачный цвет с альфа-каналом (R, G, B, A)
transparent_color = (255, 0, 0, 128)

# Создание прозрачной Surface
transparent_surface = pygame.Surface((200, 200), pygame.SRCALPHA)
transparent_surface.fill(transparent_color)

# Основной цикл программы
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Очистка экрана
    screen.fill(0)

    # Рисование прозрачной Surface на экране
    screen.blit(transparent_surface, (300, 200))

    # Обновление экрана
    pygame.display.flip()
