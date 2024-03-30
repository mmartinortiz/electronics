# Example of using a BMP180 sensor (currently deprecated) with a Raspberry Pi Pico
# and CircuitPython. The BMP180 sensor is a temperature and pressure sensor that
# can be used to calculate altitude. This example will print the temperature,
# pressure, and altitude every second.
import time

import board
import busio
from bmp180 import BMP180

# Adjust to the setup of the board. When using the Pico, the I2C pins are marked as GPX
# Other boards may use board.SCL and board.SDA
i2c = busio.I2C(scl=board.GP9, sda=board.GP8)

# Lock the I2C device before we try to scan
while not i2c.try_lock():
    pass

# Print the addresses found once
print("I2C addresses found:", [hex(device_address) for device_address in i2c.scan()])

# Unlock I2C now that we're done scanning.
i2c.unlock()


bmp = BMP180(i2c)

# change this to match the location's pressure (hPa) at sea level
# https://meteologix.com/nl/observations/pressure-qnh.html
bmp.sea_level_pressure = 993

while True:
    print()
    print(f"Temperature: {bmp.temperature:2.2f}ºC")
    print(f"Pressure: {bmp.pressure:.1f} hPa")
    print(f"Altitude: {bmp.altitude:.2f} meters")

    time.sleep(1)
