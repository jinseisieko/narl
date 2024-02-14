import pygame as pg


class Image:
    def __init__(self, w: int, h: int, image) -> None:
        super().__init__()
        self.width: int = w
        self.height: int = h
        self.default_img = image
        self.img = self.init_img()

    def init_img(self):
        return pg.transform.scale(self.default_img.convert(), (self.width * 2, self.height * 2))

    def resize(self, w: int, h: int):
        if w == self.width and h == self.height:
            return
        self.width = w
        self.height = h
        self.img = self.init_img()
