#!/usr/bin/env python3
# Stove temperature watcher with thermal sensor
import os
import threading
import time
import logging

from flask import Flask, render_template
from Adafruit_AMG88xx import Adafruit_AMG88xx
from src import *

# Change directory
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

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

# Create flask server
app = Flask(__name__)

# Backgroup thread
def sensor_task():
    # Ring startup sound
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

if __name__ == "__main__":
    thread = threading.Thread(target=sensor_task)
    thread.start()

    app.run(host='0.0.0.0', port=8080)
