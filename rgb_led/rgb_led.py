from machine import Pin, PWM
from time import sleep_us

led = Pin(25, Pin.OUT)

led.on()
frequency = 1000

red = PWM(Pin("GP2"), freq=frequency)
green = PWM(Pin("GP3"), freq=frequency)
blue = PWM(Pin("GP12"), freq=frequency)

while True:
    for color in [red, green, blue]:
        for duty in range(65025):
            color.duty_u16(duty)
            sleep_us(100)

        for duty in range(65025, 0, -1):
            color.duty_u16(duty)
            sleep_us(100)
