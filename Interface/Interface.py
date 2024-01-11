"""classes interfaces"""
import pygame as pg

from Constants import *
from PlayerIndexs import *


class Interface:
    def __init__(self, player):
        self.player = player
        self.ratio_hp = self.player[0][hp] / self.player[0][max_hp]

        self.font = pg.font.Font(None, FONT_SIZE_CHARACTERISTICS)
        self.index_needed_characteristics = [max_velocity, acceleration, armor, armor_piercing, delay, bullet_damage,
                                             bullet_velocity, bullet_life_time, critical_chance, critical_coefficient,
                                             scatter, damage_delay]

    def calc(self):
        self.ratio_hp = self.player[0][hp] / self.player[0][max_hp]

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
        for i, j in enumerate(self.index_needed_characteristics):
            screen.blit(self.font.render(str(self.player[0][j]), True, "black"),
                        (COORD_CHARACTERISTICS_INTERFACE_X,
                         COORD_CHARACTERISTICS_INTERFACE_Y + INDENT_CHARACTERISTICS_INTERFACE * i))
