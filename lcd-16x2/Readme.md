# LCD Display 16x2

Demo code for displaying some text in an LCD 16x2 display over I2C using **CircuitPython**. For installing the required libraries [pipkin](https://github.com/pipkin-package) can be used. `pipkin` is available via the `poetry` virtual environment.

**CircuitPython** needs to be flashed from the command line. The `.bin` file I used for my boards is the one for [DOIT ESP32 Development Board]([DOIT ESP32 Development Board Download](https://circuitpython.org/board/doit_esp32_devkit_v1/))

```bash
# 1. Erase the flash
esptool.py --chip esp32 --port /dev/ttyUSB0 erase_flash

# 2. Flash with CircuitPython
esptool.py --chip esp32 --port /dev/ttyUSB0 write_flash -z 0x0 <path-to-bin-file>
```

Install packages like:

```bash
pipkin --port /dev/ttyUSB0 install adafruit-circuitpython-mcp230xx
pipkin --port /dev/ttyUSB0 install adafruit-circuitpython-charlcd
```
