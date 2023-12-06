"""console logic"""
import random

import pygame

from Constants import *
from Items import get_item

pygame.init()


class Console:
    """class Console"""
    font = pygame.font.Font(*FONT_CONSOLE)  # initialization in the class so that there is no pygame in the constants

    def __init__(self, x: int, y: int, width: int, height: int, player, screen, field, clock) -> None:
        self.rect: pygame.Rect = pygame.Rect(x, y, width, height)
        self.color: tuple[int, int, int] = BLACK
        self.text: str = ''
        self.txt_surface: pygame.Surface = self.font.render(self.text, True, self.color)
        self.rect_screen: bool = False
        self.center_screen: bool = False
        self.fps: bool = False
        self.characteristic: bool = False
        self.line_target: bool = False

        self.player = player
        self.screen = screen
        self.field = field
        self.clock = clock

        self.index_previous_commands: int = 0
        self.previous_commands: list[str] = ['']

    def handle_event(self, event) -> None:
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RETURN:
                if self.previous_commands[-1] != self.text:
                    self.previous_commands.append(self.text)

                self.input_command(self.text)

                self.text = ''
                self.index_previous_commands = 0

            elif event.key == pygame.K_BACKSPACE:
                self.text = self.text[:-1]
                self.index_previous_commands = 0

            elif event.key == pygame.K_UP:
                try:
                    self.text = self.previous_commands[-(1 + self.index_previous_commands)]
                    self.index_previous_commands += 1
                except IndexError:
                    self.text = ''

            elif event.key == pygame.K_DOWN:
                try:
                    self.index_previous_commands -= 1
                    self.text = self.previous_commands[-(1 + self.index_previous_commands)]

                except IndexError:
                    self.text = ''

                if self.index_previous_commands < 0:
                    self.index_previous_commands = 0

            elif event.key == pygame.K_ESCAPE:
                pass

            else:

                self.text += event.unicode
                self.index_previous_commands = 0

            self.txt_surface = self.font.render(self.text, True, self.color)

    def update(self) -> None:
        width = max(200, self.txt_surface.get_width() + 10)
        self.rect.w = width

    def draw(self, screen) -> None:
        """method for drawing text input"""
        screen.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 5))
        pygame.draw.rect(screen, self.color, self.rect, 1)

    def draw_in_field(self) -> None:
        """a method for drawing some important things on the field"""
        if self.rect_screen:
            pygame.draw.ellipse(self.field.field, (255, 0, 0), (self.field.screen_centre[0] - MOVE_SCREEN_RECT_X,
                                                                self.field.screen_centre[1] - MOVE_SCREEN_RECT_Y,
                                                                MOVE_SCREEN_RECT_X * 2, MOVE_SCREEN_RECT_Y * 2), 2)
        if self.center_screen:
            pygame.draw.line(self.field.field, (255, 255, 255),
                             (self.field.screen_centre[0] - WIDTH, self.field.screen_centre[1] - HEIGHT),
                             (self.field.screen_centre[0] + WIDTH, self.field.screen_centre[1] + HEIGHT), 1)
            pygame.draw.line(self.field.field, (255, 255, 255),
                             (self.field.screen_centre[0] - WIDTH, self.field.screen_centre[1] + HEIGHT),
                             (self.field.screen_centre[0] + WIDTH, self.field.screen_centre[1] - HEIGHT), 1)

    def draw_in_screen(self):
        if self.fps:
            self.screen.blit(pygame.font.Font(*FONT_FPS).render(str(self.clock.get_fps())[:6], True, BLACK), (10, 40))

        if self.characteristic:
            self.screen.blit(
                pygame.font.Font(*FONT_CHARACTERISTICS).render(f"sp: {self.player.max_speed}", True, BLACK),
                (10, 55))
            self.screen.blit(pygame.font.Font(*FONT_CHARACTERISTICS).render(f"mhp: {self.player.max_hp}", True, BLACK),
                             (10, 70))
            self.screen.blit(pygame.font.Font(*FONT_CHARACTERISTICS).render(f"pe: {self.player.period}", True, BLACK),
                             (10, 85))
            self.screen.blit(
                pygame.font.Font(*FONT_CHARACTERISTICS).render(f"pr: {self.player.projectile_range}", True, BLACK),
                (10, 100))
            self.screen.blit(
                pygame.font.Font(*FONT_CHARACTERISTICS).render(f"psp: {self.player.projectile_speed}", True, BLACK),
                (10, 115))
            self.screen.blit(
                pygame.font.Font(*FONT_CHARACTERISTICS).render(f"psi: {self.player.projectile_size}", True, BLACK),
                (10, 130))
            self.screen.blit(
                pygame.font.Font(*FONT_CHARACTERISTICS).render(f"pd: {self.player.projectile_damage}", True, BLACK),
                (10, 145))

        if self.line_target:
            cursor_pos = pygame.mouse.get_pos()
            pygame.draw.line(self.screen, (255, 255, 0),
                             (self.player.rect.centerx - self.field.screen_centre[0] + WIDTH // 2,
                              self.player.rect.centery - self.field.screen_centre[1] + HEIGHT // 2),
                             (cursor_pos[0], cursor_pos[1]), width=2)

    def open_console(self) -> None:
        self.text = ''

    def player_reset(self):
        self.player.inventory.items.clear()
        self.player.max_speed = DEFAULT_PLAYER_SPEED
        self.player.acceleration = self.player.max_speed / ACCELERATION_SMOOTHNESS
        self.player.resistance_acceleration = self.player.max_speed / SLOWDOWN_SMOOTHNESS
        self.player.max_hp = DEFAULT_PLAYER_HP
        self.player.period = DEFAULT_PROJECTILE_PERIOD
        self.player.projectile_range = DEFAULT_PROJECTILE_RANGE
        self.player.projectile_speed = DEFAULT_PROJECTILE_SPEED
        self.player.projectile_size = DEFAULT_PROJECTILE_SIZE
        self.player.projectile_damage = DEFAULT_PROJECTILE_DAMAGE
        self.player.buckshot_scatter = False

    def input_command(self, command: str) -> None:
        try:
            if command == "y":
                self.player.add_item(get_item(0))
                return

            command = command.split()
            object_, command, values = command[0], command[1], command[2:]
            if object_ == "screen_draw" or object_ == "scrd":
                if command == "rect":
                    if values[0].lower() == "true" or values[0].lower() == "1":
                        self.rect_screen = True
                    elif values[0].lower() == "false" or values[0].lower() == "0":
                        self.rect_screen = False

                if command == "centre_screen" or command == "centres" or command == "cnts":
                    if values[0].lower() == "true" or values[0].lower() == "1":
                        self.center_screen = True
                    elif values[0].lower() == "false" or values[0].lower() == "0":
                        self.center_screen = False
                if command == "fps":
                    if values[0].lower() == "true" or values[0].lower() == "1":
                        self.fps = True
                    elif values[0].lower() == "false" or values[0].lower() == "0":
                        self.fps = False
                if command == "characteristic" or command == "ch":
                    if values[0].lower() == "true" or values[0].lower() == "1":
                        self.characteristic = True
                    elif values[0].lower() == "false" or values[0].lower() == "0":
                        self.characteristic = False
                if command == "line_target" or command == "lt":
                    if values[0].lower() == "true" or values[0].lower() == "1":
                        self.line_target = True
                    elif values[0].lower() == "false" or values[0].lower() == "0":
                        self.line_target = False
                if command == "all":
                    if values[0].lower() == "true" or values[0].lower() == "1":
                        self.center_screen = True
                        self.rect_screen = True
                        self.fps = True
                        self.characteristic = True
                        self.line_target = True
                    elif values[0].lower() == "false" or values[0].lower() == "0":
                        self.center_screen = False
                        self.rect_screen = False
                        self.fps = False
                        self.characteristic = False
                        self.line_target = False

            if object_ == "player" or object_ == "pl":
                if command == "additem" or command == "addi":
                    count = 1
                    if len(values) > 1:
                        count = int(values[1])

                    if values[0] == "r":
                        for _ in range(count):
                            self.player.add_item(get_item(random.randint(0, ITEMS_COUNT - 1)))
                    for _ in range(count):
                        self.player.add_item(get_item(int(values[0])))

                if command == "inventory" or command == "inv":
                    if values[0] == "clear" or values[0] == "cl":
                        self.player_reset()

                if command == "reset" or command == "res":
                    self.player_reset()
                    if values[0] == "r":
                        for _ in range(int(values[1])):
                            self.player.add_item(get_item(random.randint(0, ITEMS_COUNT - 1)))
                    for _ in range(int(values[1])):
                        self.player.add_item(get_item(int(values[0])))
        except Exception:
            pass
