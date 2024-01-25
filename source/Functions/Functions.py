import numpy as np
import pygame as pg


def DT(clock: pg.time.Clock):
    return 0.001 * clock.get_time()


def set_direction(pressed):
    direction: np.ndarray = np.array([0, 0])
    if pressed[pg.K_a]:
        direction[0] -= 1
    if pressed[pg.K_d]:
        direction[0] += 1
    if pressed[pg.K_w]:
        direction[1] -= 1
    if pressed[pg.K_s]:
        direction[1] += 1
    return direction
