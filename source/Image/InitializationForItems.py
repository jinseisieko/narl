import pygame as pg

images = {}


def init_images_for_items():
    global images
    images = {
        'no-image': pg.transform.scale(pg.image.load(r"resource\image\ItemImages\no-image.png"), (32, 32)),
        'fire': pg.transform.scale(pg.image.load(r"resource\image\ItemImages\fire.png"), (32, 32)),
        'apple': pg.transform.scale(pg.image.load(r"resource\image\ItemImages\apple.png"), (32, 32)),
        'boot': pg.transform.scale(pg.image.load(r"resource\image\ItemImages\boot.png"), (32, 32)),
        'armor': pg.transform.scale(pg.image.load(r"resource\image\ItemImages\armor.png"), (32, 32)),
        'book': pg.transform.scale(pg.image.load(r"resource\image\ItemImages\book.png"), (32, 32)),
        'brick': pg.transform.scale(pg.image.load(r"resource\image\ItemImages\brick.png"), (32, 32)),
        'glass_shard': pg.transform.scale(pg.image.load(r"resource\image\ItemImages\glass_shard.png"), (32, 32)),
        'rebound': pg.transform.scale(pg.image.load(r"resource\image\ItemImages\rebound.png"), (32, 32)),
        'shotgun': pg.transform.scale(pg.image.load(r"resource\image\ItemImages\shotgun.png"), (32, 32)),

        'butterfly': pg.transform.scale(pg.image.load(r"resource\image\ItemImages\butterfly.png"), (32, 32)),
        'hammer': pg.transform.scale(pg.image.load(r"resource\image\ItemImages\hammer.png"), (32, 32)),
        'scissors': pg.transform.scale(pg.image.load(r"resource\image\ItemImages\scissors.png"), (32, 32)),
        'scope': pg.transform.scale(pg.image.load(r"resource\image\ItemImages\scope.png"), (32, 32)),
        'sunflower': pg.transform.scale(pg.image.load(r"resource\image\ItemImages\sunflower.png"), (32, 32)),
    }


def get_images_for_items():
    global images
    return images
