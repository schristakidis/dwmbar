import subprocess

from . import BarComponent


class VolumeCar(BarComponent):
    interval = 60

    def update_value(self):
        mute = subprocess.getoutput('pulsemixer --get-mute')
        if str(mute) == '1':
            self.value = "🔇"
            return self.value

        vol = subprocess.getoutput('pulsemixer --get-volume').split()[0]

        try:
            vol = int(vol)
        except Exception:
            return self.value

        if vol > 70:
            icon = "🔊"
        elif vol < 30:
            icon = "🔈"
        else:
            icon = "🔉"

        self.value = '{} {}'.format(icon, vol)
        return self.value
