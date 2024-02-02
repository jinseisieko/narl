from source.Constants import MUSIC_FOR_LEVEL
from source.Settings.SettingsData import *


class BackgroundMusic:
    def __init__(self, wave):
        self.wave = wave
        self.music_list = []
        self.index = 0
        self.channel = pg.mixer.Channel(0)

    def update_music_list(self):
        self.music_list = [pg.mixer.Sound(f"resource/music/{x}") for x in MUSIC_FOR_LEVEL[0]]

    def play(self):
        if not self.channel.get_busy():
            self.channel.play(self.music_list[self.index])
            self.index += 1
            self.index %= len(self.music_list)

    def update(self):
        self.channel.set_volume(0.3 * MUSIC_VOLUME * MASTER_VOLUME)


class SoundEffect:
    def __init__(self):
        self.player_volume_coefficient = 0.3
        self.enemy_volume_coefficient = 0.2
        self.new_wave_volume_coefficient = 1
        self.new_level_volume_coefficient = 1
        self.update()

    def update(self):
        self.player_volume = self.player_volume_coefficient * SFX_VOLUME * MASTER_VOLUME
        self.enemy_volume = self.enemy_volume_coefficient * SFX_VOLUME * MASTER_VOLUME
        self.new_wave_volume = self.new_wave_volume_coefficient * SFX_VOLUME * MASTER_VOLUME
        self.new_level_volume = self.new_level_volume_coefficient * SFX_VOLUME * MASTER_VOLUME

    def player_damage(self):
        sn = pg.mixer.Sound("resource/music/player_damage.mp3")
        sn.set_volume(self.player_volume)
        sn.play()

    def kill_enemy(self):
        sn = pg.mixer.Sound("resource/music/enemy_damage2.mp3")
        sn.set_volume(self.enemy_volume)
        sn.play()

    def new_wave(self):
        sn = pg.mixer.Sound("resource/music/new_wave.mp3")
        sn.set_volume(self.new_wave_volume)
        sn.play()

    def new_level(self):
        sn = pg.mixer.Sound("resource/music/castle_levelup.mp3")
        sn.set_volume(self.new_level_volume)
        sn.play()
