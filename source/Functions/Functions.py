from source.Constants import *
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


def get_key_code(key_name):
    return KEY_CODE_REVERSE.get(key_name, None)
