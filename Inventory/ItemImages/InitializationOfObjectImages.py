import pygame as pg

images = {}


def init_images():
    global images
    images = {
        'no-image': pg.transform.scale(pg.image.load(r"Inventory\ItemImages\no-image.png"), (32, 32)),
    }


def get_images():
    global images
    return images
