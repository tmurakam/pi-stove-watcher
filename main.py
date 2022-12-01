#!/usr/bin/env python
# Stove temperature watcher with thermal sensor

from Adafruit_AMG88xx import Adafruit_AMG88xx
import thermal_display

# initialize the sensor
sensor = Adafruit_AMG88xx()

# initialize display
display = thermal_display.ThermalDisplay()

# main loop
while 1:
    # read the pixels
    pixels = sensor.readPixels()

    # draw
    display.draw(pixels)
