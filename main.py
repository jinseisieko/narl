"""pg main loop"""
import sys
import warnings
import peewee

import pygame as pg
from tqdm import tqdm

from source.MainWindow import MAIN_WINDOW

_ = peewee.Model
pg.init()
warnings.filterwarnings("ignore", category=RuntimeWarning)
mainWindow = MAIN_WINDOW

with tqdm() as pbar:
    while mainWindow.running:
        mainWindow.play()
        pbar.update(1)

pg.quit()
sys.exit()
