"""constants"""
import tkinter as tk

import numpy as np
import pygame

pygame.init()

FIELD_WIDTH: np.int_ = np.int_(5000)
FIELD_HEIGHT: np.int_ = np.int_(5000)
WIDTH: np.int_ = np.int_(tk.Tk().winfo_screenwidth())
HEIGHT: np.int_ = np.int_(tk.Tk().winfo_screenheight())
MOVE_SCREEN_RECT_X: np.int_ = np.int_(WIDTH // 8)
MOVE_SCREEN_RECT_Y: np.int_ = np.int_(HEIGHT // 8)
SPAWN_LINE: np.int_ = np.int_(50)
KILL_LINE: np.int_ = np.int_(100)

BACKGROUND_PICTURE_SIZE: np.int_ = np.int_(400)

FPS: np.float_ = np.float_(120)

PLAYER_HALF_SIZE_X: np.int_ = np.int_(40)  # pixels
PLAYER_HALF_SIZE_Y: np.int_ = np.int_(40)  # pixels
PLAYER_MAX_VELOCITY = np.float_(500)  # pixels / second
PLAYER_SLOWDOWN: np.float_ = np.float_(600)  # pixels / second ** 2
PLAYER_ACCELERATION: np.float_ = np.float_(1500)  # pixels / second ** 2
PLAYER_MAX_HP: np.int_ = np.int_(10)  # int
PLAYER_ARMOR: np.float_ = np.float_(0)  # int
PLAYER_DELAY: np.float_ = np.float_(1)  # seconds
PLAYER_ARMOR_PIERCING: np.float_ = np.float_(0)  # int
PLAYER_BULLET_SIZE_X: np.float_ = np.float_(10)  # pixels
PLAYER_BULLET_SIZE_Y: np.float_ = np.float_(10)  # pixels
PLAYER_BULLET_DAMAGE: np.float_ = np.float_(3)  # int
PLAYER_CRITICAL_COEFFICIENT: np.float_ = np.float_(1.1)  # any
PLAYER_CRITICAL_CHANCE: np.float_ = np.float_(0.1)  # from 0 to 1
PLAYER_SCATTER: np.float_ = np.float_(0.001)  # radians
PLAYER_BULLET_LIVE_TIME: np.float_ = np.float_(2)  # seconds
PLAYER_BULLET_VELOCITY: np.float_ = np.float_(800)  # pixels/second
PLAYER_DAMAGE_DELAY: np.float_ = np.float_(0.6)  # seconds
PLAYER_NEED_EXP: np.float_ = np.float_(5)  # seconds
PLAYER_SLOWDOWN_FACTOR = PLAYER_SLOWDOWN / PLAYER_ACCELERATION

ENEMY_SIZE_X: np.float_ = np.float_(25)  # pixels
ENEMY_SIZE_Y: np.float_ = np.float_(25)  # pixels
ENEMY_HP: np.float_ = np.float_(10)  # int
ENEMY_DAMAGE: np.float_ = np.float_(1)  # int
ENEMY_MAX_VELOCITY: np.float_ = np.float_(300)  # pixels / second
ENEMY_ARMOR: np.float_ = np.float_(3)  # int
COLLISIONS_REPELLING: np.float_ = np.float_(25)  # pixels / second

RED: tuple[int, int, int] = (255, 0, 0)
GREEN: tuple[int, int, int] = (0, 255, 0)
BLUE: tuple[int, int, int] = (0, 0, 255)
GRAY: tuple[int, int, int] = (200, 200, 200)
BLACK: tuple[int, int, int] = (0, 0, 0)

# fonts
FONT_CONSOLE: tuple[(None, str), int] = (None, 27)
FONT_PAUSE: tuple[(None, str), int] = (None, 46)
FONT_FPS: tuple[(None, str), int] = (None, 27)
FONT_CHARACTERISTICS: tuple[(None, str), int] = (None, 27)
FONT_COUNT_OBJECTS: tuple[(None, str), int] = (None, 27)

CLOCK: pygame.time.Clock = pygame.time.Clock()

MAX_ENEMIES: np.int_ = np.int_(100)
MAX_PLAYER_BULLETS: np.int_ = np.int_(300)
MAX_ENEMY_BULLETS: np.int_ = np.int_(300)
MAX_OBSTACLES: np.int_ = np.int_(100)

SIZE_HP_INTERFACE_Y: int = HEIGHT // 2
SIZE_HP_INTERFACE_X: int = 20

COORD_HP_INTERFACE_X: int = 10
COORD_HP_INTERFACE_Y: int = 10

COORD_CHARACTERISTICS_INTERFACE_X: int = 40
COORD_CHARACTERISTICS_INTERFACE_Y: int = 10
FONT_SIZE_CHARACTERISTICS: int = 35
INDENT_CHARACTERISTICS_INTERFACE: int = 33

NUMBER_OF_ITEMS: int = 5

MUSIC_FOR_LEVEL: dict = {
    1: ["arthur-vyncke-cherry-metal(chosic.com).mp3", "Adventures-in-Adventureland(chosic.com).mp3",
        "Adventures-in-Adventureland(chosic.com).mp3"]
}
