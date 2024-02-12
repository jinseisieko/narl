import pygame as pg

images = {}


def init_images_for_game():
    global images
    images = {
        'grass1': pg.transform.scale(pg.image.load(r"resource\image\mapImages\grasses\grass1.png"), (400, 400)),
        'grass2': pg.transform.scale(pg.image.load(r"resource\image\mapImages\grasses\grass2.png"), (400, 400)),
        'grass3': pg.transform.scale(pg.image.load(r"resource\image\mapImages\grasses\grass3.png"), (400, 400)),
        'grass4': pg.transform.scale(pg.image.load(r"resource\image\mapImages\grasses\grass4.png"), (400, 400)),

        'test_player': pg.transform.scale(pg.image.load(r"resource\image\playerImages\test_player.png"), (80, 80)),
        'test_bullet': pg.transform.scale(pg.image.load(r"resource\image\bulletImages\test_bullet.png"), (10, 10)),
        'test_enemy': pg.transform.scale(pg.image.load(r"resource\image\enemyImages\test_enemy.png"), (16, 16)),
        'cursor': pg.transform.scale(pg.image.load(r"resource\image\other\cursor.png"), (32, 32)),

        'forest1': pg.transform.scale(pg.image.load(r"resource\image\mapImages\forest\forest1.png"), (400, 400)),
        'forest2': pg.transform.scale(pg.image.load(r"resource\image\mapImages\forest\forest2.png"), (400, 400)),
        'forest3': pg.transform.scale(pg.image.load(r"resource\image\mapImages\forest\forest3.png"), (400, 400)),
        'forest4': pg.transform.scale(pg.image.load(r"resource\image\mapImages\forest\forest4.png"), (400, 400)),
        'forest5': pg.transform.scale(pg.image.load(r"resource\image\mapImages\forest\forest5.png"), (400, 400)),
        'forest6': pg.transform.scale(pg.image.load(r"resource\image\mapImages\forest\forest6.png"), (400, 400)),
        'forest7': pg.transform.scale(pg.image.load(r"resource\image\mapImages\forest\forest7.png"), (400, 400)),
        'forest8': pg.transform.scale(pg.image.load(r"resource\image\mapImages\forest\forest8.png"), (400, 400)),
        'forest9': pg.transform.scale(pg.image.load(r"resource\image\mapImages\forest\forest9.png"), (400, 400)),
        'forest10': pg.transform.scale(pg.image.load(r"resource\image\mapImages\forest\forest10.png"), (400, 400)),
        'forest11': pg.transform.scale(pg.image.load(r"resource\image\mapImages\forest\forest11.png"), (400, 400)),
        'forest12': pg.transform.scale(pg.image.load(r"resource\image\mapImages\forest\forest12.png"), (400, 400)),
        'forest13': pg.transform.scale(pg.image.load(r"resource\image\mapImages\forest\forest13.png"), (400, 400)),
        'forest14': pg.transform.scale(pg.image.load(r"resource\image\mapImages\forest\forest14.png"), (400, 400)),
        'forest15': pg.transform.scale(pg.image.load(r"resource\image\mapImages\forest\forest15.png"), (400, 400)),

        'acceleration': pg.transform.scale(pg.image.load(r"resource\image\interface\acceleration.png"), (32, 32)),
        'armor': pg.transform.scale(pg.image.load(r"resource\image\interface\armor.png"), (32, 32)),
        'armor_piercing': pg.transform.scale(pg.image.load(r"resource\image\interface\armor_piercing.png"), (32, 32)),
        'bullet_damage': pg.transform.scale(pg.image.load(r"resource\image\interface\bullet_damage.png"), (32, 32)),
        'bullet_life_time': pg.transform.scale(pg.image.load(r"resource\image\interface\bullet_life_time.png"),
                                               (32, 32)),
        'bullet_velocity': pg.transform.scale(pg.image.load(r"resource\image\interface\bullet_velocity.png"), (32, 32)),
        'critical_chance': pg.transform.scale(pg.image.load(r"resource\image\interface\critical_chance.png"), (32, 32)),
        'critical_coefficient': pg.transform.scale(pg.image.load(r"resource\image\interface\critical_coefficient.png"),
                                                   (32, 32)),
        'damage_delay': pg.transform.scale(pg.image.load(r"resource\image\interface\damage_delay.png"), (32, 32)),
        'delay': pg.transform.scale(pg.image.load(r"resource\image\interface\delay.png"), (32, 32)),
        'max_velocity': pg.transform.scale(pg.image.load(r"resource\image\interface\max_velocity.png"), (32, 32)),
        'scatter': pg.transform.scale(pg.image.load(r"resource\image\interface\scatter.png"), (32, 32)),
    }


def get_images_for_game():
    global images
    return images
