import cv2
import pygame as pg

from source.Constants import *


class Video:
    def __init__(self, name) -> None:
        super().__init__()
        self.name = name
        self.video = cv2.VideoCapture(name)
        self.success, self.video_image = self.video.read()
        self.fps = self.video.get(cv2.CAP_PROP_FPS)
        self.active = True

        success, video_image = self.video.read()
        self.video_surf = pg.image.frombuffer(
            video_image.tobytes(),
            video_image.shape[1::-1],
            "BGR"
        )

    def update(self, screen):
        success, video_image = self.video.read()
        if success:
            self.video_surf = pg.transform.scale(pg.image.frombuffer(
                video_image.tobytes(),
                video_image.shape[1::-1],
                "BGR"
            ), [WIDTH, HEIGHT])
        else:
            self.active = False

        screen.blit(self.video_surf, (0, 0))

    def repeat(self):
        self.video = cv2.VideoCapture(self.name)
        self.success, self.video_image = self.video.read()
        self.fps = self.video.get(cv2.CAP_PROP_FPS)
        self.active = True

        success, video_image = self.video.read()
        self.video_surf = pg.image.frombuffer(
            video_image.tobytes(),
            video_image.shape[1::-1],
            "BGR"
        )
