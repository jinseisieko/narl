"""classes interfaces"""
import pygame as pg

from source.Calculations.Data import *
from source.Image.InitializationForGame import get_images_for_game
from source.Image.InitializationForItems import get_images_for_items
from source.PlayerIndexes import *


class Interface:
    def __init__(self, game):
        self.game = game
        self.player = self.game.player.characteristics.characteristics
        self.ratio_hp = self.player[0][hp] / self.player[0][max_hp]

        self.font = pg.font.Font(None, FONT_SIZE_CHARACTERISTICS)
        self.index_needed_characteristics = [max_velocity, acceleration, armor, armor_piercing, delay, bullet_damage,
                                             bullet_velocity, bullet_life_time, critical_chance, critical_coefficient,
                                             scatter, damage_delay]
        self.index_needed_characteristics_name = ["max_velocity", "acceleration", "armor", "armor_piercing", "delay",
                                                  "bullet_damage",
                                                  "bullet_velocity", "bullet_life_time", "critical_chance",
                                                  "critical_coefficient",
                                                  "scatter", "damage_delay"]

        self.items_surface = pg.Surface((WIDTH, HEIGHT), pg.SRCALPHA)

        self.make_bar_background()

    def make_bar_background(self):
        self.level_background = pg.Surface((SIZE_PLAYER_LEVEL_INTERFACE_X,
                                            SIZE_PLAYER_LEVEL_INTERFACE_Y))
        clr_l = "#24d3e8"
        clr_r = "#af2dd2"

        left_color = (int(clr_l[1:3], 16), int(clr_l[3:5], 16), int(clr_l[5:7], 16))

        right_color = (int(clr_r[1:3], 16), int(clr_r[3:5], 16), int(clr_r[5:7], 16))

        for i in range(SIZE_PLAYER_LEVEL_INTERFACE_Y):
            color = (
                int(left_color[0] + (right_color[0] - left_color[0]) * i / SIZE_PLAYER_LEVEL_INTERFACE_Y),
                int(left_color[1] + (right_color[1] - left_color[1]) * i / SIZE_PLAYER_LEVEL_INTERFACE_Y),
                int(left_color[2] + (right_color[2] - left_color[2]) * i / SIZE_PLAYER_LEVEL_INTERFACE_Y)
            )
            pg.draw.rect(self.level_background, color, (0, i, SIZE_PLAYER_LEVEL_INTERFACE_X, 1))

        self.wave_background = pg.Surface((SIZE_WAVE_INTERFACE_X,
                                           SIZE_WAVE_INTERFACE_Y))
        clr_l = "#d67a00"
        clr_r = "#00d642"

        left_color = (int(clr_l[1:3], 16), int(clr_l[3:5], 16), int(clr_l[5:7], 16))

        right_color = (int(clr_r[1:3], 16), int(clr_r[3:5], 16), int(clr_r[5:7], 16))

        for i in range(SIZE_WAVE_INTERFACE_Y):
            color = (
                int(left_color[0] + (right_color[0] - left_color[0]) * i / SIZE_WAVE_INTERFACE_Y),
                int(left_color[1] + (right_color[1] - left_color[1]) * i / SIZE_WAVE_INTERFACE_Y),
                int(left_color[2] + (right_color[2] - left_color[2]) * i / SIZE_WAVE_INTERFACE_Y)
            )
            pg.draw.rect(self.wave_background, color, (0, i, SIZE_WAVE_INTERFACE_X, 1))

    def calc(self):
        self.ratio_hp = self.player[0][hp] / self.player[0][max_hp]

    def update_items_surface(self):
        array_draw = self.game.player.characteristics.array_draw
        for i, row in enumerate(array_draw):
            for j, name in enumerate(row):
                if not (name in get_images_for_items()):
                    name = 'no-image'
                self.items_surface.blit(get_images_for_items()[name],
                                        (WIDTH - 37 * NUMBER_OF_ITEMS - 10 + j * 37 - 50, 10 + i * 37))

    def draw(self, screen: pg.Surface):
        # draw bars

        screen.blit(self.level_background, (COORD_PLAYER_LEVEL_INTERFACE_X + 3, COORD_PLAYER_LEVEL_INTERFACE_Y + 3))
        screen.blit(self.wave_background, (COORD_WAVE_INTERFACE_X + 3, COORD_WAVE_INTERFACE_Y + 3))

        pg.draw.rect(screen, (0, 0, 0),
                     (COORD_PLAYER_LEVEL_INTERFACE_X, COORD_PLAYER_LEVEL_INTERFACE_Y,
                      SIZE_PLAYER_LEVEL_INTERFACE_X + 6, SIZE_PLAYER_LEVEL_INTERFACE_Y + 6),
                     border_radius=3, width=4)

        pg.draw.rect(screen, (0, 0, 0),
                     (COORD_WAVE_INTERFACE_X, COORD_WAVE_INTERFACE_Y,
                      SIZE_WAVE_INTERFACE_X + 6, SIZE_WAVE_INTERFACE_Y + 6),
                     border_radius=3, width=4)

        pg.draw.rect(screen, "gold",
                     (COORD_WAVE_INTERFACE_X - 1, COORD_WAVE_INTERFACE_Y + wave[8] / wave[7] * SIZE_WAVE_INTERFACE_Y,
                      SIZE_WAVE_INTERFACE_X + 8, 6), border_radius=3)

        pg.draw.rect(screen, "gold",
                     (COORD_PLAYER_LEVEL_INTERFACE_X - 1,
                      COORD_PLAYER_LEVEL_INTERFACE_Y + player[0, 28] / player[0, 29] * SIZE_PLAYER_LEVEL_INTERFACE_Y,
                      SIZE_PLAYER_LEVEL_INTERFACE_X + 8, 6), border_radius=3)

        pg.draw.rect(screen, (255, 255, 255),
                     (COORD_HP_INTERFACE_X, COORD_HP_INTERFACE_Y, SIZE_HP_INTERFACE_X, SIZE_HP_INTERFACE_Y),
                     border_radius=3)

        pg.draw.rect(screen, "#eb002a",
                     (COORD_HP_INTERFACE_X, COORD_HP_INTERFACE_Y + (1 - self.ratio_hp) * SIZE_HP_INTERFACE_Y,
                      SIZE_HP_INTERFACE_X, SIZE_HP_INTERFACE_Y * self.ratio_hp),
                     border_radius=3)
        pg.draw.rect(screen, (0, 0, 0),
                     (COORD_HP_INTERFACE_X, COORD_HP_INTERFACE_Y, SIZE_HP_INTERFACE_X, SIZE_HP_INTERFACE_Y),
                     border_radius=3, width=4)

        # characteristics
        for i, (j, name) in enumerate(zip(self.index_needed_characteristics, self.index_needed_characteristics_name)):
            screen.blit(get_images_for_game()[name],
                        (COORD_CHARACTERISTICS_INTERFACE_X,
                         COORD_CHARACTERISTICS_INTERFACE_Y + INDENT_CHARACTERISTICS_INTERFACE * i))
            screen.blit(
                self.font.render(str(self.player[0][j])[:7] if self.player[0][j] > 1e-4 else "0", True, "#3A2980"),
                (COORD_CHARACTERISTICS_INTERFACE_X + 33,
                 COORD_CHARACTERISTICS_INTERFACE_Y + INDENT_CHARACTERISTICS_INTERFACE * i))

        # items
        screen.blit(self.items_surface, (0, 0))
