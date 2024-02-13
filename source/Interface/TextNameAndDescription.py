import pygame as pg

from source.Image.InitializationForGame import get_images_for_game
from source.Image.InitializationForItems import get_images_for_items


class TextNameAndDescription:
    font1 = pg.font.Font("resource/fonts/EightBits.ttf", 60)
    font2 = pg.font.Font("resource/fonts/EightBits.ttf", 45)

    def __init__(self, name, description, id_, enemies=False) -> None:
        super().__init__()
        self.id = id_
        self.name = name
        self.description = description
        self.enemies = enemies
        self.text_name = self.font1.render(self.name, True, (0, 0, 0))
        self.text_description = self.font2.render(self.description, True, (0, 0, 0))
        if not enemies:
            if not (self.id in get_images_for_items()):
                self.id = 'no-image'
        else:
            if not (self.id in get_images_for_game()):
                self.id = 'armor'

    def draw(self, screen, x, y):
        screen.blit(get_images_for_items()[self.id] if not self.enemies else get_images_for_game()[self.id],
                    (x - (self.text_name.get_width() // 2) - 40, y + 16))
        screen.blit(self.text_name, (x - (self.text_name.get_width() // 2), y))
        screen.blit(self.text_description,
                    (x - (self.text_description.get_width() // 2), y + self.text_name.get_height() + 5))
