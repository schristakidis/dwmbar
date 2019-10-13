from subprocess import getoutput

from . import BarComponent


class KBLayoutCar(BarComponent):
    interval = None

    def update_value(self):
        layout = getoutput(r'xkblayout-state print %s')
        self.value = ': {}'.format(layout)
        return self.value
