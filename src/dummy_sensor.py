import random

class DummySensor:
    def __init__(self):
        self._pixels = [[0 for _ in range(8)] for _ in range(8)]

    @property
    def pixels(self):
        self._pixels = [[random.randint(10, 70) for _ in range(8)] for _ in range(8)]
        return self._pixels
