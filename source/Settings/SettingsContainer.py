from source.Settings.Settings import save_settings
from source.Settings.SettingsData import *


class SettingsContainer:

    def __init__(self) -> None:
        super().__init__()
        self.text_input_master_volume: str = str(MASTER_VOLUME[0])
        self.text_input_music_volume: str = str(MUSIC_VOLUME[0])
        self.text_input_sfx_volume: str = str(SFX_VOLUME[0])
        self.text_input_max_fps: str = str(MAX_FPS[0])

    def update_settings(self):
        update(self.text_input_master_volume, self.text_input_music_volume, self.text_input_sfx_volume,
               self.text_input_max_fps)
        save_settings(MASTER_VOLUME, MUSIC_VOLUME, SFX_VOLUME, MAX_FPS, CONTROLS)
