"""pg main loop"""
import sys
import warnings

from tqdm import tqdm
import pygame as pg
from source.Game import GAME

pg.init()
game = GAME

with tqdm() as pbar:
    while game.running:
        game.play()
        pbar.update(1)

pg.quit()
sys.exit()
