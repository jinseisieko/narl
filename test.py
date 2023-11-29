import pygame
import sys

# Инициализация Pygame
pygame.init()

# Размеры окна
width, height = 800, 600

# Создание окна
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Двойное нажатие клавиши в Pygame")

# Цвета
black = (0, 0, 0)
white = (255, 255, 255)

# Шрифт
font = pygame.font.Font(None, 36)

# Переменные для отслеживания двойного нажатия
double_click_interval = 500  # интервал в миллисекундах между двумя нажатиями для считывания как двойное нажатие
last_click_time = 0
double_click = False

# Основной цикл игры
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                # Проверяем, прошло ли достаточно времени с момента последнего нажатия
                current_time = pygame.time.get_ticks()
                if current_time - last_click_time < double_click_interval:
                    # Это двойное нажатие
                    double_click = True
                    print("Двойное нажатие!")
                else:
                    # Это первое нажатие
                    double_click = False

                # Обновляем время последнего нажатия
                last_click_time = current_time

    # Отрисовка
    screen.fill(white)

    # Отображение статуса двойного нажатия
    text = font.render("Двойное нажатие: {}".format(double_click), True, black)
    screen.blit(text, (10, 10))

    pygame.display.flip()

    # Ограничение частоты кадров
    pygame.time.Clock().tick(60)
