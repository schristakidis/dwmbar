from subprocess import getoutput

from . import BarComponent
from .colors import print_inactive, print_notice


class SpotifyCar(BarComponent):
    interval = 5

    def update_value(self):
        player = 'playerctl --player=spotify'

        try:
            artist = getoutput('{} metadata artist'.format(player))
            title = getoutput('{} metadata title'.format(player))
            status = getoutput('{} status'.format(player))
        except Exception:
            return

        if status == 'Paused':
            color_func = print_inactive
        else:
            color_func = print_notice

        if title != 'No players found':
            self.value = color_func(f'{artist} - {title}')
        else:
            self.value = ''

        return self.value
