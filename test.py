"""pg main loop"""
import sys

from tqdm import tqdm

import ImageSprites
from Collisions.Collisions import calc_player_movement
from Constants import *
from Field import Field
from Movable_objects.Player import *

pg.init()

field: Field = Field()

# player
player: Player = Player("a", field)
matrix = player.matrix

# field
screen: pg.Surface = pg.display.set_mode((WIDTH, HEIGHT), flags=pg.NOFRAME)

# actions
running: bool = True


def dt():
    return 0.001 * CLOCK.get_time()


with (tqdm() as pbar):
    while running:

        direction = np.array([0, 0])
        current_time: int = pg.time.get_ticks()
        for event in pg.event.get():
            if event.type == pg.QUIT or pg.key.get_pressed()[pg.K_DELETE]:
                running = False
                quit()

        press = pg.key.get_pressed()
        if press[pg.K_w]:
            direction[1] -= 1
            print(1, direction)
        if press[pg.K_s]:
            direction[1] += 1
            print(2, direction)
        if press[pg.K_a]:
            direction[0] -= 1
            print(3, direction)
        if press[pg.K_d]:
            direction[0] += 1
            print(4, direction)

        calc_player_movement(matrix, direction, dt())
        field.move_screen_relative_player(matrix, dt())

        # draw
        # ||| ! самый медленный код из всех ! |||
        screen.fill((0, 0, 0))

        field_screen_centre_x, field_screen_centre_y = field.screen_centre[0] - WIDTH // 2, field.screen_centre[
            1] - HEIGHT // 2

        field.draw()
        player.draw()

        screen.blit(field.field, (0, 0), (field_screen_centre_x, field_screen_centre_y, WIDTH, HEIGHT))
        pg.draw.circle(screen, "white", (WIDTH // 2, HEIGHT // 2), 5)

        mouse_x, mouse_y = pygame.mouse.get_pos()
        screen.blit(ImageSprites.sprites['cursor'],
                    (mouse_x - 16, mouse_y - 16))

        pg.display.flip()
        CLOCK.tick(FPS)
        pbar.update(1)
pg.quit()
sys.exit()
