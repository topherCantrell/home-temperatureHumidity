"""
  - Add this line to /etc/rc.local (before the exit 0):
  -   /home/pi/ONBOOT.sh 2> /home/pi/ONBOOT.errors > /home/pi/ONBOOT.stdout &
  - Add the following ONBOOT.sh script to /home/pi and make it executable:
  
#!/bin/bash
cd /home/pi/home-dungeonHumidity
python3 app_monitor.py  
"""

import time
import ez_post


import Adafruit_DHT


def read_humidity_temperature():
    # Note that sometimes you won't get a reading and
    # the results will be null (because Linux can't
    # guarantee the timing of calls to read the sensor).
    # If this happens try again! (we'll try 4 times)
    for i in range(4):
        humidity, temperature = Adafruit_DHT.read_retry(11, 4)
        if humidity is not None and temperature is not None:
            break
    temperature = temperature * 9/5.0 + 32
    return {
        'humidity' : humidity,
        'temperature' : temperature
        }

while True:
    
    readings = read_humidity_temperature()   
     
    try:
        ez_post.post_to_home_gateway('dungeonHumidity',readings)
    except OSError:
        pass # Ignore connection error in case the server is down temporarily
    
    time.sleep(60)
           
    