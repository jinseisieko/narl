"""constants"""
import tkinter as tk

import numpy as np
import pygame

pygame.init()

FIELD_WIDTH: np.int_ = 5000
FIELD_HEIGHT: np.int_ = 5000
WIDTH: np.int_ = tk.Tk().winfo_screenwidth()
HEIGHT: np.int_ = tk.Tk().winfo_screenheight()
MOVE_SCREEN_RECT_X: np.int_ = WIDTH // 8
MOVE_SCREEN_RECT_Y: np.int_ = HEIGHT // 8

BACKGROUND_PICTURE_SIZE: np.int_ = 400

FPS: np.int_ = 120

ITEMS_COUNT: int = 44
H: int = 7

PLAYER_HALF_SIZE_X: np.int_ = 40  # pixels
PLAYER_HALF_SIZE_Y: np.int_ = 40  # pixels
PLAYER_MAX_VELOCITY = np.float_(500)  # pixels / second
PLAYER_SLOWDOWN: np.float_ = np.float_(600)  # pixels / second ** 2
PLAYER_ACCELERATION: np.float_ = np.float_(1500)  # pixels / second ** 2
PLAYER_MAX_HP: np.int_ = 100  # int
PLAYER_ARMOR: np.float_ = np.float_(0)  # int
PLAYER_DELAY: np.float_ = np.float_(0.01)  # seconds
PLAYER_ARMOR_PIERCING: np.float_ = np.float_(2)  # int
PLAYER_BULLET_SIZE_X: np.float_ = np.float_(10)  # pixels
PLAYER_BULLET_SIZE_Y: np.float_ = np.float_(10)  # pixels
PLAYER_BULLET_DAMAGE: np.float_ = np.float_(2)  # int
PLAYER_CRITICAL_COEFFICIENT: np.float_ = np.float_(2)  # any
PLAYER_CRITICAL_CHANCE: np.float_ = np.float_(0.8)  # from 0 to 1
PLAYER_SCATTER: np.float_ = np.float_(1)  # radians
PLAYER_BULLET_LIVE_TIME: np.float_ = np.float_(2)  # seconds
PLAYER_BULLET_VELOCITY: np.float_ = np.float_(1000)  # pixels/second
PLAYER_DAMAGE_DELAY: np.float_ = np.float_(0.5)  # seconds

RED: tuple[np.int_, np.int_, np.int_] = (255, 0, 0)
GREEN: tuple[np.int_, np.int_, np.int_] = (0, 255, 0)
BLUE: tuple[np.int_, np.int_, np.int_] = (0, 0, 255)
GRAY: tuple[np.int_, np.int_, np.int_] = (200, 200, 200)
BLACK: tuple[np.int_, np.int_, np.int_] = (0, 0, 0)

# fonts
FONT_CONSOLE = (None, 27)
FONT_PAUSE = (None, 46)
FONT_FPS = (None, 27)
FONT_CHARACTERISTICS = (None, 27)
FONT_COUNT_OBJECTS = (None, 27)

ENEMY_SIZE_X: np.float_ = np.float_(25)  # pixels
ENEMY_SIZE_Y: np.float_ = np.float_(25)  # pixels
ENEMY_HP: np.float_ = np.float_(10)  # int
ENEMY_DAMAGE: np.float_ = np.float_(1)  # int
ENEMY_MAX_VELOCITY: np.float_ = np.float_(300)  # pixels / second
ENEMY_ARMOR: np.float_ = np.float_(3)  # int
COLLISIONS_REPELLING: np.float_ = np.float_(25)  # pixels / second

CLOCK = pygame.time.Clock()

MAX_ENEMIES: np.int_ = np.int_(100)
MAX_BULLETS: np.int_ = np.int_(300)
MAX_OBSTACLES: np.int_ = np.int_(100)

SIZE_HP_INTERFACE_Y = HEIGHT / 2
SIZE_HP_INTERFACE_X = 20

COORD_HP_INTERFACE_X = 10
COORD_HP_INTERFACE_Y = 10

COORD_CHARACTERISTICS_INTERFACE_X = 40
COORD_CHARACTERISTICS_INTERFACE_Y = 10
FONT_SIZE_CHARACTERISTICS = 35
INDENT_CHARACTERISTICS_INTERFACE = 25
