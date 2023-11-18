from time import sleep_us

from machine import PWM, Pin

power_led = Pin(25, Pin.OUT)

power_led.on()
FREQUENCY = 1000

RED = "red"
GREEN = "green"
BLUE = "blue"
COLORS = [RED, GREEN, BLUE]


class PwmLed:
    def __init__(self, red: PWM, green: PWM, blue: PWM) -> None:
        self.red = red
        self.green = green
        self.blue = blue

    def color_duty(self, color: str, duty: int):
        if color == RED:
            self.red.duty_u16(duty)
        if color == GREEN:
            self.green.duty_u16(duty)
        if color == BLUE:
            self.blue.duty_u16(duty)


LEDS = [
    PwmLed(
        red=PWM(Pin("GP2"), freq=FREQUENCY),
        green=PWM(Pin("GP3"), freq=FREQUENCY),
        blue=PWM(Pin("GP12"), freq=FREQUENCY),
    ),
    PwmLed(
        red=PWM(Pin("GP13"), freq=FREQUENCY),
        green=PWM(Pin("GP14"), freq=FREQUENCY),
        blue=PWM(Pin("GP15"), freq=FREQUENCY),
    ),
]

while True:
    for color in COLORS:
        for duty in range(65025):
            for led in LEDS:
                led.color_duty(color=color, duty=duty)
            sleep_us(100)

        for duty in range(65025, 0, -1):
            for led in LEDS:
                led.color_duty(color=color, duty=duty)
            sleep_us(100)
