import pygame
import sys

pygame.init()

# Определение размеров игрового поля
width, height = 800, 600
game_field = pygame.Surface((width, height))

# Определение размеров отображаемой области
view_width, view_height = 400, 300

# Создание окна
screen = pygame.display.set_mode((view_width, view_height))
pygame.display.set_caption("Отрисовка ограниченной области игрового поля")

# Определение цветов
white = (255, 255, 255)
red = (255, 0, 0)

# Заполнение игрового поля цветом
game_field.fill(white)

# Рисование красного квадрата на игровом поле
pygame.draw.rect(game_field, red, (50, 50, 50, 50))

# Основной цикл игры
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Отображение части игрового поля на экране
    screen.blit(game_field, (0, 0), (0, 0, view_width, view_height))

    pygame.display.flip()

pygame.quit()
sys.exit()
