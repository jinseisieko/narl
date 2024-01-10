"""console logic"""
import pygame as pg
import pyperclip

from Console.ConsoleValues import ConsoleValues


class PlayerInd:
    x = 0
    y = 1
    size_x = 2
    size_y = 3
    hp = 4
    ___ = 5
    vx = 6
    vy = 7
    max_velocity = 8
    slowdown = 9
    acceleration = 10
    max_hp = 11
    armor = 12
    delay = 13
    armor_piercing = 14
    bullet_size_x = 15
    bullet_size_y = 16
    bullet_damage = 17
    critical_coefficient = 18
    critical_chance = 19
    scatter = 20
    bullet_life_time = 21
    bullet_velocity = 22
    damage_delay = 23


class Console:
    font = pg.font.Font(None, 27)  # initialization in the class so that there is no pygame in the constants

    def __init__(self, game, x, y) -> None:
        self.game = game
        self.color: tuple[int, int, int] = (0, 0, 0)

        self.text: str = ''
        self.txt_surface: pg.Surface = self.font.render(self.text, True, self.color)
        self.consoleValues: ConsoleValues = ConsoleValues()

        self.index_previous_commands: int = 0
        self.previous_commands: list[str] = ['']

        self.x: int = x
        self.y: int = y

        self.width: int = max(200, self.txt_surface.get_width() + 10)
        self.height: int = self.txt_surface.get_height()

    def handle_event(self, event) -> None:
        if event.type == pg.KEYDOWN:
            if event.key == pg.K_RETURN:
                if self.previous_commands[-1] != self.text:
                    self.previous_commands.append(self.text)

                self.input_command(self.text)

                self.text = ''
                self.index_previous_commands = 0
            elif event.key == pg.K_LCTRL:
                pass
            elif event.key == pg.K_v and self.game.key_pressed[pg.K_LCTRL]:
                self.text += pyperclip.paste()
            elif event.key == pg.K_BACKSPACE:
                self.text = self.text[:-1]
                self.index_previous_commands = 0

            elif event.key == pg.K_UP:
                try:
                    self.text = self.previous_commands[-(1 + self.index_previous_commands)]
                    self.index_previous_commands += 1
                except IndexError:
                    self.text = ''

            elif event.key == pg.K_DOWN:
                try:
                    self.index_previous_commands -= 1
                    self.text = self.previous_commands[-(1 + self.index_previous_commands)]

                except IndexError:
                    self.text = ''

                if self.index_previous_commands < 0:
                    self.index_previous_commands = 0

            elif event.key == pg.K_ESCAPE:
                self.input_command(self.text)
                self.text = ''

            else:
                print(event)
                self.text += event.unicode
                self.index_previous_commands = 0

        self.txt_surface = self.font.render(self.text, True, self.color)

    def update(self) -> None:
        self.width = max(200, self.txt_surface.get_width() + 10)
        self.height = self.txt_surface.get_height() + 4

    def draw(self, screen) -> None:
        """method for drawing text input"""
        screen.blit(self.txt_surface, (self.x + 5, self.y + 5))
        pg.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height), 1)

    def open_console(self) -> None:
        self.text = ''

    def draw_in_field(self, field: pg.Surface) -> None:
        ...

    def draw_in_screen(self, screen: pg.Surface) -> None:
        ...

    def input_command(self, command: str) -> None:
        player_object_name = ["player", "pl"]
        player_command_set_x_name = ["x", "set_x"]
        player_command_set_y_name = ["y", "set_y"]
        player_command_set_size_x_name = ["size_x"]
        player_command_set_size_y_name = ["size_y"]
        player_command_set_hp_name = ["hp", "set_hp"]
        player_command_set___name = ["_", "set__"]
        player_command_set_vx_name = ["vx", "set_vx"]
        player_command_set_vy_name = ["vy", "set_vy"]
        player_command_set_max_velocity_name = ["max_velocity", "set_max_velocity"]
        player_command_set_slowdown_name = ["slowdown", "set_slowdown"]
        player_command_set_acceleration_name = ["acceleration", "set_acceleration"]
        player_command_set_max_hp_name = ["max_hp", "set_max_hp"]
        player_command_set_armor_name = ["armor", "set_armor"]
        player_command_set_delay_name = ["delay", "set_delay"]
        player_command_set_armor_piercing_name = ["armor_piercing", "set_armor_piercing"]
        player_command_set_bullet_size_x_name = ["bullet_size_x", "set_bullet_size_x"]
        player_command_set_bullet_size_y_name = ["bullet_size_y", "set_bullet_size_y"]
        player_command_set_bullet_damage_name = ["bullet_damage", "set_bullet_damage"]
        player_command_set_critical_coefficient_name = ["critical_coefficient", "set_critical_coefficient"]
        player_command_set_critical_chance_name = ["critical_chance", "set_critical_chance"]
        player_command_set_scatter_name = ["scatter", "set_scatter"]
        player_command_set_bullet_life_time_name = ["bullet_life_time", "set_bullet_life_time"]
        player_command_set_bullet_velocity_name = ["bullet_velocity", "set_bullet_velocity"]
        player_command_set_damage_delay_name = ["damage_delay", "set_damage_delay"]

        structure_command = command.split()

        match structure_command:
            case (object_, name):
                ...
            case (object_, name, value):
                if object_ in player_object_name:
                    if name in player_command_set_x_name:
                        try:
                            x_ = float(value)
                            self.game.player.characteristics.characteristics[0][
                                PlayerInd.x] = x_
                        except ValueError:
                            ...

                    elif name in player_command_set_y_name:
                        try:
                            y_ = float(value)
                            self.game.player.characteristics.characteristics[0][
                                PlayerInd.y] = y_
                        except ValueError:
                            ...

                    elif name in player_command_set_size_x_name:
                        try:
                            size_x_ = float(value)
                            self.game.player.characteristics.characteristics[0][
                                PlayerInd.size_x] = size_x_

                        except ValueError:
                            ...

                    elif name in player_command_set_size_y_name:
                        try:
                            size_y_ = float(value)
                            self.game.player.characteristics.characteristics[0][
                                PlayerInd.size_y] = size_y_

                        except ValueError:
                            ...

                    elif name in player_command_set_hp_name:
                        try:
                            hp_ = float(value)
                            self.game.player.characteristics.characteristics[0][
                                PlayerInd.hp] = hp_

                        except ValueError:
                            ...

                    elif name in player_command_set___name:
                        try:
                            __ = float(value)
                            self.game.player.characteristics.characteristics[0][
                                PlayerInd.___] = __

                        except ValueError:
                            ...

                    elif name in player_command_set_vx_name:
                        try:
                            vx_ = float(value)
                            self.game.player.characteristics.characteristics[0][
                                PlayerInd.vx] = vx_

                        except ValueError:
                            ...

                    elif name in player_command_set_vy_name:
                        try:
                            vy_ = float(value)
                            self.game.player.characteristics.characteristics[0][
                                PlayerInd.vy] = vy_

                        except ValueError:
                            ...

                    elif name in player_command_set_max_velocity_name:
                        try:
                            max_velocity_ = float(value)
                            self.game.player.characteristics.characteristics[0][
                                PlayerInd.max_velocity] = max_velocity_

                        except ValueError:
                            ...

                    elif name in player_command_set_slowdown_name:
                        try:
                            slowdown_ = float(value)
                            self.game.player.characteristics.characteristics[0][
                                PlayerInd.slowdown] = slowdown_

                        except ValueError:
                            ...

                    elif name in player_command_set_acceleration_name:
                        try:
                            acceleration_ = float(value)
                            self.game.player.characteristics.characteristics[0][
                                PlayerInd.acceleration] = acceleration_

                        except ValueError:
                            ...

                    elif name in player_command_set_max_hp_name:
                        try:
                            max_hp_ = float(value)
                            self.game.player.characteristics.characteristics[0][
                                PlayerInd.max_hp] = max_hp_

                        except ValueError:
                            ...

                    elif name in player_command_set_armor_name:
                        try:
                            armor_ = float(value)
                            self.game.player.characteristics.characteristics[0][
                                PlayerInd.armor] = armor_

                        except ValueError:
                            ...

                    elif name in player_command_set_delay_name:
                        try:
                            delay_ = float(value)
                            self.game.player.characteristics.characteristics[0][
                                PlayerInd.delay] = delay_

                        except ValueError:
                            ...

                    elif name in player_command_set_armor_piercing_name:
                        try:
                            armor_piercing_ = float(value)
                            self.game.player.characteristics.characteristics[0][
                                PlayerInd.armor_piercing] = armor_piercing_

                        except ValueError:
                            ...

                    elif name in player_command_set_bullet_size_x_name:
                        try:
                            bullet_size_x_ = float(value)
                            self.game.player.characteristics.characteristics[0][
                                PlayerInd.bullet_size_x] = bullet_size_x_

                        except ValueError:
                            ...

                    elif name in player_command_set_bullet_size_y_name:
                        try:
                            bullet_size_y_ = float(value)
                            self.game.player.characteristics.characteristics[0][
                                PlayerInd.bullet_size_y] = bullet_size_y_

                        except ValueError:
                            ...

                    elif name in player_command_set_bullet_damage_name:
                        try:
                            bullet_damage_ = float(value)
                            self.game.player.characteristics.characteristics[0][
                                PlayerInd.bullet_damage] = bullet_damage_

                        except ValueError:
                            ...

                    elif name in player_command_set_critical_coefficient_name:
                        try:
                            critical_coefficient_ = float(value)
                            self.game.player.characteristics.characteristics[0][
                                PlayerInd.bullet_damage] = critical_coefficient_

                        except ValueError:
                            ...

                    elif name in player_command_set_critical_chance_name:
                        try:
                            critical_chance_ = float(value)
                            self.game.player.characteristics.characteristics[0][
                                PlayerInd.critical_chance] = critical_chance_

                        except ValueError:
                            ...
                    elif name in player_command_set_scatter_name:
                        try:
                            scatter_ = float(value)
                            self.game.player.characteristics.characteristics[0][
                                PlayerInd.scatter] = scatter_

                        except ValueError:
                            ...

                    elif name in player_command_set_bullet_life_time_name:
                        try:
                            bullet_life_time_ = float(value)
                            self.game.player.characteristics.characteristics[0][
                                PlayerInd.bullet_life_time] = bullet_life_time_

                        except ValueError:
                            ...

                    elif name in player_command_set_bullet_velocity_name:
                        try:
                            bullet_velocity_ = float(value)
                            self.game.player.characteristics.characteristics[0][
                                PlayerInd.bullet_velocity] = bullet_velocity_

                        except ValueError:
                            ...

                    elif name in player_command_set_damage_delay_name:
                        try:
                            damage_delay_ = float(value)
                            self.game.player.characteristics.characteristics[0][
                                PlayerInd.damage_delay] = damage_delay_

                        except ValueError:
                            ...

            case (object_, name, value1, value2):
                ...

            case (object_, name, value1, value2, value3):
                ...

            case _:
                ...

    #
    # import random
    # import pyperclip
    #
    # import pygame
    #
    # from Constants import *
    # from Enemies import Enemy
    # from Items import get_item
    #
    # pygame.init()
    #
    #
    # class Console:
    #     """class Console"""
    #     font = pygame.font.Font(*FONT_CONSOLE)  # initialization in the class so that there is no pygame in the constants
    #
    #     def __init__(self, x: int, y: int, width: int, height: int, player, screen, field, clock, projectiles, enemies,
    #                  player_group, chunks) -> None:
    #         self.rect: pygame.Rect = pygame.Rect(x, y, width, height)
    #         self.color: tuple[int, int, int] = BLACK
    #         self.text: str = ''
    #         self.txt_surface: pygame.Surface = self.font.render(self.text, True, self.color)
    #         self.rect_screen: bool = False
    #         self.center_screen: bool = False
    #         self.fps: bool = False
    #         self.characteristic: bool = False
    #         self.line_target: bool = False
    #         self.chunks_: bool = False
    #         self.objects: bool = False
    #
    #         self.player = player
    #         self.screen = screen
    #         self.field = field
    #         self.clock = clock
    #         self.chunks = chunks
    #
    #         self.projectiles: pygame.sprite.Group = projectiles
    #         self.enemies: pygame.sprite.Group = enemies
    #         self.player_group: pygame.sprite.Group = player_group
    #
    #         self.index_previous_commands: int = 0
    #         self.previous_commands: list[str] = ['']
    #
    #     def handle_event(self, event) -> None:
    #         if pygame.key.get_pressed()[pygame.K_LCTRL] and pygame.key.get_pressed()[pygame.K_v]:
    #             self.text += pyperclip.paste()
    #             return
    #         if event.type == pygame.KEYDOWN:
    #             if event.key == pygame.K_RETURN:
    #                 if self.previous_commands[-1] != self.text:
    #                     self.previous_commands.append(self.text)
    #
    #                 self.input_command(self.text)
    #
    #                 self.text = ''
    #                 self.index_previous_commands = 0
    #
    #             elif event.key == pygame.K_BACKSPACE:
    #                 self.text = self.text[:-1]
    #                 self.index_previous_commands = 0
    #
    #             elif event.key == pygame.K_UP:
    #                 try:
    #                     self.text = self.previous_commands[-(1 + self.index_previous_commands)]
    #                     self.index_previous_commands += 1
    #                 except IndexError:
    #                     self.text = ''
    #
    #             elif event.key == pygame.K_DOWN:
    #                 try:
    #                     self.index_previous_commands -= 1
    #                     self.text = self.previous_commands[-(1 + self.index_previous_commands)]
    #
    #                 except IndexError:
    #                     self.text = ''
    #
    #                 if self.index_previous_commands < 0:
    #                     self.index_previous_commands = 0
    #
    #             elif event.key == pygame.K_ESCAPE:
    #                 pass
    #
    #             else:
    #
    #                 self.text += event.unicode
    #                 self.index_previous_commands = 0
    #
    #         self.txt_surface = self.font.render(self.text, True, self.color)
    #
    #     def update(self) -> None:
    #         width = max(200, self.txt_surface.get_width() + 10)
    #         self.rect.w = width
    #
    #     def draw(self, screen) -> None:
    #         """method for drawing text input"""
    #         screen.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 5))
    #         pygame.draw.rect(screen, self.color, self.rect, 1)
    #
    #     def draw_in_field(self) -> None:
    #         """a method for drawing some important things on the field"""
    #         if self.rect_screen:
    #             pygame.draw.ellipse(self.field.field, (255, 0, 0), (self.field.screen_centre[0] - MOVE_SCREEN_RECT_X,
    #                                                                 self.field.screen_centre[1] - MOVE_SCREEN_RECT_Y,
    #                                                                 MOVE_SCREEN_RECT_X * 2, MOVE_SCREEN_RECT_Y * 2), 2)
    #         if self.center_screen:
    #             pygame.draw.line(self.field.field, (255, 255, 255),
    #                              (self.field.screen_centre[0] - WIDTH, self.field.screen_centre[1] - HEIGHT),
    #                              (self.field.screen_centre[0] + WIDTH, self.field.screen_centre[1] + HEIGHT), 1)
    #             pygame.draw.line(self.field.field, (255, 255, 255),
    #                              (self.field.screen_centre[0] - WIDTH, self.field.screen_centre[1] + HEIGHT),
    #                              (self.field.screen_centre[0] + WIDTH, self.field.screen_centre[1] - HEIGHT), 1)
    #
    #         if self.chunks_:
    #             for i in range(0, CHUNK_N_X):
    #                 pygame.draw.line(self.field.field, (255, 0, 255), (i * CHUNK_SIZE, 0), (i * CHUNK_SIZE, FIELD_HEIGHT),
    #                                  width=2)
    #
    #             for i in range(0, CHUNK_N_Y):
    #                 pygame.draw.line(self.field.field, (255, 0, 255), (0, i * CHUNK_SIZE), (FIELD_WIDTH, i * CHUNK_SIZE),
    #                                  width=2)
    #
    #     def draw_in_screen(self):
    #         if self.fps:
    #             self.screen.blit(pygame.font.Font(*FONT_FPS).render(str(self.clock.get_fps())[:6], True, BLACK), (10, 40))
    #
    #         if self.characteristic:
    #             self.screen.blit(
    #                 pygame.font.Font(*FONT_CHARACTERISTICS).render(f"sp: {self.player.max_speed}", True, BLACK),
    #                 (10, 55))
    #             self.screen.blit(pygame.font.Font(*FONT_CHARACTERISTICS).render(f"mhp: {self.player.max_hp}", True, BLACK),
    #                              (10, 70))
    #             self.screen.blit(pygame.font.Font(*FONT_CHARACTERISTICS).render(f"pe: {self.player.period}", True, BLACK),
    #                              (10, 85))
    #             self.screen.blit(
    #                 pygame.font.Font(*FONT_CHARACTERISTICS).render(f"pr: {self.player.projectile_range}", True, BLACK),
    #                 (10, 100))
    #             self.screen.blit(
    #                 pygame.font.Font(*FONT_CHARACTERISTICS).render(f"psp: {self.player.projectile_speed}", True, BLACK),
    #                 (10, 115))
    #             self.screen.blit(
    #                 pygame.font.Font(*FONT_CHARACTERISTICS).render(f"psi: {self.player.projectile_size}", True, BLACK),
    #                 (10, 130))
    #             self.screen.blit(
    #                 pygame.font.Font(*FONT_CHARACTERISTICS).render(f"pd: {self.player.projectile_damage}", True, BLACK),
    #                 (10, 145))
    #
    #         if self.line_target:
    #             cursor_pos = pygame.mouse.get_pos()
    #             pygame.draw.line(self.screen, (255, 255, 0),
    #                              (self.player.rect.centerx - self.field.screen_centre[0] + WIDTH // 2,
    #                               self.player.rect.centery - self.field.screen_centre[1] + HEIGHT // 2),
    #                              (cursor_pos[0], cursor_pos[1]), width=2)
    #
    #         if self.objects:
    #             self.screen.blit(pygame.font.Font(*FONT_COUNT_OBJECTS).render(f"enemies: {len(self.enemies)}", True, BLACK),
    #                              (10, HEIGHT - 80))
    #             self.screen.blit(
    #                 pygame.font.Font(*FONT_COUNT_OBJECTS).render(f"projectiles: {len(self.projectiles)}", True, BLACK),
    #                 (10, HEIGHT - 60))
    #             self.screen.blit(
    #                 pygame.font.Font(*FONT_COUNT_OBJECTS).render(f"player_group: {len(self.player_group)}", True, BLACK),
    #                 (10, HEIGHT - 40))
    #
    #     def open_console(self) -> None:
    #         self.text = ''
    #
    #     def player_reset(self):
    #         self.player.inventory.items.clear()
    #         self.player.max_speed = DEFAULT_PLAYER_SPEED
    #         self.player.acceleration = self.player.max_speed / ACCELERATION_SMOOTHNESS
    #         self.player.resistance_acceleration = self.player.max_speed / SLOWDOWN_SMOOTHNESS
    #         self.player.max_hp = DEFAULT_PLAYER_HP
    #         self.player.period = DEFAULT_PROJECTILE_PERIOD
    #         self.player.projectile_range = DEFAULT_PROJECTILE_RANGE
    #         self.player.projectile_speed = DEFAULT_PROJECTILE_SPEED
    #         self.player.projectile_size = DEFAULT_PROJECTILE_SIZE
    #         self.player.projectile_damage = DEFAULT_PROJECTILE_DAMAGE
    #         self.player.buckshot_scatter_count = 0
    #         self.player.green_gecko_count = 0
    #         self.player.red_gecko_count = 0
    #         self.player.scope_count = 0
    #         self.player.cactus_count = 0
    #         self.player.pokeball_count = 0
    #
    #     def input_command(self, command: str) -> None:
    #         try:
    #             if command == "y":
    #                 self.player.add_item(get_item(0))
    #                 return
    #
    #             command = command.split()
    #             object_, command, values = command[0], command[1], command[2:]
    #             if object_ == "screen_draw" or object_ == "scrd":
    #                 if command == "rect":
    #                     if values[0].lower() == "true" or values[0].lower() == "1":
    #                         self.rect_screen = True
    #                     elif values[0].lower() == "false" or values[0].lower() == "0":
    #                         self.rect_screen = False
    #
    #                 if command == "centre_screen" or command == "centres" or command == "cnts":
    #                     if values[0].lower() == "true" or values[0].lower() == "1":
    #                         self.center_screen = True
    #                     elif values[0].lower() == "false" or values[0].lower() == "0":
    #                         self.center_screen = False
    #                 if command == "fps":
    #                     if values[0].lower() == "true" or values[0].lower() == "1":
    #                         self.fps = True
    #                     elif values[0].lower() == "false" or values[0].lower() == "0":
    #                         self.fps = False
    #                 if command == "characteristic" or command == "cha":
    #                     if values[0].lower() == "true" or values[0].lower() == "1":
    #                         self.characteristic = True
    #                     elif values[0].lower() == "false" or values[0].lower() == "0":
    #                         self.characteristic = False
    #                 if command == "line_target" or command == "lt":
    #                     if values[0].lower() == "true" or values[0].lower() == "1":
    #                         self.line_target = True
    #                     elif values[0].lower() == "false" or values[0].lower() == "0":
    #                         self.line_target = False
    #                 if command == "chunks" or command == "chu":
    #                     if values[0].lower() == "true" or values[0].lower() == "1":
    #                         self.chunks_ = True
    #                     elif values[0].lower() == "false" or values[0].lower() == "0":
    #                         self.chunks_ = False
    #                 if command == "objects" or command == "obj":
    #                     if values[0].lower() == "true" or values[0].lower() == "1":
    #                         self.objects = True
    #                     elif values[0].lower() == "false" or values[0].lower() == "0":
    #                         self.objects = False
    #                 if command == "all":
    #                     if values[0].lower() == "true" or values[0].lower() == "1":
    #                         self.center_screen = True
    #                         self.rect_screen = True
    #                         self.fps = True
    #                         self.characteristic = True
    #                         self.line_target = True
    #                         self.chunks_ = True
    #                         self.objects = True
    #                     elif values[0].lower() == "false" or values[0].lower() == "0":
    #                         self.center_screen = False
    #                         self.rect_screen = False
    #                         self.fps = False
    #                         self.characteristic = False
    #                         self.line_target = False
    #                         self.chunks_ = False
    #                         self.objects = False
    #
    #             if object_ == "player" or object_ == "pl":
    #                 if command == "additem" or command == "addi":
    #                     count = 1
    #                     if len(values) > 1:
    #                         count = int(values[1])
    #
    #                     if values[0] == "r":
    #                         for _ in range(count):
    #                             self.player.add_item(get_item(random.randint(0, ITEMS_COUNT - 1)))
    #                     for _ in range(count):
    #                         self.player.add_item(get_item(int(values[0])))
    #
    #                 if command == "inventory" or command == "inv":
    #                     if values[0] == "clear" or values[0] == "cl":
    #                         self.player_reset()
    #
    #                 if command == "reset" or command == "res":
    #                     self.player_reset()
    #                     if values[0] == "r":
    #                         for _ in range(int(values[1])):
    #                             self.player.add_item(get_item(random.randint(0, ITEMS_COUNT - 1)))
    #                     for _ in range(int(values[1])):
    #                         self.player.add_item(get_item(int(values[0])))
    #
    #             if object_ == "field" or object_ == "fd":
    #                 if command == "spawbot" or command == "sb":
    #                     for _ in range(int(values[0])):
    #                         enemy = Enemy(self.player, self.player.x + random.randint(-WIDTH // 2, WIDTH // 2),
    #                                       self.player.y + random.randint(-WIDTH // 2, WIDTH // 2), self.chunks)
    #                         self.enemies.add(enemy)
    #
    #         except Exception as e:
    #             print(e)
