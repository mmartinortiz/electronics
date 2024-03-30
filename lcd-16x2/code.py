import time

import adafruit_character_lcd.character_lcd_i2c as character_lcd
import board
import busio

# The following packages can be install in the ESP32 board using pipkin:
# pipkin --port /dev/ttyUSB0 install adafruit-circuitpython-mcp230xx
# pipkin --port /dev/ttyUSB0 install adafruit-circuitpython-charlcd
# Adjust to the setup of the board. When using the Pico, the I2C pins are marked as GPX
# Other boards may use board.SCL and board.SDA

# Adjust to the setup of the board. When using the Pico, the I2C pins are marked as GPX
# Other boards, like ESP32,  may use board.SCL and board.SDA
i2c = busio.I2C(scl=board.SCL, sda=board.SDA)

# Lock the I2C device before we try to scan
while not i2c.try_lock():
    pass

# Print the addresses found once
devices = i2c.scan()
address = 0x20
print("I2C addresses found:", [hex(device_address) for device_address in devices])
if len(devices) == 1:
    address = devices[0]

# Unlock I2C now that we're done scanning.
i2c.unlock()

cols = 16
rows = 2
lcd = character_lcd.Character_LCD_I2C(i2c, cols, rows, address=address)

# Turn backlight on
lcd.backlight = True

# Print a two line message
lcd.message = "Hello\nCircuitPython"
time.sleep(5)
lcd.clear()

# Print two line message right to left
lcd.text_direction = lcd.RIGHT_TO_LEFT
lcd.message = "Hello\nCircuitPython"
time.sleep(5)

# Return text direction to left to right, display cursor
lcd.text_direction = lcd.LEFT_TO_RIGHT
lcd.clear()
lcd.cursor = True
lcd.message = "Cursor! "
time.sleep(5)

# Display blinking cursor
lcd.clear()
lcd.blink = True
lcd.message = "Blinky Cursor!"
time.sleep(5)
lcd.blink = False
lcd.clear()

# Create message to scroll
scroll_msg = "<-- Scroll"
lcd.message = scroll_msg

# Scroll message to the left
for i in range(len(scroll_msg)):
    time.sleep(0.5)
    lcd.move_left()
lcd.clear()
lcd.message = "Going to sleep\nCya later!"
time.sleep(5)

# Turn backlight off
lcd.backlight = False
time.sleep(2)
print("Done")
