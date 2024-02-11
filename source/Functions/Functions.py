import numpy as np
from source.Settings.SettingsData import *


def DT(clock: pg.time.Clock):
    return 0.001 * clock.get_time()


def set_direction(pressed):
    direction: np.ndarray = np.array([0, 0])
    if pressed[CONTROLS["LEFT"]]:
        direction[0] -= 1
    if pressed[CONTROLS["RIGHT"]]:
        direction[0] += 1
    if pressed[CONTROLS["FORWARD"]]:
        direction[1] -= 1
    if pressed[CONTROLS["BACKWARD"]]:
        direction[1] += 1
    return direction
