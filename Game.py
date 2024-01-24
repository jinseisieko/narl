"""game class"""
from Buttons import StartButton, ExitButton
from Calculations.Calculations import *
from Calculations.Data import *
from Console.ConsoleInter import ConsoleInter
from Field import Field
from Functions.Functions import *
from ImageSprites import sprites
from Interface.Interface import Interface
from Inventory.ItemImages.InitializationOfObjectImages import init_images
from Movable_objects.Enemies import *
from Movable_objects.Obstacles import *
from Movable_objects.Player import *
from TitleScreen import TitleScreen


class Game:
    def __init__(self):
        self.state = 0
        self.screen: pg.Surface = pg.display.set_mode((WIDTH, HEIGHT), flags=pg.NOFRAME, depth=0)
        init_images()
        self.field: Field = Field(field)
        self.title_screen: TitleScreen = TitleScreen(self.screen)
        self.title_screen.buttons.append(StartButton(self.title_screen.background))
        self.title_screen.buttons.append(ExitButton(self.title_screen.background))
        self.player: Player = Player(r"image\test_player.png", self.field)

        self.enemy_set: set = set()
        self.bullet_set: set = set()
        self.obstacle_set: set = set()

        self.console = ConsoleInter(self, 100, 10)

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

        self.key_pressed: (list, None) = None

        self.FPS = FPS

        global GAME
        GAME = self

        self.interface = Interface(self)

    def play(self):
        self.change_pseudo_constants()
        self.check_events()
        if self.state == 1:
            self.calc_calculations()
            self.draw()
            self.draw_console()
            self.draw_interface()
        elif self.state == 0:
            self.title_screen.draw()
        self.end_cycle()

    def start_game(self):
        self.state = 1
        self.make_borders()
        self.create_enemies()
        self.create_obstacles()

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
        self.key_pressed = pg.key.get_pressed()

    def draw_console(self):
        if self.console_:
            self.console.update()
            self.console.draw_in_screen(self.screen)
            self.console.draw_in_field(self.field.field)

            self.console.draw(self.screen)

    def draw_interface(self):
        self.interface.calc()
        self.interface.draw(self.screen)

    def check_events(self):
        for event in pg.event.get():

            if event.type == pg.QUIT or self.key_pressed[pg.K_DELETE]:
                self.running: bool = False
                quit()
            if self.state:
                if self.key_pressed[pg.K_y]:
                    self.player.add_item(*self.player.characteristics.getitem.get_rank_random(r1=10, r2=5))

                if event.type == pg.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        self.shooting = True
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
                    if event.key == pg.K_SPACE:
                        self.shooting = True

                if event.type == pg.KEYUP:
                    if event.key == pg.K_SPACE:
                        self.shooting = False
            else:
                if event.type == pg.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        mouse_pos = np.array(pg.mouse.get_pos())
                        if self.title_screen.buttons[0].update(mouse_pos):
                            self.state = 1
                            self.start_game()
                            pg.mouse.set_visible(False)
                        if self.title_screen.buttons[1].update(mouse_pos):
                            self.running = 0

    def shoot(self):
        if not self.pause:
            player[0, 25] = min(player[0, 13], player[0, 25] + self.dt)
            if self.shooting:
                Id = calc_shooting(player, bullets, np.array(pg.mouse.get_pos()), field, np.array(list(bullet_ids)),
                                   self.dt)
                for x in Id:
                    self.bullet_set.add(DefaultBullet(bullets, x, "green", self.field, bullet_ids))
                    bullet_ids.remove(x)

    def calc_calculations(self):
        if not self.pause:
            calc_player_movement(player, set_direction(self.key_pressed), self.dt)

            calc_enemy_direction(enemies, *player[0, 0:2])
            calc_movements(enemies, self.dt)
            calc_bullet_movements(bullets, self.dt)
            self.shoot()

            calc_collisions(enemies, COLLISIONS_REPELLING, self.dt)
            calc_obstacles(enemies, obstacles)
            calc_obstacles(bullets, obstacles, bounce=bool(player[0, 26]))
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
        self.screen.blit(sprites['cursor'],
                         (mouse_x - 16, mouse_y - 16))

    def end_cycle(self):
        pg.display.flip()
        CLOCK.tick(self.FPS)


GAME = Game()
