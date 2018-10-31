# home-temperatureHumidity
DHT11 Temperature and Humidity Sensor

I bought from amazon:<br>
https://www.amazon.com/gp/product/B079NJ64RV

The board I bought is essentially a DHT11 module with a pullup resistor and a cap:<br>
https://www.mouser.com/ds/2/758/DHT11-Technical-Data-Sheet-Translated-Version-1143054.pdf

The datasheet describes the one-wire, two-way serial communication protocol.

Adafruit sells the raw DHT11 modules, and they have lots of tutorials and libraries:<br>
https://www.adafruit.com/product/386

The sensor requires a hybrid serial interfce -- you cannot use the built in serial port.
Adafruit made a nice Python library that includes a C module for the I/O:<br>
https://github.com/adafruit/Adafruit_Python_DHT

Great tutorial. It even mentions success on the Pi Zero:<br>
https://www.raspberrypi-spy.co.uk/2017/09/dht11-temperature-and-humidity-sensor-raspberry-pi/
