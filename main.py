#!/usr/bin/env python3
# Stove temperature watcher with thermal sensor

from Adafruit_AMG88xx import Adafruit_AMG88xx
from thermal_display import ThermalDisplay
from stove_watcher import StoveWatcher
from alerter import Alerter

# initialize the sensor
sensor = Adafruit_AMG88xx()

# initialize
display = ThermalDisplay()
alerter = Alerter()
watcher = StoveWatcher(alerter)

# main loop
while 1:
    # read temperatures
    temps = sensor.readPixels()

    # draw
    display.draw(temps)

    # watch
    watcher.watch(temps)
