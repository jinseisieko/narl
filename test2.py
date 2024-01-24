"""pg main loop"""
import sys
import warnings

from tqdm import tqdm
from Game import *

pg.init()
warnings.filterwarnings("ignore", category=RuntimeWarning)
game = GAME

with tqdm() as pbar:
    while game.running:
        game.play()
        pbar.update(1)

pg.quit()
sys.exit()
