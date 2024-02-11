from collections import defaultdict

import pygame as pg

from source.Constants import FPS, np

MASTER_VOLUME = [1.0]
MUSIC_VOLUME = [1.0]
SFX_VOLUME = [1.0]
MAX_FPS = [FPS]
CONTROLS = {
    "FORWARD": pg.K_w,
    "BACKWARD": pg.K_s,
    "LEFT": pg.K_a,
    "RIGHT": pg.K_d,
    "MENU": pg.K_ESCAPE,
    "SHOOT": pg.K_SPACE,
    "OPEN_CONSOLE": pg.K_F1
}

# CONTROLS = defaultdict(lambda: -1, CONTROLS)
# CONTROLS_2 = defaultdict(lambda: -1, CONTROLS_2)


def update(a, b, c, d):
    global MASTER_VOLUME, MUSIC_VOLUME, SFX_VOLUME, MAX_FPS
    if a.replace(".", "").isnumeric():
        MASTER_VOLUME[0] = np.float_(a)
    if b.replace(".", "").isnumeric():
        MUSIC_VOLUME[0] = np.float_(b)
    if c.replace(".", "").isnumeric():
        SFX_VOLUME[0] = np.float_(c)
    if d.replace(".", "").isnumeric():
        MAX_FPS[0] = np.float_(d)
