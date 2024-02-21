from source.Calculations.Calculations import *
from source.Calculations.Data import *
from source.Console.ConsoleInter import ConsoleInter
from source.Field.Field import Field
from source.Functions.Functions import set_direction
from source.Interface.Interface import Interface
from source.Levels.Level import Level1
from source.Movable_objects.Boss import Boss
from source.Movable_objects.Bullets import DefaultBullet
from source.Movable_objects.Enemies import Enemy
from source.Movable_objects.Obstacles import *
from source.Movable_objects.Player import *
from source.Save.Save import load, delete_all_save
from source.Sounds.Sound import *
from source.States.InterfaceData import Data
from source.States.InterfaceState import InterfaceState
from source.States.NewItem import NewItem
from source.States.Pause import Pause
from source.States.ScreenOfDeath import ScreenOfDeath
from source.Calculations.Data import *

n = 0


class MainGameMode(InterfaceState, Data):
    def start(self):
        self.pause = False
        self.interface.update_items_surface()
        pg.mouse.set_visible(False)
        self.main_window.fps = MAX_FPS[0]

    def __init__(self, screen, main_window, level=Level1(), mode=0) -> None:
        super().__init__(screen, main_window)
        self.mode = mode
        self.type = "MainGameMode"
        self.level = level
        self.field: Field = ...
        self.start_level(level)
        self.screen: pg.Surface = screen

        self.player: Player = Player(self.main_window, get_images_for_game()["test_player"])

        self.enemy_set: set = set()
        self.player_bullet_set: set = set()
        self.enemy_bullet_set: set = set()
        self.obstacle_set: set = set()

        self.console = ConsoleInter(self, 100, 10)

        self.background_music = BackgroundMusic()
        self.sound_effect = SoundEffect()

        self.time_passed: np.float_ = np.float_(0)

        self.shooting: bool = False
        self.spawning: bool = False
        self.console_: bool = False
        self.pause: bool = True
        self.boss_fight: bool = False

        self.interface = Interface(self)

        self.last_screen = self.screen.copy()

        self.begin()
        print(self.main_window.meta_player.name)

    def start_level(self, level):
        if level.end:
            player[0][hp] = -1
            return
        self.field: Field = Field(field, level.background)
        name = "red"
        if level.name is None:
            ...
        else:
            name = level.name
        if level.obstacles is None:
            ...
        else:
            obstacles[:] = level.obstacles[:]
            clear_obstacles_ids()
            clear_bullets()
            self.obstacle_set.clear()
            for x in set(range(4, MAX_OBSTACLES)):
                self.obstacle_set.add(Obstacle(obstacles, x, name, obstacles_ids))
                obstacles_ids.remove(x)
        calc_creation_wave(wave, level.difficulty / 2, level.enemies_types)

    def begin(self):
        pg.mouse.set_visible(False)
        self.pause = False
        self.main_window.fps = MAX_FPS[0]
        self.background_music.update(self.level.number)
        self.background_music.update_music_list()
        if self.mode:
            if load(self):
                self.player.characteristics.update_array_draw()
                self.interface.update_items_surface()
                self.make_borders()
                for x in set(range(0, MAX_ENEMIES)) - entity_ids:
                    self.enemy_set.add(Enemy(enemies, x, "green", entity_ids))
                for x in set(range(0, MAX_PLAYER_BULLETS)) - player_bullets_ids:
                    self.player_bullet_set.add(DefaultBullet(player_bullets, x, "test_bullet", player_bullets_ids))
                for x in set(range(4, MAX_OBSTACLES)) - obstacles_ids:
                    self.obstacle_set.add(Obstacle(obstacles, x, "red", obstacles_ids))
            else:
                clear_data()
                self.make_borders()

        else:
            clear_data()
            self.make_borders()
        self.player.update_characteristics()

    def make_borders(self):
        obstacles[0] = np.array([FIELD_WIDTH / 2, - 1000, FIELD_WIDTH, 1000])
        obstacles[1] = np.array([FIELD_WIDTH / 2, FIELD_HEIGHT + 1000, FIELD_WIDTH, 1000])
        obstacles[2] = np.array([- 1000, FIELD_HEIGHT / 2, 1000, FIELD_HEIGHT])
        obstacles[3] = np.array([FIELD_WIDTH + 1000, FIELD_HEIGHT / 2, 1000, FIELD_HEIGHT])
        self.obstacle_set.add(
            Obstacle(obstacles, 0, "red", obstacles_ids))
        self.obstacle_set.add(
            Obstacle(obstacles, 1, "red", obstacles_ids))
        self.obstacle_set.add(
            Obstacle(obstacles, 2, "red", obstacles_ids))
        self.obstacle_set.add(
            Obstacle(obstacles, 3, "red", obstacles_ids))
        obstacles_ids.discard(0)
        obstacles_ids.discard(1)
        obstacles_ids.discard(2)
        obstacles_ids.discard(3)

    def create_obstacles(self):
        self.obstacle_set |= set(
            [Obstacle(obstacles, obstacles_ids.pop(), "black", obstacles_ids,
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
        if self.main_window.key_pressed[pg.K_y]:
            self.player.add_item(*self.player.characteristics.getitem.get_rank_random())
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
            if event.key == CONTROLS["OPEN_CONSOLE"]:
                self.console_ = not self.console_
                self.pause = self.console_
                if self.console_:
                    self.console.open_console()
            if event.key == CONTROLS["SHOOT"]:
                self.shooting = True
            if event.key == CONTROLS["MENU"]:
                self.pause = True
                self.main_window.set_state(Pause(self.screen, self.main_window, self, self.last_screen))
        if event.type == pg.KEYUP:
            if event.key == CONTROLS["SHOOT"]:
                self.shooting = False

    def shoot(self):
        player[0, 25] = min(player[0, 13], player[0, 25] + self.main_window.dt)
        if self.shooting:
            Id = calc_player_shooting(player, player_bullets, np.array(pg.mouse.get_pos()), field,
                                      np.array(list(player_bullets_ids)),
                                      self.main_window.dt)
            for x in Id:
                self.player_bullet_set.add(DefaultBullet(player_bullets, x, "test_bullet", player_bullets_ids))
                player_bullets_ids.remove(x)

    def spawn(self):
        wave[2] = min(wave[1], wave[2] + self.main_window.dt)
        if self.spawning:
            Id = calc_waves(wave, enemies, field, np.array(list(entity_ids)), self.main_window.dt, enemy_types)
            for x in Id:
                self.enemy_set.add(Enemy(enemies, x, "green", entity_ids))
                entity_ids.remove(x)

    def damage_player(self, who):
        res = calc_player_damage(who, player, self.main_window.dt)
        if res == 1:
            self.player.animate_damage_play()
            self.sound_effect.player_damage()
        elif res == 2:
            delete_all_save(self.main_window.meta_player.name)
            self.sound_effect.player_death()
            self.main_window.set_state(ScreenOfDeath(self.screen, self.main_window, self.last_screen))

    def calc_calculations(self):
        if not self.pause:
            calc_player_movement(player, set_direction(self.main_window.key_pressed), self.main_window.dt)

            if self.boss_fight:
                calc_boss_direction(boss, player)
                calc_movements(enemies, self.main_window.dt)
                boss[0, 13] = min(boss[0, 12], boss[0, 13] + self.main_window.dt)

                Id = calc_boss_shooting(boss, enemy_bullets, player, np.array(list(enemy_bullets_ids)),
                                        self.main_window.dt)
                for x in Id:
                    self.enemy_bullet_set.add(DefaultBullet(enemy_bullets, x, "test_bullet", enemy_bullets_ids))
                    enemy_bullets_ids.remove(x)
                    print(x)

                enemy_bullets[0] = np.array([boss[0, 0], boss[0, 1], boss[0, 2] + 100, boss[0, 3] + 100, 1, 20, 0, 0, 0, 1, 1, 10])
                calc_bullet_movements(enemy_bullets, self.main_window.dt, default_bullet)

                calc_obstacles(boss, obstacles, np.array([]))
                calc_obstacles(enemy_bullets, obstacles, default_bullet, kill=True, bounce=True)

                self.shoot()
                calc_bullet_movements(player_bullets, self.main_window.dt, default_bullet)
                calc_obstacles(player_bullets, obstacles, default_bullet, kill=True, bounce=bool(player[0, 26]))
                calc_obstacles(player, obstacles, np.array([]))
                calc_damage(boss, player_bullets, player, default_boss, default_bullet)
                self.damage_player(boss)
                self.damage_player(enemy_bullets)
            else:
                self.spawn()

                calc_enemy_direction(enemies, *player[0, 0:2])
                calc_movements(enemies, self.main_window.dt)
                calc_bullet_movements(enemy_bullets, self.main_window.dt, default_bullet)

                calc_collisions(enemies, COLLISIONS_REPELLING, self.main_window.dt)
                calc_obstacles(enemies, obstacles, default_enemy)
                calc_obstacles(enemy_bullets, obstacles, default_bullet, kill=True, bounce=True)

                calc_killing_enemies(enemies, field, default_enemy)

                self.shoot()
                calc_bullet_movements(player_bullets, self.main_window.dt, default_bullet)
                calc_obstacles(player_bullets, obstacles, default_bullet, kill=True, bounce=bool(player[0, 26]))
                calc_obstacles(player, obstacles, np.array([]))

                calc_damage(enemies, player_bullets, player, default_enemy, default_bullet)
                self.damage_player(enemies)

            calc_cameraman(player, field, self.main_window.dt)

    def draw_or_kill(self):
        for x in self.player_bullet_set.copy():
            if x.matrix[x.Id, 8] > 0:
                self.player_bullet_set.remove(x)
                x.kill()
            else:
                x.draw(self.field.field)

        for x in self.enemy_bullet_set.copy():
            if x.matrix[x.Id, 8] > 0:
                self.enemy_bullet_set.remove(x)
                x.kill()
            else:
                x.draw(self.field.field)

        self.player.draw(self.field.field)

        for x in self.enemy_set.copy():
            if x.matrix[x.Id, 8] > 0:
                wave[3] -= 1
                self.enemy_set.remove(x)
                x.kill()
                if x.matrix[x.Id, 8] != 5:
                    self.main_window.tasksAndAchievements.kill_100_enemies(1)
                    self.main_window.tasksAndAchievements.kill_1000_enemies(1)
                    wave[8] += 1
                    player[0, 28] += 1
                    self.sound_effect.kill_enemy()
            else:
                x.draw(self.field.field)

        if self.boss_fight:
            self.boss.draw(self.field.field)

        for x in self.obstacle_set:
            x.draw(self.field.field)

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
        if not self.boss_fight:
            if calc_creation_wave(wave, self.level.difficulty, self.level.enemies_types):
                self.sound_effect.new_wave()

        if calc_player_level(player):
            self.pause = True
            self.main_window.set_state(NewItem(self.screen, self.main_window, self, self.last_screen))
            self.sound_effect.new_level()

    def check_level(self):
        if not self.boss_fight:
            if wave[0] > self.level.count_waves:
                if not self.level.boss is None:
                    for x in self.enemy_set.copy():
                        self.enemy_set.remove(x)
                        x.kill()
                        x.matrix[x.Id] = default_enemy

                    self.boss_fight = True

                    self.boss = Boss(boss, self.level.boss)
                    calc_boss_fight_start(player, boss, self.level.number - 2, boss_types, field)
                    enemy_bullets_ids.remove(0)
                else:
                    self.level = self.level.next()
                    self.start_level(self.level)
        else:
            if boss[0, 4] <= 0:
                enemy_bullets_ids.add(0)
                self.level = self.level.next()
                self.start_level(self.level)
                self.boss_fight = False

    def update(self):
        global n

        self.calc_calculations()
        self.draw()
        self.draw_console()
        self.draw_interface()
        self.end_calculations()
        self.draw_cursor()
        self.check_level()

        n += 1
        # self.main_window.fps = 15 + 60 * math.sin(n / 1000 * 2 * math.pi) ** 2
        self.play_music()
