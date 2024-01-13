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
        game.change_pseudo_constants()
        game.check_events()
        game.shoot()
        game.calc_calculations()
        game.draw()
        game.draw_console()
        game.draw_interface()
        game.end_cycle()
        pbar.update(1)

pg.quit()
sys.exit()
