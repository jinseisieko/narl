"""Game class"""
import ImageSprites
from Collisions.Collisions import *
from Constants import *
from Field import Field
from Functions.Functions import *
from Movable_objects.Enemies import *
from Movable_objects.Obstacles import *
from Movable_objects.Player import *


class Game:
    def __init__(self):
        self.field: Field = Field()
        self.player: Player = Player("a", self.field)
        self.screen: pg.Surface = pg.display.set_mode((WIDTH, HEIGHT), flags=pg.NOFRAME)
        pg.mouse.set_visible(False)
        self.enemy_set: set = set()
        self.bullet_set: set = set()
        self.obstacle_set: set = set()
        self.default_enemy_data = np.array(
            [1100, 1000, ENEMY_SIZE_X, ENEMY_SIZE_Y, ENEMY_HP, ENEMY_DAMAGE, 0, 0, 0, ENEMY_MAX_VELOCITY],
            dtype=np.float_)
        self.dt: np.float_ = np.float_(0)
        self.running: bool = True
        self.time_passed: np.float_ = np.float_(0)
        self.delay: np.float_ = PLAYER_DELAY
        self.shooting: bool = False
        self.COLLISIONS_REPELLING = COLLISIONS_REPELLING

    def create_enemies(self, number: np.int_ = MAX_ENEMIES) -> None:
        self.enemy_set = set([Enemy(np.array(
            [self.default_enemy_data[0] + 10 * i, self.default_enemy_data[1] + 20 * i * (-1) ** i,
             *self.default_enemy_data[2:]]),
            enemies, entity_ids.pop(), "black", self.field, entity_ids)
            for i in range(number)])

    def make_borders(self):
        self.obstacle_set.add(
            Obstacle(np.array([FIELD_WIDTH / 2, - 100, FIELD_WIDTH, 100]), obstacles, obstacles_ids.pop(), "red",
                     self.field,
                     obstacles_ids))
        self.obstacle_set.add(
            Obstacle(np.array([FIELD_WIDTH / 2, FIELD_HEIGHT + 100, FIELD_WIDTH, 100]), obstacles, obstacles_ids.pop(),
                     "red",
                     self.field, obstacles_ids))
        self.obstacle_set.add(
            Obstacle(np.array([- 100, FIELD_HEIGHT / 2, 100, FIELD_HEIGHT]), obstacles, obstacles_ids.pop(), "red",
                     self.field,
                     obstacles_ids))
        self.obstacle_set.add(
            Obstacle(np.array([FIELD_WIDTH + 100, FIELD_HEIGHT / 2, 100, FIELD_HEIGHT]), obstacles, obstacles_ids.pop(),
                     "red", self.field, obstacles_ids))

    def create_obstacles(self):
        self.obstacle_set |= set([Obstacle(np.array([0 + 100 * i, 0 + 200 * i, 10, 60]), obstacles, obstacles_ids.pop(),
                                           "yellow", self.field, obstacles_ids)
                                  for i in range(10)])

    def change_pseudo_constants(self):
        self.dt = DT(CLOCK)
        self.time_passed = max(self.time_passed - self.dt, 0)

    def check_events(self):
        for event in pg.event.get():
            if event.type == pg.QUIT or pg.key.get_pressed()[pg.K_DELETE]:
                self.running: bool = False
                quit()

            if pg.key.get_pressed()[pg.K_y]:
                self.player.characteristics.apply("tast1")

            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.shooting: bool = True
            if event.type == pg.MOUSEBUTTONUP:
                if event.button == 1:
                    self.shooting = False

    def shoot(self):
        if self.shooting:
            if self.time_passed == 0:
                player_pos = player[..., :2][0]
                mouse_pos = np.array(pg.mouse.get_pos()) + self.field.screen_centre - np.array([WIDTH, HEIGHT]) / 2
                angle = np.arctan2(*(mouse_pos - player_pos)[::-1])
                data = [player_pos[0], player_pos[1], PLAYER_BULLET_SIZE_X, PLAYER_BULLET_SIZE_Y, 1,
                        PLAYER_BULLET_DAMAGE,
                        PLAYER_BULLET_VELOCITY * np.cos(angle) + player[..., 6][0],
                        PLAYER_BULLET_VELOCITY * np.sin(angle) + player[..., 7][0], 0, 0, 5]
                if len(bullet_ids):
                    index = bullet_ids.pop()
                    self.bullet_set.add(
                        DefaultBullet(data, bullets, index, "green", self.field, bullet_ids))
                else:
                    print("bullet error")
                self.time_passed = self.delay

    def calc_calculations(self):
        calc_player_movement(player, set_direction(pg.key.get_pressed()), self.dt)

        calc_enemy_direction(enemies, *player[..., 0:2][0])
        calc_movements(enemies, self.dt)
        calc_bullet_movements(bullets, self.dt)

        calc_collisions(enemies, self.COLLISIONS_REPELLING, self.dt)
        calc_obstacles(enemies, obstacles)
        calc_obstacles(bullets, obstacles, True)
        calc_obstacles(player, obstacles)

        calc_damage(enemies, bullets)

        self.field.move_screen_relative_player(player, self.dt)

    def draw_or_kill(self):
        self.player.draw()
        for x in set(self.enemy_set):
            if x.matrix[x.Id, 8] == 1:
                self.enemy_set.remove(x)
                x.kill()
            else:
                x.draw()

        for x in set(self.bullet_set):
            if x.matrix[x.Id, 8] == 1:
                self.bullet_set.remove(x)
                x.kill()
            else:
                x.draw()

        for x in self.obstacle_set:
            x.draw()

    def draw(self):
        self.screen.fill(0)
        self.field.draw()
        self.draw_or_kill()
        field_screen_centre_x, field_screen_centre_y = self.field.screen_centre[0] - WIDTH // 2, \
                                                       self.field.screen_centre[
                                                           1] - HEIGHT // 2
        self.screen.blit(self.field.field, (0, 0), (field_screen_centre_x, field_screen_centre_y, WIDTH, HEIGHT))
        pg.draw.circle(self.screen, "white", (WIDTH // 2, HEIGHT // 2), 5)
        mouse_x, mouse_y = pygame.mouse.get_pos()
        self.screen.blit(ImageSprites.sprites['cursor'],
                         (mouse_x - 16, mouse_y - 16))

    def end_cycle(self):
        pg.display.flip()
        CLOCK.tick(FPS * 1000)
