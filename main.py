#!/usr/bin/env python3
# Stove temperature watcher with thermal sensor
import time
import logging

from Adafruit_AMG88xx import Adafruit_AMG88xx
from thermal_display import ThermalDisplay
from stove_watcher import StoveWatcher
from alerter_sound import Alerter
#from alerter_alexa import Alerter

# initialize logging
formatter = '%(asctime)s : %(message)s'
logging.basicConfig(filename="stove_watcher.log", format=formatter, level=logging.INFO, datefmt="%Y/%m/%d %H:%M:%S")

# initialize the sensor
sensor = Adafruit_AMG88xx(address=0x68)

# initialize
display = ThermalDisplay()
alerter = Alerter()
watcher = StoveWatcher(alerter)

# let the sensor initialize
time.sleep(.1)

alerter.startup()

# main loop
while 1:
    # read temperatures
    temps = sensor.readPixels()

    # draw
    display.draw(temps)

    # watch
    watcher.watch(temps)

    time.sleep(.5)
