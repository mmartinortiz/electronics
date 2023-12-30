import time

import adafruit_rgbled
import microcontroller
from rainbowio import colorwheel

# Create the RGB LED objects
LEDS = [
    adafruit_rgbled.RGBLED(
        microcontroller.pin.GPIO8,
        microcontroller.pin.GPIO7,
        microcontroller.pin.GPIO6,
    ),
    adafruit_rgbled.RGBLED(
        microcontroller.pin.GPIO13,
        microcontroller.pin.GPIO14,
        microcontroller.pin.GPIO15,
    ),
]


while True:
    for i in range(255):
        i = (i + 1) % 256
        for led in LEDS:
            led.color = colorwheel(i)
        time.sleep(0.1)
