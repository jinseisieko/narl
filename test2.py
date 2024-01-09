"""pg main loop"""
import sys
import warnings

from tqdm import tqdm

from Game import *

pg.init()
warnings.filterwarnings("ignore", category=RuntimeWarning)
Game = Game()
Game.make_borders()
Game.create_enemies()
Game.create_obstacles()

with (tqdm() as pbar):
    while Game.running:
        Game.change_pseudo_constants()
        Game.check_events()
        Game.shoot()
        Game.calc_calculations()
        Game.draw()
        Game.draw_console()
        Game.end_cycle()
        pbar.update(1)

pg.quit()
sys.exit()
