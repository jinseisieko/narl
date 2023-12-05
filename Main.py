"""pygame main loop"""

import sys

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

clock = pygame.time.Clock()

# groups
all_sprites: pygame.sprite.Group = pygame.sprite.Group()
players_projectile: pygame.sprite.Group = pygame.sprite.Group()
enemies: pygame.sprite.Group = pygame.sprite.Group()
enemies_projectile: pygame.sprite.Group = pygame.sprite.Group()
player_group: pygame.sprite.Group = pygame.sprite.Group()

object_ID: dict[int] = dict()
IDs: set[int] = set()
lastID = 0

# player
player: Player = Player(field, lastID, IDs)
object_ID[lastID] = player
lastID += 1
player_group.add(player)

# field
screen: pygame.Surface = pygame.display.set_mode((WIDTH, HEIGHT), flags=pygame.NOFRAME)

console = Console(10, 10, 200, 20, player)

enemy: Enemy = Enemy(player, player.x, player.y, lastID, IDs)
enemies.add(enemy)
object_ID[lastID] = enemy
lastID += 1
enemy1: Enemy = Enemy(player, player.x, player.y, lastID, IDs)
enemies.add(enemy1)
object_ID[lastID] = enemy1
# all_sprites.add(enemy)

# actions
running: bool = True
shooting: bool = False
console_opening: bool = False
pause: bool = False

# frames
frame_draw: int = 0
frame_shot: int = 0

last_click_time: dict[str, int] = {W: 0, A: 0, S: 0, D: 0}
text_pause: pygame.Surface = pygame.font.Font(*FONT_PAUSE).render("pause", True, BLACK)

pygame.mouse.set_visible(False)

time_draw: int = TICKS // FPS[DEFAULT_FPS]

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

        if len(IDs) == 0:
            lastID += 1
            IDs.add(lastID)

        # add new obj
        if not pause:
            if shooting and frame_shot == 0:
                frame_shot = player.period
                projectile = player.shot(IDs.pop(), IDs)

                object_ID[lastID] = projectile
                players_projectile.add(projectile)
                # all_sprites.add(projectile)

        enemies_positions = np.zeros((CHUNK_N_X, CHUNK_N_Y, 20, 9))
        projectiles_positions = np.zeros((CHUNK_N_X, CHUNK_N_Y, 40, 9))
        positions: set[tuple[int, int]] = set()

        # update
        if not pause:
            player_group.update()
            enemies.update(enemies_positions, positions)

            players_projectile.update(projectiles_positions)
            positions_np = np.array(list(positions))
            player_data, enemy_data, projectiles_data = calculate_soft_collision(0, enemies_positions,
                                                                                 projectiles_positions, positions_np,
                                                                                 CHUNK_N_X, CHUNK_N_Y, 20)

            for pos in positions:
                for i in range(len(enemy_data[pos[0]][pos[1]])):
                    if enemy_data[pos[0]][pos[1]][i][8] == 0:
                        continue
                    object_ID[enemy_data[pos[0]][pos[1]][i][8]].dx = enemy_data[pos[0]][pos[1]][i][2]
                    object_ID[enemy_data[pos[0]][pos[1]][i][8]].dy = enemy_data[pos[0]][pos[1]][i][3]

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
            console.draw_in_screen(screen, clock)
            if console_opening:
                console.draw(screen)
            if pause:
                screen.blit(text_pause, (WIDTH - text_pause.get_size()[0] - 10, 10))

            for i, row in enumerate(player.inventory.get_to_draw()):
                for j, item in enumerate(row):
                    screen.blit(ImageSprites.sprites[item.image], (WIDTH - 37 * 5 - 10 + j * 37, 10 + i * 37))
        # draw frames
        if frame_draw > 0:
            frame_draw -= 1

        # update frames
        if not pause:
            if frame_shot > 0:
                frame_shot -= 1

        pygame.display.flip()
        clock.tick(TICKS * 100)
        # print(player.x, player.y)
        # print(player.rect.centerx, player.rect.centery, 2)
        pbar.update(1)

pygame.quit()
sys.exit()
