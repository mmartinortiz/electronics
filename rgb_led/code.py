import time
import microcontroller
from rainbowio import colorwheel
import adafruit_rgbled


# Create the RGB LED objects
LEDS = [
    adafruit_rgbled.RGBLED(
        microcontroller.pin.GPIO2, microcontroller.pin.GPIO3, microcontroller.pin.GPIO12
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
