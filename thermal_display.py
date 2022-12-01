import pygame
import os
import math

import numpy as np
from scipy.interpolate import griddata

from colour import Color

WIDTH = 240
HEIGHT = 240

# low range of the sensor (this will be blue on the screen)
MIN_TEMP = 26

# high range of the sensor (this will be red on the screen)
MAX_TEMP = 32

# how many color values we can have
COLOR_DEPTH = 1024


# some utility functions
def constrain(val, min_val, max_val):
    return min(max_val, max(min_val, val))


def temp_to_pixels(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) / (in_max - in_min) + out_min


class ThermalDisplay:
    lcd = None
    displayPixelWidth = WIDTH / 30
    displayPixelHeight = HEIGHT / 30
    colors = None

    points = [(math.floor(i / 8), (i % 8)) for i in range(0, 64)]
    grid_x, grid_y = np.mgrid[0:7:32j, 0:7:32j]

    def initialize(self):
        # the list of colors we can choose from
        colors = list(Color("indigo").range_to(Color("red"), COLOR_DEPTH))

        # create the array of colors
        self.colors = [(int(c.red * 255), int(c.green * 255), int(c.blue * 255)) for c in colors]

        os.putenv('SDL_FBDEV', '/dev/fb1')
        pygame.init()
        self.lcd = pygame.display.set_mode((WIDTH, HEIGHT))
        self.lcd.fill((255, 0, 0))

        pygame.display.update()
        pygame.mouse.set_visible(False)

        self.lcd.fill((0, 0, 0))
        pygame.display.update()

    def draw(self, temps):
        # temp to pixel
        pixels = [temp_to_pixels(temps, MIN_TEMP, MAX_TEMP, 0, COLOR_DEPTH - 1) for p in temps]

        # perform interpolation
        bicubic = griddata(points=self.points, values=pixels, xi=(self.grid_x, self.grid_y), method='cubic')

        for y, row in enumerate(bicubic):
            for x, pixel in enumerate(row):
                pygame.draw.rect(self.lcd, self.colors[constrain(int(pixel), 0, COLOR_DEPTH - 1)],
                                 (self.displayPixelHeight * y, self.displayPixelWidth * x,
                                  self.displayPixelHeight, self.displayPixelWidth))

        pygame.display.update()
