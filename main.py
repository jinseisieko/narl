import sys
import pygame
from consts import *
from game_sprites import *
from gameplay import Room
from console import reproduce_command
from improvements import *

pygame.init()

COLOR_INACTIVE = (150, 150, 150)
COLOR_ACTIVE = (0, 0, 0)
FONT = pygame.font.Font(None, 27)


class InputBox:  # консоль
    def __init__(self, x, y, w, h, text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = COLOR_INACTIVE
        self.text = text
        self.txt_surface = FONT.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
            self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    reproduce_command(self.text, player)
                    player.update_characteristics()
                    self.text = ''
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                self.txt_surface = FONT.render(self.text, True, self.color)

    def update(self):
        width = max(200, self.txt_surface.get_width() + 10)
        self.rect.w = width

    def draw(self, screen):
        screen.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 5))
        pygame.draw.rect(screen, self.color, self.rect, 2)

    def open_console(self):
        self.active = True
        self.text = ''
        self.color = COLOR_ACTIVE if self.active else COLOR_INACTIVE


# создание частиц
def create_particles(x, y, direction_, deviation, size_, color_, n):
    particles_ = []
    for _ in range(n):
        rand_deviation = (random.uniform(-deviation, deviation), random.uniform(-deviation, deviation))

        particle_ = {
            'pos': [x, y],
            'dir': [direction_[0] + rand_deviation[0], direction_[1] + rand_deviation[1]],
            'size': size_,
            'color': color_,
            'life': 20
        }
        particles_.append(particle_)
    return particles_


# группы
all_sprites = pygame.sprite.Group()
projectiles = pygame.sprite.Group()
enemies = pygame.sprite.Group()
particles = []

# игрок
player = Player()
all_sprites.add(player)

# класс комнаты
room_number = 1
room = Room(room_number, player)
room.add(all_sprites, enemies)

screen = pygame.display.set_mode((WIDTH_, HEIGHT))
pygame.display.set_caption("NARL")
clock = pygame.time.Clock()

# шрифты
font_room = pygame.font.Font(None, 40)
font_ch = pygame.font.Font(None, 25)

running = True
shooting = False
console = False

# задержки
frame_count_projectile = 0
frame_count_target = 0
frame_end_console = 0
player.update_characteristics()

input_console = InputBox(100, 0, 140, 32)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            shooting = True
        elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            shooting = False
        elif pygame.key.get_pressed()[pygame.K_F1] and frame_end_console == 0:
            frame_end_console = 20
            if console:
                console = False
            else:
                console = True
                input_console.open_console()

        if console:
            input_console.handle_event(event)
    if not console:
        # стрельба
        if shooting and frame_count_projectile == 0:
            frame_count_projectile = player.period
            projectiles_player = player.shot()
            for projectile in projectiles_player:
                projectiles.add(projectile)
                all_sprites.add(projectile)

        # проверка на столкновение врага и патрона
        for enemy_x in enemies:
            for projectile_x in projectiles:
                if enemy_x.rect.colliderect(projectile_x.rect):
                    enemy_x.hp -= projectile_x.damage
                    if enemy_x.hp <= 0:
                        # добавление частиц
                        mouse_x, mouse_y = enemy_x.rect.centerx, enemy_x.rect.centery
                        direction = [random.uniform(-1, 1), random.uniform(-1, 1)]
                        size = enemy_x.size // 5
                        color = enemy_x.color
                        particles += create_particles(mouse_x, mouse_y, direction, 1.5, size, color, 10)

                        enemy_x.kill()
                    projectile_x.kill()
                    break

        # проверка на столкновение врага и игрока
        for enemy_x in enemies:
            if enemy_x.rect.colliderect(player.rect):

                if frame_count_target == 0:
                    no_target = True
                    frame_count_target = FPS // 2

                    player.hp -= 1
                    if player.hp <= 0:
                        print("You Lose")
                break

        all_sprites.update()

    # отрисовка
    screen.fill((255, 255, 255))
    pygame.draw.rect(screen, GRAY, [R, 0, WIDTH, HEIGHT])
    projectiles.draw(screen)
    screen.blit(player.image, player.rect)
    enemies.draw(screen)

    # отрисовка частиц
    for particle in particles:
        particle['pos'][0] += particle['dir'][0]
        particle['pos'][1] += particle['dir'][1]
        particle['life'] -= 1
        pygame.draw.rect(screen, particle['color'],
                         [particle['pos'][0], particle['pos'][1], particle['size'], particle['size']])
    particles = [p for p in particles if p['life'] > 0]

    text_room = font_room.render(str(room_number), True, (0, 0, 0))
    screen.blit(text_room, (10, 10))

    text_hp = font_ch.render("hp: " + str(player.hp), True, (0, 0, 0))
    screen.blit(text_hp, (10, 50))

    text_speed = font_ch.render("speed: " + str(player.speed), True, (0, 0, 0))
    screen.blit(text_speed, (10, 70))

    text_damage = font_ch.render("damage: " + str(player.damage), True, (0, 0, 0))
    screen.blit(text_damage, (10, 90))

    text_period = font_ch.render("period: " + str(FPS / player.period)[:6], True, (0, 0, 0))
    screen.blit(text_period, (10, 110))

    text_speed_projectile = font_ch.render("speed projectile: " + str(player.speed_projectile), True, (0, 0, 0))
    screen.blit(text_speed_projectile, (10, 130))

    text_range_projectile = font_ch.render("range projectile: " + str(player.range_projectile), True, (0, 0, 0))
    screen.blit(text_range_projectile, (10, 150))

    text_size_projectile = font_ch.render("size projectile: " + str(player.size_projectile[0]), True, (0, 0, 0))
    screen.blit(text_size_projectile, (10, 170))

    text_inventory = font_ch.render("inventory:", True, (0, 0, 0))
    screen.blit(text_inventory, (R + WIDTH + 10, 0))
    test_all_improvements = []

    # тестовыйй вывод инвенторя
    for item in player.all_improvements:
        text_i = font_ch.render(f"- {item.__class__.__name__}"[:-11], True, (0, 0, 0))
        test_all_improvements.append(text_i)
    for i, text_item in enumerate(test_all_improvements):
        screen.blit(text_item, (R + WIDTH + 10, 30 + i * 15))

    if console:
        input_console.update()
        input_console.draw(screen)

    pygame.display.flip()
    clock.tick(FPS)
    # print("FPS:", int(clock.get_fps()))
    if not console:
        if frame_count_projectile > 0:
            frame_count_projectile -= 1

        if frame_count_target > 0:
            frame_count_target -= 1

    if frame_end_console > 0:
        frame_end_console -= 1

    if len(enemies) == 0:
        # новая комната
        room_number += 1
        print(room_number)
        room = Room(room_number, player)
        room.add(all_sprites, enemies)

pygame.quit()
sys.exit()
