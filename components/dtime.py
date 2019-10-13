from . import BarComponent
from datetime import datetime


class TimeCar(BarComponent):
    interval = 10

    def update_value(self):
        t = datetime.now().strftime('%a %d %b %H:%M')
        self.value = '  {} '.format(t)
        return self.value
