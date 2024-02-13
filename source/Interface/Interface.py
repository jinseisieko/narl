"""classes interfaces"""
import pygame as pg

from source.Constants import *
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

        self.items_surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)

    def calc(self):
        self.ratio_hp = self.player[0][hp] / self.player[0][max_hp]

    def update_items_surface(self):
        array_draw = self.game.player.characteristics.array_draw
        for i, row in enumerate(array_draw):
            for j, name in enumerate(row):
                if not (name in get_images_for_items()):
                    name = 'no-image'
                self.items_surface.blit(get_images_for_items()[name],
                                        (WIDTH - 37 * NUMBER_OF_ITEMS - 10 + j * 37, 10 + i * 37))

    def draw(self, screen: pg.Surface):
        # draw hp

        pygame.draw.rect(screen, (255, 255, 255),
                         (COORD_HP_INTERFACE_X, COORD_HP_INTERFACE_Y, SIZE_HP_INTERFACE_X, SIZE_HP_INTERFACE_Y),
                         border_radius=3)

        pygame.draw.rect(screen, (255, 0, 0),
                         (COORD_HP_INTERFACE_X, COORD_HP_INTERFACE_Y + (1 - self.ratio_hp) * SIZE_HP_INTERFACE_Y,
                          SIZE_HP_INTERFACE_X, SIZE_HP_INTERFACE_Y * self.ratio_hp),
                         border_radius=3)
        pygame.draw.rect(screen, (0, 0, 0),
                         (COORD_HP_INTERFACE_X, COORD_HP_INTERFACE_Y, SIZE_HP_INTERFACE_X, SIZE_HP_INTERFACE_Y),
                         border_radius=3, width=4)

        # characteristics
        for i, (j, name) in enumerate(zip(self.index_needed_characteristics, self.index_needed_characteristics_name)):
            screen.blit(get_images_for_game()[name],
                        (COORD_CHARACTERISTICS_INTERFACE_X,
                         COORD_CHARACTERISTICS_INTERFACE_Y + INDENT_CHARACTERISTICS_INTERFACE * i))
            screen.blit(self.font.render(str(self.player[0][j])[:7] if self.player[0][j] > 1e-4 else "0", True, "#3A2980"),
                        (COORD_CHARACTERISTICS_INTERFACE_X + 33,
                         COORD_CHARACTERISTICS_INTERFACE_Y + INDENT_CHARACTERISTICS_INTERFACE * i))

        # items
        screen.blit(self.items_surface, (0, 0))
