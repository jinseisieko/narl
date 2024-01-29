from source.Calculations.Calculations import *
from source.Calculations.Data import *
from source.Console.ConsoleInter import ConsoleInter
from source.Field.Field import Field
from source.Functions.Functions import set_direction
from source.Image.InitializationForGame import get_images_for_game
from source.Interface.Interface import Interface
from source.Levels.Level import Level2
from source.Movable_objects.Bullets import DefaultBullet
from source.Movable_objects.Enemies import Enemy
from source.Movable_objects.Obstacles import *
from source.Movable_objects.Player import *
from source.Save.Save import load
from source.Sounds.Music import *
from source.States.InterfaceData import Data
from source.States.InterfaceState import InterfaceState
from source.States.NewItem import NewItem
from source.States.Pause import Pause
from source.States.ScreenOfDeath import ScreenOfDeath


class MainGameMode(InterfaceState, Data):
    def start(self):
        self.pause = False
        pg.mouse.set_visible(False)

    def __init__(self, screen, game, level=Level2(), mode=0) -> None:
        super().__init__(screen, game)
        self.type = "MainGameMode"
        self.level = level
        self.field: Field = ...
        self.start_level(level)
        self.screen: pg.Surface = screen

        self.player: Player = Player(get_images_for_game()["test_player"], self.field)

        self.enemy_set: set = set()
        self.bullet_set: set = set()
        self.obstacle_set: set = set()

        self.console = ConsoleInter(self, 100, 10)

        self.background_music = BackgroundMusic(wave)

        self.time_passed: np.float_ = np.float_(0)

        self.shooting: bool = False
        self.spawning: bool = False
        self.console_: bool = False
        self.pause: bool = True

        self.FPS = FPS

        self.interface = Interface(self)

        self.last_screen = self.screen.copy()
        self.begin(mode)

    def start_level(self, level):
        self.field: Field = Field(field, level.background)
        calc_creation_wave(wave, level.difficulty)

    def begin(self, mode):
        pg.mouse.set_visible(False)
        self.pause = False
        self.game.fps = FPS
        self.background_music.update_music_list()
        if mode:
            load()
            self.make_borders()
            for x in set(range(0, MAX_ENEMIES)) - entity_ids:
                self.enemy_set.add(Enemy(enemies, x, "green", self.field, entity_ids))
            for x in set(range(0, MAX_BULLETS)) - bullet_ids:
                self.bullet_set.add(DefaultBullet(bullets, x, "test_bullet", self.field, bullet_ids))
            for x in set(range(4, MAX_OBSTACLES)) - obstacles_ids:
                self.obstacle_set.add(Obstacle(obstacles, x, "red", self.field, obstacles_ids))
        else:
            clear_data()
            self.make_borders()
            self.create_obstacles()

    def make_borders(self):
        obstacles[0] = np.array([FIELD_WIDTH / 2, - 100, FIELD_WIDTH, 100])
        obstacles[1] = np.array([FIELD_WIDTH / 2, FIELD_HEIGHT + 100, FIELD_WIDTH, 100])
        obstacles[2] = np.array([- 100, FIELD_HEIGHT / 2, 100, FIELD_HEIGHT])
        obstacles[3] = np.array([FIELD_WIDTH + 100, FIELD_HEIGHT / 2, 100, FIELD_HEIGHT])
        self.obstacle_set.add(
            Obstacle(obstacles, 0, "red", self.field, obstacles_ids))
        self.obstacle_set.add(
            Obstacle(obstacles, 1, "red", self.field, obstacles_ids))
        self.obstacle_set.add(
            Obstacle(obstacles, 2, "red", self.field, obstacles_ids))
        self.obstacle_set.add(
            Obstacle(obstacles, 3, "red", self.field, obstacles_ids))
        obstacles_ids.discard(0)
        obstacles_ids.discard(1)
        obstacles_ids.discard(2)
        obstacles_ids.discard(3)

    def create_obstacles(self):
        self.obstacle_set |= set(
            [Obstacle(obstacles, obstacles_ids.pop(), "black", self.field, obstacles_ids,
                      data=np.array([0 + 100 * i, 0 + 200 * i, 200, 600]))
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
            self.player.add_item(*self.player.characteristics.getitem.get_rank_random(r1=10, r2=5, r3=1000))
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 1:
                self.shooting = True
            if event.button == 3:
                self.spawning = not (self.spawning and True)
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
            if event.key == pg.K_ESCAPE:
                self.pause = True
                self.game.set_state(Pause(self.screen, self.game, self, self.last_screen))
        if event.type == pg.KEYUP:
            if event.key == pg.K_SPACE:
                self.shooting = False

    def shoot(self):
        player[0, 25] = min(player[0, 13], player[0, 25] + self.game.dt)
        if self.shooting:
            Id = calc_shooting(player, bullets, np.array(pg.mouse.get_pos()), field, np.array(list(bullet_ids)),
                               self.game.dt)
            for x in Id:
                self.bullet_set.add(DefaultBullet(bullets, x, "test_bullet", self.field, bullet_ids))
                bullet_ids.remove(x)

    def spawn(self):
        wave[2] = min(wave[1], wave[2] + self.game.dt)
        if self.spawning:
            Id = calc_waves(wave, enemies, field, np.array(list(entity_ids)), self.game.dt, types)
            for x in Id:
                self.enemy_set.add(Enemy(enemies, x, "green", self.field, entity_ids))
                entity_ids.remove(x)

    def damage_player(self):
        res = calc_player_damage(enemies, player, self.game.dt)
        if res == 1:
            self.player.animate_damage_play()
            sn = pg.mixer.Sound("../resource/music/player_damage.mp3")
            sn.set_volume(0.3)
            sn.play()
        elif res == 2:
            self.game.set_state(ScreenOfDeath(self.screen, self.game, self.last_screen))

    def calc_calculations(self):
        if not self.pause:
            calc_player_movement(player, set_direction(self.game.key_pressed), self.game.dt)
            self.spawn()

            calc_enemy_direction(enemies, *player[0, 0:2])
            calc_movements(enemies, self.game.dt)
            calc_bullet_movements(bullets, self.game.dt, default_bullet)
            calc_killing_enemies(enemies, field, default_enemy)
            self.shoot()

            calc_collisions(enemies, COLLISIONS_REPELLING, self.game.dt)
            calc_obstacles(enemies, obstacles, default_enemy)
            calc_obstacles(bullets, obstacles, default_bullet, kill=True, bounce=bool(player[0, 26]))
            calc_obstacles(player, obstacles, np.array([]))

            calc_damage(enemies, bullets, player, default_enemy, default_bullet)
            self.damage_player()

            calc_cameraman(player, field, self.game.dt)

    def draw_or_kill(self):
        for x in self.bullet_set.copy():
            if x.matrix[x.Id, 8] > 0:
                self.bullet_set.remove(x)
                x.kill()
            else:
                x.draw()

        self.player.draw()

        for x in self.enemy_set.copy():
            if x.matrix[x.Id, 8] > 0:
                wave[3] -= 1
                self.enemy_set.remove(x)
                x.kill()
                if x.matrix[x.Id, 8] != 5:
                    wave[8] += 1
                    player[0, 28] += 1
                    sn = pg.mixer.Sound("../resource/music/enemy_damage2.mp3")
                    sn.set_volume(0.2)
                    sn.play()
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

    def draw_cursor(self):
        self.last_screen = self.screen.copy()
        mouse_x, mouse_y = pygame.mouse.get_pos()
        self.screen.blit(get_images_for_game()['cursor'],
                         (mouse_x - 16, mouse_y - 16))

    def play_music(self):
        self.background_music.play()

    def end_calculations(self):
        if calc_creation_wave(wave, self.level.difficulty):
            sn1 = pg.mixer.Sound("../resource/music/new_wave.mp3")
            sn1.set_volume(1)
            sn1.play()
        if calc_player_level(player):
            self.pause = True
            self.game.set_state(NewItem(self.screen, self.game, self, self.last_screen))
            sn1 = pg.mixer.Sound("../resource/music/castle_levelup.mp3")
            sn1.set_volume(1)
            sn1.play()

    def update(self):
        self.calc_calculations()
        self.draw()
        self.draw_console()
        self.draw_interface()
        self.end_calculations()
        self.draw_cursor()
        # self.play_music()
