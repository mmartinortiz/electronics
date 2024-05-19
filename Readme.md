# Electronic projects

Multiple electronic projects with (or without) MicroControllers

## Development

For managing the different programs and libraries used for my electronic projects, I use [DevBox](https://www.jetpack.io/devbox). For [installing DevBox](https://www.jetpack.io/devbox/docs/quickstart/#install-devbox) run:

```bash
curl -fsSL https://get.jetpack.io/devbox | bash
```

Once installed, just execute `devbox shell` to get into a Shell with all the programs a libraries you need. Within this DevBox Shell, you can still use your favourite IDEs.

The following programs are available in your DevBox shell, either provided directly by `devbox` (see `devbox.json`) or `poetry` (via `pyproject.toml`):

- [Thonny](https://thonny.org/)
- [ESPTool](https://github.com/espressif/esptool)
- Python 3.11.
- [Ruff](https://www.ruff.io/), for code formatting.
- [rshell](https://github.com/dhylands/rshell), for remote execution of Python files.
- [pre-commit](https://pre-commit.com/), for making sure that committed files look nice.
- [Poetry](https://python-poetry.org/), for managing a Python Virtual environment with the project libraries.
- [Arduino IDE](https://www.arduino.cc/en/software)
- [mpremote](https://github.com/micropython/micropython-lib/tree/master/mpremote), a command line tool or uploading files to Micro Python devices
- [pipkin](https://github.com/aivarannamaa/pipkin), tool for installing distribution packages for MicroPython and CircuitPython

## How to upload a file to the Pico, and make it be run on boot

```shell
rshell cp program.py /pyboard/main.py
```

## Installing packages into ESP32 running CircuitPython

For installing libraries into the ESP32 running CircuitPython, I found easier to use [pipkin]([GitHub - aivarannamaa/pipkin: Tool for installing distribution packages for MicroPython and CircuitPython](https://github.com/aivarannamaa/pipkin)) instead of `circup`. Some examples:

```bash
pipkin --port /dev/ttyUSB0 install adafruit-circuitpython-mcp230xx
pipkin --port /dev/ttyUSB0 install adafruit-circuitpython-charlcd
```

## Connecting ESP32 to WiFi

To setup WiFi on ESP32 with CircuitPython we need to create a file called `settings.toml` in the root of the file system.

1. Use Thonny to connect to the REPL of the board

2. Use the following snippet for creating the file

```python
f = open('settings.toml', 'w')
f.write('CIRCUITPY_WIFI_SSID = "wifissid"\n')
f.write('CIRCUITPY_WIFI_PASSWORD = "wifipassword"\n')
f.write('CIRCUITPY_WEB_API_PASSWORD = "webpassword"\n')
f.close()
```

3. Restart the REPL using Thonny. Using the button will not work ¯\_(ツ)\_/¯

4. IP and MAC can be obtained using this code

```python
import wifi

print("My MAC addr: %02X:%02X:%02X:%02X:%02X:%02X" % tuple(wifi.radio.mac_address))
print("My IP address is", wifi.radio.ipv4_address)
```

More details [here](https://learn.adafruit.com/circuitpython-with-esp32-quick-start/setting-up-web-workflow).

For installing libraries, take the following precautions:

1. Close Thonny

2. Reconnect the ESP32 device (unplug, and plug again)

3. Install the libraries one by one

```bash
pipkin --port /dev/ttyUSB0 install adafruit-circuitpython-bme680
pipkin --port /dev/ttyUSB0 install adafruit-circuitpython-minimqtt
```
