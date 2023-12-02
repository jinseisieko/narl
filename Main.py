"""pygame main loop"""

import sys
from collections import deque

import numba
import pygame
from tqdm import tqdm

import ImageSprites
from Constants import *
from Enemies import Enemy
from Field import Field
from Player import Player
from time import time, sleep


@numba.jit(nopython=True, fastmath=True)
def calculate_canter(screen_centre: float, param: int) -> float:
    return screen_centre - param // 2


@numba.jit(nopython=True, fastmath=True)
def calculate_cursor_coordinates(mouse_x: int, mouse_y: int, projectile_size):
    return mouse_x - projectile_size // 2, mouse_y - projectile_size // 2


field: Field = Field()

mode_fps: int = DEFAULT_FPS
clock = pygame.time.Clock()

# groups
all_sprites: pygame.sprite.Group = pygame.sprite.Group()
players_projectile: pygame.sprite.Group = pygame.sprite.Group()
enemies: pygame.sprite.Group = pygame.sprite.Group()
enemies_projectile: pygame.sprite.Group = pygame.sprite.Group()
player_group: pygame.sprite.Group = pygame.sprite.Group()

# player
player: Player = Player(field)
player_group.add(player)
all_sprites.add(player_group)

# field

screen: pygame.Surface = pygame.display.set_mode((WIDTH, HEIGHT), flags=pygame.NOFRAME)

enemy: Enemy = Enemy(player, player.x, player.y)
# enemies.add(enemy)
all_sprites.add(enemy)

# actions
running: bool = True
shooting: bool = False

# frames
frame_draw: int = 0
frame_shot: int = 0

last_click_time: dict[str, int] = {W: 0, A: 0, S: 0, D: 0, }

pygame.mouse.set_visible(False)

t0 = time()
with tqdm() as pbar:
    while running:
        flag_for_event: bool = True
        current_time: int = pygame.time.get_ticks()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
                break
            elif pygame.key.get_pressed()[pygame.K_DELETE]:
                pygame.quit()
                running = False
                break
            elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
                shooting = True
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                shooting = False

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
        else:
            flag_for_event = False

        if flag_for_event:
            break

        # add new obj
        if shooting and frame_shot == 0:
            frame_shot = player.period
            projectiles = player.shot()

            for projectile in projectiles:
                players_projectile.add(projectile)
                all_sprites.add(projectile)

        # update
        all_sprites.update()

        # screen movement calculation
        field.move_screen_relative_player(player)
        # draw

        # ||| ! самый медленный код из всех ! |||
        if frame_draw == 0:
            frame_draw: int = TICKS // FPS[mode_fps]

            field_screen_centre_x: float = calculate_canter(field.screen_centre[0], WIDTH)
            field_screen_centre_y: float = calculate_canter(field.screen_centre[1], HEIGHT)

            field.draw(enemies_projectile, players_projectile, player_group, enemies, player=player)

            screen.fill((0, 0, 0))

            screen.blit(field.field, (0, 0), (field_screen_centre_x, field_screen_centre_y, WIDTH, HEIGHT))

            screen.blit(ImageSprites.sprites['cursor'],
                        (calculate_cursor_coordinates(*pygame.mouse.get_pos(), player.projectile_size)))

        # update frames
        if frame_draw > 0:
            frame_draw -= 1

        if frame_shot > 0:
            frame_shot -= 1

        pygame.display.flip()
        clock.tick(TICKS)
        # clock.tick(TICKS * 10 // 2)
        # print("FPS:", int(clock.get_fps()) / 120 * FPS[mode_fps], "Objects: ", len(all_sprites))
        pbar.update(1)
pygame.quit()
sys.exit()
