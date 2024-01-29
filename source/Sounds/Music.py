import pygame as pg

from source.Constants import MUSIC_FOR_LEVEL


class BackgroundMusic:
    def __init__(self, wave):
        self.wave = wave
        self.music_list = []
        self.index = 0
        self.channel = pg.mixer.Channel(0)
        self.channel.set_volume(0.3)

    def update_music_list(self):
        self.music_list = [pg.mixer.Sound(f"../resource/music/{x}") for x in MUSIC_FOR_LEVEL[0]]

    def play(self):
        if not self.channel.get_busy():
            self.channel.play(self.music_list[self.index])
            self.index += 1
            self.index %= len(self.music_list)
