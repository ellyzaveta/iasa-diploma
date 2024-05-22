import time


class Timer:
    def __init__(self):
        self.start_time = 0

    def start(self):
        self.start_time = time.time()

    def end(self):
        return round(time.time() - self.start_time, 3)
