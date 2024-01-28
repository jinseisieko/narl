import pygame as pg

images = {}


def init_images_for_items():
    global images
    images = {
        'no-image': pg.transform.scale(pg.image.load(r"..\resource\image\ItemImages\no-image.png"), (32, 32)),
        'fire': pg.transform.scale(pg.image.load(r"..\resource\image\ItemImages\fire.png"), (32, 32)),
        'stone': pg.transform.scale(pg.image.load(r"..\resource\image\ItemImages\stone.png"), (32, 32)),
        'apple': pg.transform.scale(pg.image.load(r"..\resource\image\ItemImages\apple.png"), (32, 32)),
        'boot': pg.transform.scale(pg.image.load(r"..\resource\image\ItemImages\boot.png"), (32, 32)),
    }


def get_images_for_items():
    global images
    return images
