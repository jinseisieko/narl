import pygame as pg

images = {}


def init_images_for_game():
    global images
    images = {
        'grass1': pg.transform.scale(pg.image.load(r"..\resource\image\mapImages\grasses\grass1.png"), (400, 400)),
        'grass2': pg.transform.scale(pg.image.load(r"..\resource\image\mapImages\grasses\grass2.png"), (400, 400)),
        'grass3': pg.transform.scale(pg.image.load(r"..\resource\image\mapImages\grasses\grass3.png"), (400, 400)),
        'grass4': pg.transform.scale(pg.image.load(r"..\resource\image\mapImages\grasses\grass4.png"), (400, 400)),
        'test_player': pg.transform.scale(pg.image.load(r"..\resource\image\playerImages\test_player.png"), (80, 80)),
        'test_bullet': pg.transform.scale(pg.image.load(r"..\resource\image\bulletImages\test_bullet.png"), (10, 10)),
        'test_enemy':  pg.transform.scale(pg.image.load(r"..\resource\image\enemyImages\test_enemy.png"), (16, 16)),
        'cursor': pg.transform.scale(pg.image.load(r"..\resource\image\other\cursor.png"), (32, 32)),
    }


def get_images_for_game():
    global images
    return images
