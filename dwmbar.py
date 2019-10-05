#!/usr/bin/python

import time
import subprocess

from components.volume import VolumeCar
from components.dtime import TimeCar


delimeter = ' | '


class Bar:
    def __init__(self, update_interval):
        self.cars = {
            VolumeCar(1, self.update_car): {
                'value': None,
                'pos': 1
            },
            TimeCar(0, self.update_car): {
                'value': None,
                'pos': -1
            }
        }
        self.update_interval = update_interval
        self.run()

    @property
    def sorted_cars(self):
        return sorted(
            self.cars.values(), key=lambda item: item['pos'], reverse=True
        )

    def update_car(self, car, value):
        self.cars[car]['value'] = value
        self.update_bar()

    def update_bar(self):
        status = (delimeter).join([
            c['value'] for c in self.sorted_cars
        ])
        print(status)
        print('xsetroot -name "{}"'.format(status))
        a = subprocess.getoutput('xsetroot -name "{}"'.format(status))
        print(a)
        print('DONE')

    def run(self):
        while True:
            for car, value in self.cars.items():
                value['value'] = car.update_value()

            self.update_bar()
            time.sleep(self.update_interval)


if __name__ == '__main__':
    Bar(60)
