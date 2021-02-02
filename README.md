# Raspberry Pi thermal camera

Raspberry pi thermal camera using Adafruit_AMG88xx lib.

# Adafruit libraries
Some libraries are marked as deprecated - however it still works fine.

* AMG88xx (https://github.com/adafruit/Adafruit_AMG88xx_python)
* PureIO (https://github.com/adafruit/Adafruit_Python_PureIO)
* Bitfield (https://github.com/adafruit/Adafruit_bitfield_python)
* GPIO (https://github.com/adafruit/Adafruit_Python_GPIO)

# How to run
Clone this repo
```bash
git clone https://github.com/kotamorishi/pi-thermal-camera
```

Install some libraries.
```bash
cd pi-thermal-camera
./install.sh
```

Run
```bash
python3 thermal_cam.py
```

# Ta-da
![Image of sample](https://github.com/kotamorishi/pi-thermal-camera/blob/main/images/1.jpg?raw=true)

# Problem
The sensor read out is not adequate with range. It seems lower and lower with distance.
I hope that sensor might be able to measure the temp around 1m distance.(I am really not sure it works or not)

# Correction with ToF sensor

So I add VL53L0X to detect the renge and correct the value. It seems okay for my environment but it may not be accurate.
Thanks for ToF range sensor VL53L0X (https://github.com/hoanhan101/vl53l0x)

Run(Keyboard requires sudo)
```bash
sudo python3 thermal_cam_range.py
```

