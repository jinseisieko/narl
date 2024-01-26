from source.Calculations.Calculations import *
from source.Calculations.Data import *
from source.Console.ConsoleInter import ConsoleInter
from source.Field import Field
from source.Functions.Functions import set_direction
from source.Image.InitializationForGame import get_images_for_game
from source.Interface.Interface import Interface
from source.Movable_objects.Bullets import DefaultBullet
from source.Movable_objects.Enemies import Enemy
from source.Movable_objects.Obstacles import *
from source.Movable_objects.Player import *
from source.States.InterfaceState import InterfaceState


class MainGameMode(InterfaceState):
    def __init__(self, screen, game) -> None:
        super().__init__(screen, game)
        self.type = "MainGameMode"

        self.screen: pg.Surface = screen

        self.field: Field = Field(field)
        self.player: Player = Player(get_images_for_game()["test_player"], self.field)

        self.enemy_set: set = set()
        self.bullet_set: set = set()
        self.obstacle_set: set = set()

        self.console = ConsoleInter(self, 100, 10)

        self.default_enemy_data = np.array(
            [1100, 1000, ENEMY_SIZE_X, 2 * ENEMY_SIZE_Y, ENEMY_HP, ENEMY_DAMAGE, 0, 0, 0, ENEMY_MAX_VELOCITY,
             ENEMY_ARMOR, 0, 0],
            dtype=np.float_)

        self.time_passed: np.float_ = np.float_(0)

        self.shooting: bool = False
        self.spawning: bool = False
        self.console_: bool = False
        self.pause: bool = False

        self.FPS = FPS

        global GAME
        GAME = self

        self.interface = Interface(self)
        self.start()

    def start(self):
        pg.mouse.set_visible(False)
        self.make_borders()
        self.create_enemies()
        self.create_obstacles()
        self.game.fps = FPS

    def create_enemies(self, number: np.int_ = MAX_ENEMIES) -> None:
        return
        for i in range(number):
            Id = entity_ids.pop()
            enemies[Id] = np.array(
                [self.default_enemy_data[0] + 10 * i, self.default_enemy_data[1] + 20 * i * (-1) ** i,
                 *self.default_enemy_data[2:]])
            self.enemy_set.add(Enemy(enemies, Id, "black", self.field, entity_ids))

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

    def draw_console(self):
        if self.console_:
            self.console.update()
            self.console.draw_in_screen(self.screen)
            self.console.draw_in_field(self.field.field)

            self.console.draw(self.screen)

    def draw_interface(self):
        self.interface.calc()
        self.interface.draw(self.screen)

    def check_events(self, event):
        if self.game.key_pressed[pg.K_y]:
            self.player.add_item(*self.player.characteristics.getitem.get_rank_random(r1=10, r2=5))
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                self.shooting = True
            if event.button == 3:
                self.spawning = True

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

    def shoot(self):
        if not self.pause:
            player[0, 25] = min(player[0, 13], player[0, 25] + self.game.dt)
            if self.shooting:
                Id = calc_shooting(player, bullets, np.array(pg.mouse.get_pos()), field, np.array(list(bullet_ids)),
                                   self.game.dt)
                for x in Id:
                    self.bullet_set.add(DefaultBullet(bullets, x, "test_bullet", self.field, bullet_ids))
                    bullet_ids.remove(x)

    def spawn(self):
        if not self.pause:
            wave[2] = min(wave[1], wave[2] + self.game.dt)
            if self.spawning:
                Id = calc_waves(player, wave, enemies, field, np.array(list(entity_ids)), self.game.dt, types)
                for x in Id:
                    self.enemy_set.add(Enemy(enemies, x, "green", self.field, entity_ids))
                    entity_ids.remove(x)

    def calc_calculations(self):
        if not self.pause:
            calc_player_movement(player, set_direction(self.game.key_pressed), self.game.dt)
            self.spawn()

            calc_enemy_direction(enemies, *player[0, 0:2])
            calc_movements(enemies, self.game.dt)
            calc_bullet_movements(bullets, self.game.dt)
            self.shoot()

            calc_collisions(enemies, COLLISIONS_REPELLING, self.game.dt)
            calc_obstacles(enemies, obstacles)
            calc_obstacles(bullets, obstacles, bounce=bool(player[0, 26]))
            calc_obstacles(player, obstacles)

            calc_damage(enemies, bullets, player)
            calc_player_damage(enemies, player, self.game.dt)

            calc_cameraman(player, field, self.game.dt)

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
        mouse_x, mouse_y = pygame.mouse.get_pos()
        self.screen.blit(get_images_for_game()['cursor'],
                         (mouse_x - 16, mouse_y - 16))

    def update(self):
        self.calc_calculations()
        self.draw()
        self.draw_console()
        self.draw_interface()
