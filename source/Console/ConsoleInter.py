"""console logic"""
import pygame as pg
import pyperclip

from source.Console.ConsoleValues import ConsoleValues
from source.Inventory.Exception.ExceptionNotFoundName import ExceptionNotFoundName
from source.PlayerIndexes import *


class ConsoleInter:
    font = pg.font.Font(None, 27)  # initialization in the class so that there is no pygame in the constants

    def __init__(self, game, x_, y_) -> None:
        self.game = game
        self.color: tuple[int, int, int] = (0, 0, 0)

        self.text: str = ''
        self.txt_surface: pg.Surface = self.font.render(self.text, True, self.color)
        self.consoleValues: ConsoleValues = ConsoleValues()

        self.index_previous_commands: int = 0
        self.previous_commands: list[str] = ['']

        self.x: int = x_
        self.y: int = y_

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
        self.txt_surface = self.font.render(self.text, True, self.color)

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
        player_command_add_item = ["add", "add_item"]

        structure_command = command.split()

        if len(structure_command) == 2:
            object_ = structure_command[0]
            name = structure_command[1]

        elif len(structure_command) == 3:
            object_ = structure_command[0]
            name = structure_command[1]
            value = structure_command[2]
            if object_ in player_object_name:
                if name in player_command_set_x_name:
                    try:
                        x_ = float(value)
                        self.game.player.characteristics.characteristics[0][
                            x] = x_
                    except ValueError:
                        ...

                elif name in player_command_set_y_name:
                    try:
                        y_ = float(value)
                        self.game.player.characteristics.characteristics[0][
                            y] = y_
                    except ValueError:
                        ...

                elif name in player_command_set_size_x_name:
                    try:
                        size_x_ = float(value)
                        self.game.player.characteristics.characteristics[0][
                            size_x] = size_x_

                    except ValueError:
                        ...

                elif name in player_command_set_size_y_name:
                    try:
                        size_y_ = float(value)
                        self.game.player.characteristics.characteristics[0][
                            size_y] = size_y_

                    except ValueError:
                        ...

                elif name in player_command_set_hp_name:
                    try:
                        hp_ = float(value)
                        self.game.player.characteristics.characteristics[0][
                            hp] = hp_

                    except ValueError:
                        ...

                elif name in player_command_set_vx_name:
                    try:
                        vx_ = float(value)
                        self.game.player.characteristics.characteristics[0][
                            vx] = vx_

                    except ValueError:
                        ...

                elif name in player_command_set_vy_name:
                    try:
                        vy_ = float(value)
                        self.game.player.characteristics.characteristics[0][
                            vy] = vy_

                    except ValueError:
                        ...

                elif name in player_command_set_max_velocity_name:
                    try:
                        max_velocity_ = float(value)
                        self.game.player.characteristics.characteristics[0][
                            max_velocity] = max_velocity_

                    except ValueError:
                        ...

                elif name in player_command_set_slowdown_name:
                    try:
                        slowdown_ = float(value)
                        self.game.player.characteristics.characteristics[0][
                            slowdown] = slowdown_

                    except ValueError:
                        ...

                elif name in player_command_set_acceleration_name:
                    try:
                        acceleration_ = float(value)
                        self.game.player.characteristics.characteristics[0][
                            acceleration] = acceleration_

                    except ValueError:
                        ...

                elif name in player_command_set_max_hp_name:
                    try:
                        max_hp_ = float(value)
                        self.game.player.characteristics.characteristics[0][
                            max_hp] = max_hp_

                    except ValueError:
                        ...

                elif name in player_command_set_armor_name:
                    try:
                        armor_ = float(value)
                        self.game.player.characteristics.characteristics[0][
                            armor] = armor_

                    except ValueError:
                        ...

                elif name in player_command_set_delay_name:
                    try:
                        delay_ = float(value)
                        self.game.player.characteristics.characteristics[0][
                            delay] = delay_

                    except ValueError:
                        ...

                elif name in player_command_set_armor_piercing_name:
                    try:
                        armor_piercing_ = float(value)
                        self.game.player.characteristics.characteristics[0][
                            armor_piercing] = armor_piercing_

                    except ValueError:
                        ...

                elif name in player_command_set_bullet_size_x_name:
                    try:
                        bullet_size_x_ = float(value)
                        self.game.player.characteristics.characteristics[0][
                            bullet_size_x] = bullet_size_x_

                    except ValueError:
                        ...

                elif name in player_command_set_bullet_size_y_name:
                    try:
                        bullet_size_y_ = float(value)
                        self.game.player.characteristics.characteristics[0][
                            bullet_size_y] = bullet_size_y_

                    except ValueError:
                        ...

                elif name in player_command_set_bullet_damage_name:
                    try:
                        bullet_damage_ = float(value)
                        self.game.player.characteristics.characteristics[0][
                            bullet_damage] = bullet_damage_

                    except ValueError:
                        ...

                elif name in player_command_set_critical_coefficient_name:
                    try:
                        critical_coefficient_ = float(value)
                        self.game.player.characteristics.characteristics[0][
                            critical_coefficient] = critical_coefficient_

                    except ValueError:
                        ...

                elif name in player_command_set_critical_chance_name:
                    try:
                        critical_chance_ = float(value)
                        self.game.player.characteristics.characteristics[0][
                            critical_chance] = critical_chance_

                    except ValueError:
                        ...
                elif name in player_command_set_scatter_name:
                    try:
                        scatter_ = float(value)
                        self.game.player.characteristics.characteristics[0][
                            scatter] = scatter_

                    except ValueError:
                        ...

                elif name in player_command_set_bullet_life_time_name:
                    try:
                        bullet_life_time_ = float(value)
                        self.game.player.characteristics.characteristics[0][
                            bullet_life_time] = bullet_life_time_

                    except ValueError:
                        ...

                elif name in player_command_set_bullet_velocity_name:
                    try:
                        bullet_velocity_ = float(value)
                        self.game.player.characteristics.characteristics[0][
                            bullet_velocity] = bullet_velocity_

                    except ValueError:
                        ...

                elif name in player_command_set_damage_delay_name:
                    try:
                        damage_delay_ = float(value)
                        self.game.player.characteristics.characteristics[0][
                            damage_delay] = damage_delay_

                    except ValueError:
                        ...
                elif name in player_command_add_item:
                    try:
                        name = value
                        rank = self.game.player.characteristics.getitem.get_rank(name)
                        self.game.player.characteristics.apply(name, rank)

                    except ValueError:
                        ...
                    except ExceptionNotFoundName:
                        ...
        else:
            ...
        self.game.player.update_characteristics()

