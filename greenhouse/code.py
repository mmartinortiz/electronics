import json
import os
import ssl
import time

import adafruit_bme680
import adafruit_logging as logging
import adafruit_minimqtt.adafruit_minimqtt as MQTT
import alarm
import board
import busio
import socketpool
import wifi

# Measure every 5 minutes
PUBLISH_DELAY = 60 * 5
MQTT_TOPIC = "greenhouse/sensor"

# Enable verbosity on logs, only for local debugging
DEBUG = False

# Connect to the Sensor
# ESP32 uses a different syntac
# i2c = board.I2C()
i2c = busio.I2C(scl=board.GP9, sda=board.GP8)
sensor = adafruit_bme680.Adafruit_BME680_I2C(i2c)

wifi.radio.connect(
    os.getenv("CIRCUITPY_WIFI_SSID"),
    os.getenv("CIRCUITPY_WIFI_PASSWORD"),
)
print(f"Connected to {os.getenv('CIRCUITPY_WIFI_SSID')}")
print(f"My IP address: {wifi.radio.ipv4_address}")

# Create a socket pool
pool = socketpool.SocketPool(wifi.radio)

# Set up a MiniMQTT Client
mqtt_client = MQTT.MQTT(
    broker=os.getenv("MQTT_BROKER"),
    port=os.getenv("MQTT_PORT"),
    username=os.getenv("MQTT_USERNAME"),
    password=os.getenv("MQTT_PASSWORD"),
    socket_pool=pool,
    ssl_context=ssl.create_default_context(),
)

if DEBUG:
    logger = logging.getLogger()
    logger.setLevel(logging.DEBUG)
    mqtt_client.logger = logger

while not mqtt_client.is_connected():
    print(f"Attempting to connect to {mqtt_client.broker}")
    try:
        mqtt_client.connect()
    except Exception as exception:
        # In case of exception, go to sleep again
        print(exception)
        pause = alarm.time.TimeAlarm(monotonic_time=time.monotonic() + PUBLISH_DELAY)
        alarm.exit_and_deep_sleep_until_alarms(pause)

# Discard the first read, in my tests it is always a faulty measure
output = {
    "temperature": sensor.temperature,
    "humidity": sensor.humidity,
    "pressure": sensor.pressure,
    "gas": sensor.gas,
}

# Give a few seconds to the sensor to update
time.sleep(2)

output = {
    "temperature": sensor.temperature,
    "humidity": sensor.humidity,
    "pressure": sensor.pressure,
    "gas": sensor.gas,
}

print(f"Publishing to topic {MQTT_TOPIC}")
print(output)

# Publish the measurement
mqtt_client.publish(MQTT_TOPIC, json.dumps(output))

mqtt_client.disconnect()

# Go to sleep, once awaked, the whole code.py file will be run again
pause = alarm.time.TimeAlarm(monotonic_time=time.monotonic() + PUBLISH_DELAY)
alarm.exit_and_deep_sleep_until_alarms(pause)
