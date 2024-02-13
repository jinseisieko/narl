from source.Interface.TextNameAndDescription import TextNameAndDescription
from source.Settings.SettingsData import *


class TextNameAndDescriptionC(TextNameAndDescription):
    def update(self, mouse_pos, x, y):
        if len(np.where(np.abs(mouse_pos - np.array(
                (x, y + self.text_name.get_height() + 5 + self.text_description.get_height()))) <= np.array(
            (self.text_description.get_width(), self.text_name.get_height() + 5 + self.text_description.get_height())))[
                   0]) == 2:
            sn1 = pg.mixer.Sound("resource/music/click3.mp3")
            sn1.set_volume(0.2 * SFX_VOLUME[0] * MASTER_VOLUME[0])
            sn1.play()

            return 1
        return 0
