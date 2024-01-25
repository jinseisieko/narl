import pygame as pg

images = {}


def init_images_for_items():
    global images
    images = {
        'no-image': pg.transform.scale(pg.image.load(r"..\resource\image\ItemImages\no-image.png"), (32, 32)),
    }


def get_images_for_items():
    global images
    return images
