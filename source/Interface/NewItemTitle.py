import pygame.font

from source.Image.InitializationForItems import get_images_for_items
from source.Interface.Buttons import *


class NewItemTitle:
    def __init__(self, screen, last_frame, game):
        self.last_frame = last_frame
        self.screen = screen
        self.background = pg.Surface((WIDTH, HEIGHT))
        self.background.blit(self.last_frame, (0, 0))

        self.buttons = {}

        self.font2 = pygame.font.Font('resource/fonts/EightBits.ttf', 90)

        self.text2 = self.font2.render("Add Item", True, "#7452ff")
        self.text_rect2 = self.text2.get_rect()
        self.text_rect2.center = np.array([WIDTH / 2, HEIGHT / 2 - 120])

        random_item1, self.rank1 = game.player.characteristics.getitem.get_rank_random(r1=10, r2=5,  r3=5)
        random_item2, self.rank2 = game.player.characteristics.getitem.get_rank_random(r1=10, r2=5,  r3=5)
        random_item3, self.rank3 = game.player.characteristics.getitem.get_rank_random(r1=10, r2=5, r3=5)

        self.random_item1 = random_item1
        self.random_item2 = random_item2
        self.random_item3 = random_item3

        if not (random_item1 in get_images_for_items()):
            random_item1 = 'no-image'
        if not (random_item2 in get_images_for_items()):
            random_item2 = 'no-image'
        if not (random_item3 in get_images_for_items()):
            random_item3 = 'no-image'

        self.buttons["ItemButton1"] = ItemButton(np.array([WIDTH / 2 - 130, HEIGHT / 2]), np.array([50, 50]),
                                                 get_images_for_items()[random_item1])
        self.buttons["ItemButton2"] = ItemButton(np.array([WIDTH / 2, HEIGHT / 2]), np.array([50, 50]),
                                                 get_images_for_items()[random_item2])
        self.buttons["ItemButton3"] = ItemButton(np.array([WIDTH / 2 + 130, HEIGHT / 2]), np.array([50, 50]),
                                                 get_images_for_items()[random_item3])

    def draw(self):
        self.screen.blit(self.background, (0, 0))
        self.screen.blit(self.text2, self.text_rect2)
        self.draw_buttons(self.screen)

    def update(self):
        ...

    def draw_buttons(self, screen):
        for x in self.buttons.values():
            x.draw(screen)
