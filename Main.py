"""pygame main loop"""

import sys

import pygame
from tqdm import tqdm
from Console import *
import ImageSprites

from Enemies import Enemy
from Field import Field
from Player import Player
from Constants import *

pygame.init()

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

console = Console(10, 10, 200, 20)

enemy: Enemy = Enemy(player, player.x, player.y)
# enemies.add(enemy)
all_sprites.add(enemy)

# actions
running: bool = True
shooting: bool = False
console_opening: bool = False
pause: bool = False

# frames
frame_draw: int = 0
frame_shot: int = 0

last_click_time: dict[str, int] = {W: 0, A: 0, S: 0, D: 0, }
text_pause: pygame.Surface = pygame.font.Font(*FONT_PAUSE).render("pause", True, BLACK)

pygame.mouse.set_visible(False)

time_draw: int = TICKS // FPS[mode_fps]

with (tqdm() as pbar):
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
        else:
            flag_for_event = False

        if flag_for_event:
            break

        # add new obj
        if not pause:
            if shooting and frame_shot == 0:
                frame_shot = player.period
                projectiles = player.shot()

                for projectile in projectiles:
                    players_projectile.add(projectile)
                    all_sprites.add(projectile)

        # update
        if not pause:
            all_sprites.update()
        if console_opening:
            console.update()

        # screen movement calculation
        field.move_screen_relative_player(player)

        # draw
        # ||| ! самый медленный код из всех ! |||
        if frame_draw == 0:
            frame_draw: int = time_draw

            field_screen_centre_x, field_screen_centre_y = field.screen_centre[0] - WIDTH // 2, field.screen_centre[
                1] - HEIGHT // 2

            screen.fill((0, 0, 0))
            field.draw(enemies_projectile, players_projectile, player_group, enemies, player=player)
            console.draw_in_field(field)

            screen.blit(field.field, (0, 0), (field_screen_centre_x, field_screen_centre_y, WIDTH, HEIGHT))

            mouse_x, mouse_y = pygame.mouse.get_pos()
            screen.blit(ImageSprites.sprites['cursor'],
                        (mouse_x - player.projectile_size // 2, mouse_y - player.projectile_size // 2))

            if console_opening:
                console.draw(screen)

            if pause:
                screen.blit(text_pause, (WIDTH - text_pause.get_size()[0] - 10, 10))

        # update frames
        if not pause:
            if frame_draw > 0:
                frame_draw -= 1

            if frame_shot > 0:
                frame_shot -= 1

        pygame.display.flip()
        clock.tick(TICKS)
        # print(player.x, player.y)
        # print(player.rect.centerx, player.rect.centery, 2)
        # time.sleep(1000)
        # clock.tick(TICKS * 10 // 2)
        # print("FPS:", int(clock.get_fps()) / 120 * FPS[mode_fps], "Objects: ", len(all_sprites))
        pbar.update(1)

pygame.quit()
sys.exit()
