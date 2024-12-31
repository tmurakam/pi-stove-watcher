#!/usr/bin/env python3
# Stove temperature watcher with thermal sensor
import threading
import logging
import itertools

from flask import Flask, render_template, send_file
from src import *

# Change directory
script_dir = os.path.dirname(os.path.abspath(__file__))
os.chdir(script_dir)

# initialize logging
formatter = '%(asctime)s : %(message)s'
logging.basicConfig(filename="stove_watcher.log", format=formatter, level=logging.INFO, datefmt="%Y/%m/%d %H:%M:%S")

sensor = None

if os.environ.get("EMULATE_SENSOR") == "1":
    sensor = DummySensor()

else:
    import busio
    import adafruit_amg88xx
    import board

    # initialize the sensor
    i2c_bus = busio.I2C(board.SCL, board.SDA)
    sensor = adafruit_amg88xx.AMG88XX(i2c_bus, addr=0x68)

# initialize
display = ThermalDisplay()
alerter = Alerter()
watcher = StoveWatcher(alerter)

# shared variables
bicubic = []
max_temp = 0

# Background thread
def sensor_task():
    global bicubic, max_temp

    # let the sensor initialize
    time.sleep(.1)

    # Ring startup sound
    #alerter.startup()

    # main loop
    while 1:
        # read temperatures (8x8 array)
        temps2d = sensor.pixels

        # flatten
        temps = list(itertools.chain.from_iterable(temps2d))

        # draw
        bicubic = display.draw(temps)

        # watch
        max_temp = watcher.watch(temps)

        time.sleep(.5)

# Create flask server
app = Flask(__name__)

# API
@app.route('/', methods=['GET'])
def get():
    return render_template('index.html', temp=max_temp)

@app.route('/thermal-image')
def serve_image():
    return send_file('/tmp/thermal.png', mimetype='image/png')

def run_flask():
    app.run(host='0.0.0.0', port=8080)

if __name__ == "__main__":
    # Run flask in background thread
    thread = threading.Thread(target=run_flask, daemon=True)
    thread.start()

    sensor_task()
