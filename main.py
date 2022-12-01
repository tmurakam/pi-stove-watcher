#!/usr/bin/env python
# Stove temperature watcher with thermal sensor

from Adafruit_AMG88xx import Adafruit_AMG88xx
import thermal_display
import stove_watcher as w
import alerter

# initialize the sensor
sensor = Adafruit_AMG88xx()

# initialize display
display = thermal_display.ThermalDisplay()

alerter = alerter.Alerter()
watcher = w.StoveWatcher(alerter)

# main loop
while 1:
    # read temperatures
    temps = sensor.readPixels()

    # draw
    display.draw(temps)

    # watch
    watcher.watch(temps)
