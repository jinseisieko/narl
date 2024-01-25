import pygame

sprites: dict = {
    'player_nr': pygame.image.load(r"../resource/image/image_old/player/player_nr.png"),
    'player_pd': pygame.image.load(r"../resource/image/image_old/player/player_pd.png"),
    'phat': pygame.image.load(r"../resource/image/image_old/player/hat.png"),
    'default_projectile': None,
    'projectile30': pygame.image.load(r"../resource/image/image_old/projectiles/projectile30.png"),
    'cursor': pygame.image.load(r"../resource/image/image_old/cursor.png"),
    'texture_grass_0': pygame.image.load(r"../resource/image/image_old/texture_grass/texture_grass_0.png"),
    'texture_grass_1': pygame.image.load(r"../resource/image/image_old/texture_grass/texture_grass_1.png"),
    'texture_grass_2': pygame.image.load(r"../resource/image/image_old/texture_grass/texture_grass_2.png"),
    'texture_grass_3': pygame.image.load(r"../resource/image/image_old/texture_grass/texture_grass_3.png"),
    'texture_grass_4': pygame.image.load(r"../resource/image/image_old/texture_grass/texture_grass_4.png"),
    'texture_grass_5': pygame.image.load(r"../resource/image/image_old/texture_grass/texture_grass_5.png"),
    'texture_grass_6': pygame.image.load(r"../resource/image/image_old/texture_grass/texture_grass_6.png"),
    'texture_grass_7': pygame.image.load(r"../resource/image/image_old/texture_grass/texture_grass_7.png"),
    'texture_grass_8': pygame.image.load(r"../resource/image/image_old/texture_grass/texture_grass_8.png"),
    'enemy': pygame.image.load("../resource/image/image_old/enemy.png"),
    'lightning': pygame.image.load(r"../resource/image/image_old/items/lightning.png"),
    'rune_of_heart': pygame.image.load(r"../resource/image/image_old/items/rune_of_heart.png"),
    'wooden_bow': pygame.image.load(r"../resource/image/image_old/items/wooden_bow.png"),
    'hunting_arrow': pygame.image.load(r"../resource/image/image_old/items/hunting_arrow.png"),
    'iron_bullet': pygame.image.load(r"../resource/image/image_old/items/iron_bullet.png"),
    'cigarette': pygame.image.load(r"../resource/image/image_old/items/cigarette.png"),
    'meteorite': pygame.image.load(r"../resource/image/image_old/items/meteorite.png"),
    'elderberry_stick': pygame.image.load(r"../resource/image/image_old/items/elderberry_stick.png"),
    'paddle': pygame.image.load(r"../resource/image/image_old/items/paddle.png"),
    'pae_shot': pygame.image.load(r"../resource/image/image_old/items/pae_shot.png"),
    'red_ball': pygame.image.load(r"../resource/image/image_old/items/red_ball.png"),
    'sunflower': pygame.image.load(r"../resource/image/image_old/items/sunflower.png"),
    'orange_slice': pygame.image.load(r"../resource/image/image_old/items/orange_slice.png"),
    'dagger': pygame.image.load(r"../resource/image/image_old/items/dagger.png"),
    'last_place_medal': pygame.image.load(r"../resource/image/image_old/items/last_place_medal.png"),
    'lollipop': pygame.image.load(r"../resource/image/image_old/items/lollipop.png"),
    'mini_volcano': pygame.image.load(r"../resource/image/image_old/items/mini_volcano.png"),
    'hat': pygame.image.load(r"../resource/image/image_old/items/hat.png"),
    'mini_shark': pygame.image.load(r"../resource/image/image_old/items/mini_shark.png"),
    'helmet': pygame.image.load(r"../resource/image/image_old/items/helmet.png"),
    'green_rocket': pygame.image.load(r"../resource/image/image_old/items/green_rocket.png"),
    'red_rocket': pygame.image.load(r"../resource/image/image_old/items/red_rocket.png"),
    'iron_claw': pygame.image.load(r"../resource/image/image_old/items/iron_claw.png"),
    'gun': pygame.image.load(r"../resource/image/image_old/items/gun.png"),
    'hammer': pygame.image.load(r"../resource/image/image_old/items/hammer.png"),
    'plus_one': pygame.image.load(r"../resource/image/image_old/items/plus_one.png"),
    'buckshot': pygame.image.load(r"../resource/image/image_old/items/buckshot.png"),
    'wristwatch': pygame.image.load(r"../resource/image/image_old/items/wristwatch.png"),
    'pill': pygame.image.load(r"../resource/image/image_old/items/pill.png"),
    'green_gecko': pygame.image.load(r"../resource/image/image_old/items/green_gecko.png"),
    'butterfly': pygame.image.load(r"../resource/image/image_old/items/butterfly.png"),
    'grave_shovel': pygame.image.load(r"../resource/image/image_old/items/grave_shovel.png"),
    'casino': pygame.image.load(r"../resource/image/image_old/items/casino.png"),
    'red_gecko': pygame.image.load(r"../resource/image/image_old/items/red_gecko.png"),
    'flower': pygame.image.load(r"../resource/image/image_old/items/flower.png"),
    'syringe': pygame.image.load(r"../resource/image/image_old/items/syringe.png"),
    'christmas_tree': pygame.image.load(r"../resource/image/image_old/items/christmas_tree.png"),
    'decorated_christmas_tree': pygame.image.load(r"../resource/image/image_old/items/decorated_christmas_tree.png"),
    'scope': pygame.image.load(r"../resource/image/image_old/items/scope.png"),
    'tomato': pygame.image.load(r"../resource/image/image_old/items/tomato.png"),
    'scissors': pygame.image.load(r"../resource/image/image_old/items/scissors.png"),
    'cactus': pygame.image.load(r"../resource/image/image_old/items/cactus.png"),
    'imposter': pygame.image.load(r"../resource/image/image_old/items/imposter.png"),
    'pokeball': pygame.image.load(r"../resource/image/image_old/items/pokeball.png"),
}
