from picamera import PiCamera
from time import sleep

camera = PiCamera()
camera.resolution = (2592, 1944)

for i in range(3*60):
    camera.capture(f'image_{i:03d}.jpg')  # Take a picture every minute for 3 hours
    sleep(60)
    
from orbit import ISS
location = ISS.coordinates() # Equivalent to ISS.at(timescale.now()).subpoint()
print(location)

import csv
from sense_hat import SenseHat
from datetime import datetime
from pathlib import Path
from time import sleep

sense = SenseHat()

base_folder = Path(__file__).parent.resolve()
data_file = base_folder/'data.csv'

with open(data_file, 'w', buffering=1) as f:
    writer = csv.writer(f)
    header = ("Date/time", "Temperature", "Humidity")
    writer.writerow(header)
    for i in range(10):
        row = (datetime.now(), sense.temperature, sense.humidity)
        writer.writerow(row)
        sleep(60)