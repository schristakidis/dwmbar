#!/usr/bin/python

"""DWM Bar

Usage:
  dwmbar.py run [--interval=<int>]
  dwmbar.py update <module>
  dwmbar.py (-h | --help)

Options:
  --interval=<int>    the update interval in seconds [default: 60]
  -h --help     Show this screen.
"""

import os
import time
import subprocess
from appdirs import user_cache_dir
import signal
import logging

from docopt import docopt
from components.volume import VolumeCar
from components.dtime import TimeCar

logger = logging.getLogger('spam_application')
logger.setLevel(logging.DEBUG)
fh = logging.FileHandler('/tmp/dwmbar.log')
fh.setLevel(logging.DEBUG)
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
fh.setFormatter(formatter)
logger.addHandler(fh)

delimeter = '  |  '


MODULES = {
    'volume': {
        'module': VolumeCar,
        'sign_no': 1,
        'pos': 1
    },
    'time': {
        'module': TimeCar,
        'sign_no': 0,
        'pos': -1
    }
}


class Bar:
    def __init__(self, update_interval):
        logger.info('RUNNING')
        self.cars = {}
        for module in MODULES.values():
            self.cars[module['module'](module['sign_no'], self.update_car)] = {
                'value': None,
                'pos': module['pos']
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
        status = 'echo -e "{}"'.format(status)
        subprocess.getoutput('xsetroot -name "$({})"'.format(status))

    def run(self):
        while True:
            for car, value in self.cars.items():
                value['value'] = car.update_value()

            self.update_bar()
            time.sleep(self.update_interval)


def get_pid_path():
    return os.path.join(user_cache_dir(), 'dwm_bar_id')


def update_module(pid, module):
    module = MODULES.get(module, None)
    if not module:
        return

    try:
        os.kill(pid, signal.SIGUSR1 + module['sign_no'])
    except Exception:
        pass


if __name__ == '__main__':
    try:
        arguments = docopt(__doc__)
        pid_path = get_pid_path()
        logger.info(f'pid path is {pid_path}')
        if arguments['run']:
            try:
                with open(pid_path, 'w') as f:
                    f.write(str(os.getpid()))
            except Exception:
                pass
            Bar(int(arguments['--interval']))
        else:
            with open(pid_path) as f:
                pid = int(f.read())
            update_module(pid, arguments['<module>'])
    except Exception:
        logging.exception('FAILED TO STARTED')
