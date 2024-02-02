from collections import defaultdict

import pygame as pg

from source.Constants import FPS

MASTER_VOLUME = 1
MUSIC_VOLUME = 1
SFX_VOLUME = 1
MAX_FPS = FPS
CONTROLS_1 = {
    "FORWARD": pg.K_w,
    "BACKWARD": pg.K_s,
    "LEFT": pg.K_a,
    "RIGHT": pg.K_d,
    "MENU": pg.K_ESCAPE,
    "SHOOT": 1,
    "PRESS": 1,
    "OPEN_CONSOLE": pg.K_F1
}

CONTROLS_2 = {
    "SHOOT": pg.K_SPACE,
}

CONTROLS_1 = defaultdict(lambda: -1, CONTROLS_1)
CONTROLS_2 = defaultdict(lambda: -1, CONTROLS_2)
