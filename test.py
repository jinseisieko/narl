"""pg main loop"""
import sys
from Collisions.Collisions import *
from tqdm import tqdm

import ImageSprites

from Constants import *
from Field import Field
from Functions.Functions import *
from Movable_objects.Enemies import *
from Movable_objects.Obstacles import *
from Movable_objects.Player import *

pg.init()

field: Field = Field()

player: Player = Player("a", field)
matrix = player.matrix

screen: pg.Surface = pg.display.set_mode((WIDTH, HEIGHT), flags=pg.NOFRAME)

enemy_set = set([
    Enemy(np.array([1100 + 10 * i, 1000 + 20 * i * (-1) ** i, 25, 25, 10, 1, 0, 0, 0, 300]), enemies, entity_ids.pop(),
          "black", field,
          entity_ids) for i in range(len(entity_ids))])

bullet_set = set()

obstacle_set = set()
obstacle_set.add(
    Obstacle(np.array([FIELD_WIDTH / 2, 0, FIELD_WIDTH, 100]), obstacles, obstacles_ids.pop(), "red", field,
             obstacles_ids))
obstacle_set.add(
    Obstacle(np.array([FIELD_WIDTH / 2, FIELD_HEIGHT, FIELD_WIDTH, 100]), obstacles, obstacles_ids.pop(), "red", field,
             obstacles_ids))
obstacle_set.add(
    Obstacle(np.array([0, FIELD_HEIGHT / 2, 100, FIELD_HEIGHT]), obstacles, obstacles_ids.pop(), "red", field,
             obstacles_ids))
obstacle_set.add(
    Obstacle(np.array([FIELD_WIDTH, FIELD_HEIGHT / 2, 100, FIELD_HEIGHT]), obstacles, obstacles_ids.pop(), "red", field,
             obstacles_ids))
obstacle_set |= set([
    Obstacle(np.array([0 + 100 * i, 0 + 200 * i, 10, 60]), obstacles, obstacles_ids.pop(), "yellow", field,
             obstacles_ids)
    for i in range(10)])

pg.mouse.set_visible(False)

running: bool = True
time_passed = 0
delay = 0.01
shooting = False
with (tqdm() as pbar):
    while running:

        dt: np.float_ = DT(CLOCK)
        direction = np.array([0, 0])
        for event in pg.event.get():
            if event.type == pg.QUIT or pg.key.get_pressed()[pg.K_DELETE]:
                running = False
                quit()

            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    shooting = True
            if event.type == pg.MOUSEBUTTONUP:
                if event.button == 1:
                    shooting = False

        time_passed = max(time_passed - dt, 0)

        if shooting:
            if time_passed == 0:
                player_pos = matrix[..., :2][0]
                mouse_pos = np.array(pg.mouse.get_pos()) + matrix[..., :2][0] - np.array([WIDTH, HEIGHT]) / 2
                angle = np.arctan2(*(mouse_pos - player_pos)[::-1])
                data = [player_pos[0], player_pos[1], 10, 10, 1, 1, 500 * np.cos(angle) + matrix[..., 6][0],
                        500 * np.sin(angle) + matrix[..., 7][0], 0, 0, 5]
                if len(bullet_ids):
                    index = bullet_ids.pop()
                    bullet_set.add(
                        DefaultBullet(data, bullets, index, "green", field, bullet_ids))
                else:
                    print("bullet error")
                time_passed = delay

        calc_player_movement(matrix, set_direction(pg.key.get_pressed()), dt)

        calc_enemy_direction(enemies, *matrix[..., 0:2][0])
        calc_movements(enemies, dt)
        calc_bullet_movements(bullets, dt)

        calc_collisions(enemies, np.float_(300), dt)
        calc_obstacles(enemies, obstacles)
        calc_obstacles(bullets, obstacles, True)
        calc_obstacles(matrix, obstacles)

        calc_damage(enemies, bullets)

        field.move_screen_relative_player(matrix, dt)

        # draw
        # ||| ! самый медленный код из всех ! |||
        screen.fill((0, 0, 0))
        field.draw()
        player.draw()
        point = pg.Surface((10, 10))
        point.fill("red")
        field.field.blit(point, matrix[..., :2][0])
        for x in set(enemy_set):
            if x.matrix[x.Id, 8] == 1:
                enemy_set.remove(x)
                x.kill()
            else:
                x.draw()

        for x in set(bullet_set):
            if x.matrix[x.Id, 8] == 1:
                bullet_set.remove(x)
                x.kill()
            else:
                x.draw()

        for x in obstacle_set:
            x.draw()

        field_screen_centre_x, field_screen_centre_y = field.screen_centre[0] - WIDTH // 2, field.screen_centre[
            1] - HEIGHT // 2
        screen.blit(field.field, (0, 0), (field_screen_centre_x, field_screen_centre_y, WIDTH, HEIGHT))
        pg.draw.circle(screen, "white", (WIDTH // 2, HEIGHT // 2), 5)
        mouse_x, mouse_y = pygame.mouse.get_pos()
        screen.blit(ImageSprites.sprites['cursor'],
                    (mouse_x - 16, mouse_y - 16))

        pg.display.flip()
        CLOCK.tick(FPS * 1000)
        pbar.update(1)
pg.quit()
sys.exit()
