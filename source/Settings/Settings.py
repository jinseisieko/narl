import json

from source.Settings.ModelSettings import *


def save_settings(master_volume: list, music_volume: list, sfx_volume: list, max_fps: list, controls: dict, name):
    with DB.atomic():
        select = Settings.select().where(Settings.player == name)
        if len(select) > 2:
            select[0].delete_instance()
        Settings.create(player=name, master_volume=master_volume[0], music_volume=music_volume[0], max_fps=max_fps[0],
                        sfx_volume=sfx_volume[0],
                        controls=json.dumps(controls))


def load_settings(master_volume: list, music_volume: list, sfx_volume: list, max_fps: list, controls: dict, name):
    with DB.atomic():
        select = Settings.select().where(Settings.player == name)
        if len(select) == 0:
            return
        else:
            setting = select[-1]
            music_volume[0] = setting.music_volume
            master_volume[0] = setting.master_volume
            sfx_volume[0] = setting.sfx_volume
            max_fps[0] = setting.max_fps
            controls.clear()
            controls |= json.loads(setting.controls)
