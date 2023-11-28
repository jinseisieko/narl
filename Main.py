"""pygame main loop"""

import sys
import pygame

import ImageSprites
from Constants import *
from Player import Player
from Field import Field

mode_fps: int = 1
clock = pygame.time.Clock()

# groups
all_sprites: pygame.sprite.Group = pygame.sprite.Group()
players_projectile: pygame.sprite.Group = pygame.sprite.Group()
enemies: pygame.sprite.Group = pygame.sprite.Group()
enemies_projectile: pygame.sprite.Group = pygame.sprite.Group()
player_group: pygame.sprite.Group = pygame.sprite.Group()

# player
player: Player = Player()
player_group.add(player)
all_sprites.add(player_group)

# field
field: Field = Field()
screen: pygame.Surface = pygame.display.set_mode((WIDTH, HEIGHT), flags=pygame.NOFRAME)

# actions
running: bool = True
shooting: bool = False

# frames
frame_draw: int = 0
frame_shot: int = 0

pygame.mouse.set_visible(False)
while running:
    flag_for_event = True
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

    # draw
    if frame_draw == 0:
        frame_draw = TICKS // FPS[mode_fps]
        field.draw(enemies_projectile, players_projectile, player_group, enemies)
        screen.fill((0, 0, 0))
        screen.blit(field.field, (0, 0),
                    (player.rect.centerx - WIDTH // 2, player.rect.centery - HEIGHT // 2, WIDTH, HEIGHT))

        pos_mouse = pygame.mouse.get_pos()
        screen.blit(ImageSprites.sprites['cursor'], (pos_mouse[0], pos_mouse[1]))

    # update frames
    if frame_draw > 0:
        frame_draw -= 1

    if frame_shot > 0:
        frame_shot -= 1

    pygame.display.flip()
    clock.tick(TICKS)
    # print("FPS:", int(clock.get_fps()) / 120 * FPS[mode_fps], "Objects: ", len(all_sprites))

pygame.quit()
sys.exit()
