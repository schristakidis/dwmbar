import os
import time
import signal
import threading


class BarComponent:
    interval = 60
    name = 'BaseComponent'

    def __init__(self, sign_no, update_func):
        self.value = ''
        self.pid = os.getpid()
        self.sign_no = sign_no
        self.update_func = update_func

        signal.signal(signal.SIGUSR1 + self.sign_no, self.handle_signal)

        thread = threading.Thread(target=self.set_interval)
        thread.start()

    def set_interval(self):
        while True:
            time.sleep(self.interval)
            os.kill(self.pid, signal.SIGUSR1 + self.sign_no)

    def handle_signal(self, sign_no, stack):
        self.update_value()
        self.update_func(self, self.value)

    def update_value(self):
        """ Must return the value """
        return self.value
