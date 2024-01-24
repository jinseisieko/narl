"""pg main loop"""
import sys
import warnings

from tqdm import tqdm
import pygame as pg
from States.Game import GAME

pg.init()
warnings.filterwarnings("ignore", category=RuntimeWarning)
game = GAME

with tqdm() as pbar:
    while game.running:
        game.play()
        pbar.update(1)

pg.quit()
sys.exit()
