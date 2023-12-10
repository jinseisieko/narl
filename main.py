"""pygame main loop"""
import random
import sys

import pygame
from tqdm import tqdm

import ImageSprites
from Collisions import *
from Console import *
from Constants import *
from Enemies import Enemy
from Field import Field
from Player import Player

pygame.init()

field: Field = Field()
chunks: Chunks = Chunks()

# groups
projectiles: pygame.sprite.Group = pygame.sprite.Group()
enemies: pygame.sprite.Group = pygame.sprite.Group()
player_group: pygame.sprite.Group = pygame.sprite.Group()

# player
player: Player = Player(field, chunks)
player_group.add(player)

# fieldw
screen: pygame.Surface = pygame.display.set_mode((WIDTH, HEIGHT), flags=pygame.NOFRAME)

for _ in range(0):
    enemy2: Enemy = Enemy(player, player.x + random.randint(-1000, 1000), player.y + random.randint(-1000, 1000),
                          chunks)
    enemies.add(enemy2)
# all_sprites.add(enemy)

# actions
running: bool = True
shooting: bool = False
console_opening: bool = False
pause: bool = False

# frames
delay_shot: float = 0

last_click_time: dict[str, int] = {W: 0, A: 0, S: 0, D: 0}
text_pause: pygame.Surface = pygame.font.Font(*FONT_PAUSE).render("pause", True, BLACK)

pygame.mouse.set_visible(False)

console = Console(10, 10, 200, 20, player, screen, field, CLOCK, projectiles, enemies, player_group, chunks)

with (tqdm() as pbar):
    while running:

        current_time: int = pygame.time.get_ticks()
        for event in pygame.event.get():
            if event.type == pygame.QUIT or pygame.key.get_pressed()[pygame.K_DELETE]:
                running = False
                quit()

            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1 or event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
                shooting = True
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1 or event.type == pygame.KEYUP and event.key == pygame.K_SPACE:
                shooting = False
            elif event.type == pygame.KEYDOWN and pygame.key.get_pressed()[pygame.K_F1]:
                if console_opening:
                    console_opening = False
                else:
                    console_opening = True
                    console.open_console()

            elif event.type == pygame.KEYDOWN and pygame.key.get_pressed()[pygame.K_ESCAPE]:
                if pause:
                    pause = False
                else:
                    pause = True

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_w:
                    if current_time - last_click_time[W] < DOUBLE_CLICK_INTERVAL:
                        player.dash(0, -1)
                    last_click_time[W] = current_time

                if event.key == pygame.K_a:
                    if current_time - last_click_time[A] < DOUBLE_CLICK_INTERVAL:
                        player.dash(-1, 0)
                    last_click_time[A] = current_time

                if event.key == pygame.K_s:
                    if current_time - last_click_time[S] < DOUBLE_CLICK_INTERVAL:
                        player.dash(0, 1)
                    last_click_time[S] = current_time

                if event.key == pygame.K_d:
                    if current_time - last_click_time[D] < DOUBLE_CLICK_INTERVAL:
                        player.dash(1, 0)
                    last_click_time[D] = current_time

            if console:
                console.handle_event(event)

        # add new obj
        if not pause:
            if shooting and delay_shot == 0:
                delay_shot = player.period / 1000
                projectile = player.default_shot()

                projectiles.add(projectile)
        # update
        if not pause:
            player_group.update()
            projectiles.update()
            enemies.update()
            chunks.calculate_collisions()

        if console_opening:
            console.update()
        # screen movement calculation
        field.move_screen_relative_player(player)

        # draw
        # ||| ! самый медленный код из всех ! |||

        field_screen_centre_x, field_screen_centre_y = field.screen_centre[0] - WIDTH // 2, field.screen_centre[
            1] - HEIGHT // 2

        screen.fill((0, 0, 0))
        field.draw(projectiles, player_group, enemies, player=player)
        console.draw_in_field()

        screen.blit(field.field, (0, 0), (field_screen_centre_x, field_screen_centre_y, WIDTH, HEIGHT))

        mouse_x, mouse_y = pygame.mouse.get_pos()
        screen.blit(ImageSprites.sprites['cursor'],
                    (mouse_x - 16, mouse_y - 16))

        console.draw_in_screen()
        if console_opening:
            console.draw(screen)
        if pause:
            screen.blit(text_pause, (WIDTH - text_pause.get_size()[0] - 10, 10))

        for i, row in enumerate(player.inventory.get_to_draw()[:WIDTH // 37 * H]):
            for j, item in enumerate(row):
                screen.blit(ImageSprites.sprites[item.image], (WIDTH - 37 * H - 10 + j * 37, 10 + i * 37))

        # update frames
        if not pause:
            if delay_shot > 0:
                delay_shot -= 1 / (CLOCK.get_fps() + 1e-10)

            if delay_shot < 0:
                delay_shot = 0
        print(delay_shot)

        pygame.display.flip()
        CLOCK.tick(FPS)
        pbar.update(1)
pygame.quit()
sys.exit()
