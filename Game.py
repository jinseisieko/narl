"""game class"""

import ImageSprites
from Calculations.Calculations import *
from Calculations.Data import *
from Console.ConsoleInter import ConsoleInter
from Constants import *
from Field import Field
from Functions.Functions import *
from Interface.Interface import Interface
from Movable_objects.Enemies import *
from Movable_objects.Obstacles import *
from Movable_objects.Player import *


class Game:
    def __init__(self):
        pg.mouse.set_visible(False)
        self.screen: pg.Surface = pg.display.set_mode((WIDTH, HEIGHT), flags=pg.NOFRAME, depth=0)

        self.field: Field = Field(field)
        self.player: Player = Player(r"image\test_player.png", self.field)

        self.enemy_set: set = set()
        self.bullet_set: set = set()
        self.obstacle_set: set = set()

        self.console = ConsoleInter(self, 10, 10)

        self.default_enemy_data = np.array(
            [1100, 1000, ENEMY_SIZE_X, 2 * ENEMY_SIZE_Y, ENEMY_HP, ENEMY_DAMAGE, 0, 0, 0, ENEMY_MAX_VELOCITY,
             ENEMY_ARMOR],
            dtype=np.float_)

        self.dt: np.float_ = np.float_(0)
        self.time_passed: np.float_ = np.float_(0)

        self.running: bool = True
        self.shooting: bool = False
        self.console_: bool = False
        self.pause: bool = False

        self.COLLISIONS_REPELLING = COLLISIONS_REPELLING
        self.key_pressed: (list, None) = None

        self.FPS = FPS

        global GAME
        GAME = self

        self.interface = Interface(player)

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
        self.obstacle_set |= set(
            [Obstacle(np.array([0 + 100 * i, 0 + 200 * i, 200, 600]), obstacles, obstacles_ids.pop(),
                      "yellow", self.field, obstacles_ids)
             for i in range(10)])

    def change_pseudo_constants(self):
        self.dt = DT(CLOCK)
        self.time_passed = max(self.time_passed - self.dt, 0)
        self.key_pressed = pg.key.get_pressed()

    def draw_console(self):
        if self.console_:
            self.console.update()
            self.console.draw_in_screen(self.screen)
            self.console.draw_in_field(self.field.fwield)

            self.console.draw(self.screen)

    def draw_interface(self):
        self.interface.calc()
        self.interface.draw(self.screen)

    def check_events(self):
        for event in pg.event.get():

            if event.type == pg.QUIT or self.key_pressed[pg.K_DELETE]:
                self.running: bool = False
                quit()

            if self.key_pressed[pg.K_y]:
                self.player.characteristics.apply("ffffff")

            if event.type == pg.MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.shooting: bool = True
            if event.type == pg.MOUSEBUTTONUP:
                if event.button == 1:
                    self.shooting = False

            if event.type == pg.KEYDOWN:
                self.console.handle_event(event)
                if event.key == pg.K_F1:
                    self.console_ = not self.console_
                    self.pause = self.console_
                    if self.console_:
                        self.console.open_console()

    def shoot(self):
        if not self.pause:
            if self.shooting:
                if self.time_passed == 0:
                    player_pos = player[0, :2]
                    mouse_pos = np.array(pg.mouse.get_pos()) + self.field.data[0:2] - self.field.data[8:10] / 2
                    angle = np.arctan2(*(mouse_pos - player_pos)[::-1]) + player[0, 20] * (np.random.random() - 0.5) * 2
                    data = [player_pos[0], player_pos[1], player[0, 15], player[0, 16], 1,
                            player[0, 17],
                            player[0, 22] * np.cos(angle) + player[0, 6],
                            player[0, 22] * np.sin(angle) + player[0, 7], 0, 0, player[0, 21], player[0, 14]]
                    if len(bullet_ids):
                        index = bullet_ids.pop()
                        self.bullet_set.add(
                            DefaultBullet(data, bullets, index, "green", self.field, bullet_ids))
                    else:
                        print("bullet error")
                    self.time_passed = player[0, 13]

    def calc_calculations(self):
        if not self.pause:
            calc_player_movement(player, set_direction(self.key_pressed), self.dt)

            calc_enemy_direction(enemies, *player[0, 0:2])
            calc_movements(enemies, self.dt)
            calc_bullet_movements(bullets, self.dt)

            calc_collisions(enemies, self.COLLISIONS_REPELLING, self.dt)
            calc_obstacles(enemies, obstacles)
            calc_obstacles(bullets, obstacles, bounce=True)
            calc_obstacles(player, obstacles)

            calc_damage(enemies, bullets, player)
            calc_player_damage(enemies, player, self.dt)

            calc_cameraman(player, field, self.dt)

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
        field_screen_centre_x, field_screen_centre_y = self.field.data[0:2] - self.field.data[8:10] / 2
        self.screen.blit(self.field.field, (0, 0), (field_screen_centre_x, field_screen_centre_y, WIDTH, HEIGHT))
        pg.draw.circle(self.screen, "white", (WIDTH // 2, HEIGHT // 2), 5)
        mouse_x, mouse_y = pygame.mouse.get_pos()
        self.screen.blit(ImageSprites.sprites['cursor'],
                         (mouse_x - 16, mouse_y - 16))

    def end_cycle(self):
        pg.display.flip()
        CLOCK.tick(self.FPS * 1000)


GAME = Game()
GAME.make_borders()
GAME.create_enemies()
GAME.create_obstacles()
