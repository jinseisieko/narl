from source.Settings.SettingsData import *


class SettingsContainer:

    def __init__(self) -> None:
        super().__init__()
        self.text_input_master_volume = MASTER_VOLUME[0]
        self.text_input_music_volume = MUSIC_VOLUME[0]
        self.text_input_sfx_volume = SFX_VOLUME[0]
        self.text_input_max_fps = MAX_FPS[0]
