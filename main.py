"""pg main loop"""
import sys
import warnings

import pygame as pg
from tqdm import tqdm

from source.Game import GAME

pg.init()
warnings.filterwarnings("ignore", category=RuntimeWarning)
game = GAME

with tqdm() as pbar:
    while game.running:
        game.play()
        pbar.update(1)

pg.quit()
sys.exit()
