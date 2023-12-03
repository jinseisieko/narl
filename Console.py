"""console logic"""
import pygame
from Constants import *

pygame.init()


class Console:
    """class Console"""
    font = pygame.font.Font(*FONT_CONSOLE)  # initialization in the class so that there is no pygame in the constants

    def __init__(self, x, y, width, height):
        self.rect: pygame.Rect = pygame.Rect(x, y, width, height)
        self.color: tuple[int, int, int] = BLACK
        self.text = ''
        self.txt_surface: pygame.Surface = self.font.render(self.text, True, self.color)
        self.rect_screen: bool = False
        self.center_screen: bool = False

        self.index_previous_commands: int = 0
        self.previous_commands: list[str] = ['']

    def handle_event(self, event):
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

    def update(self):
        width = max(200, self.txt_surface.get_width() + 10)
        self.rect.w = width

    def draw(self, screen):
        """method for drawing text input"""
        screen.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 5))
        pygame.draw.rect(screen, self.color, self.rect, 1)

    def draw_in_field(self, field):
        """a method for drawing some important things on the field"""
        if self.rect_screen:
            pygame.draw.ellipse(field.field, (255, 0, 0), (field.screen_centre[0] - MOVE_SCREEN_RECT_X,
                                                           field.screen_centre[1] - MOVE_SCREEN_RECT_Y,
                                                           MOVE_SCREEN_RECT_X * 2, MOVE_SCREEN_RECT_Y * 2), 2)
        if self.center_screen:
            pygame.draw.line(field.field, (255, 255, 255),
                             (field.screen_centre[0] - WIDTH, field.screen_centre[1] - HEIGHT),
                             (field.screen_centre[0] + WIDTH, field.screen_centre[1] + HEIGHT), 1)
            pygame.draw.line(field.field, (255, 255, 255),
                             (field.screen_centre[0] - WIDTH, field.screen_centre[1] + HEIGHT),
                             (field.screen_centre[0] + WIDTH, field.screen_centre[1] - HEIGHT), 1)

    def open_console(self):
        self.text = ''

    def input_command(self, command: str):
        try:
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

                if command == "all":
                    if values[0].lower() == "true" or values[0].lower() == "1":
                        self.center_screen = True
                        self.rect_screen = True
                    elif values[0].lower() == "false" or values[0].lower() == "0":
                        self.center_screen = False
                        self.rect_screen = False
        except Exception as e:
            print(e)
