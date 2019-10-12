from . import BarComponent
from datetime import datetime


class TimeCar(BarComponent):
    interval = 10

    def update_value(self):
        t = datetime.now().strftime('%a %d %b %H:%M')
        self.value = '  \x04 {} \x01'.format(t)
        return self.value
