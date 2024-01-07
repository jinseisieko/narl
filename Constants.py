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

PLAYER_HALF_SIZE: np.int_ = 40  # matches the size of the player's image
PLAYER_MAX_VELOCITY = np.float_(500)
PLAYER_SLOWDOWN: np.float_ = np.float_(600)
PLAYER_ACCELERATION: np.float_ = np.float_(1500)
PLAYER_MAX_HP: np.int_ = 10
PLAYER_ARMOR: np.float_ = np.float_(0)
PLAYER_DELAY: np.float_ = np.float_(0.01)
PLAYER_ARMOR_PIERCING: np.float_ = np.float_(0)
PLAYER_BULLET_SIZE_X: np.float_ = np.float_(10)
PLAYER_BULLET_SIZE_Y: np.float_ = np.float_(10)
PLAYER_BULLET_DAMAGE: np.float_ = np.float_(1)
PLAYER_CRITICAL_COEFFICIENT: np.float_ = np.float_(0)
PLAYER_CRITICAL_CHANCE: np.float_ = np.float_(0)
PLAYER_SCATTER: np.float_ = np.float_(0)
PLAYER_BULLET_LIVE_TIME: np.float_ = np.float_(5)
PLAYER_BULLET_VELOCITY: np.float_ = np.float_(500)

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

ENEMY_SIZE_X: np.int_ = 25
ENEMY_SIZE_Y: np.int_ = 25
ENEMY_HP: np.int_ = 10
ENEMY_DAMAGE: np.int_ = 1
ENEMY_MAX_VELOCITY: np.int_ = 300
COLLISIONS_REPELLING: np.float_ = np.float_(300)

CLOCK = pygame.time.Clock()

MAX_ENEMIES: np.int_ = np.int_(100)
MAX_BULLETS: np.int_ = np.int_(200)
MAX_OBSTACLES: np.int_ = np.int_(100)
