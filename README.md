# servermon-mqtt

This is a simple server monitoring application written in Python. A request will be made every <interval> seconds for server status and then posted to the <mqtt-topic> as json.

I developed this to assist with monitoring my home server using [Mosquitto](https://github.com/eclipse/mosquitto) and [Home Assistant](https://www.home-assistant.io/)

This reads the following details from the server it is running on:
* CPU Percentage (by core)
* Memory Percentage
* Swap Percentage
* Disk Total in bytes
* Disk Used in bytes
* Disk Free in bytes
* Disk Used percentage

An example JSON message over MQTT is
```
{'cpu_perc': [0.0, 1.0, 0.0, 1.0, 0.0, 0.0, 0.0, 1.0], 'memory_perc': 55.0, 'swap_perc': 0.0, 'disk_total': 248618848256, 'disk_used': 106703306752, 'disk_free': 129214980096, 'disk_perc': 45.2}
```

## Running locally

You can run using python3

```
> python3 monitor.py --help
usage: monitor.py [-h] [--data-path DATA_PATH] [--mqtt-host MQTT_HOST]
                  [--debug] [--disable-mqtt] [--mqtt-topic MQTT_TOPIC]
                  [--interval INTERVAL]

optional arguments:
  -h, --help            show this help message and exit
  --data-path DATA_PATH
  --mqtt-host MQTT_HOST
  --debug
  --disable-mqtt
  --mqtt-topic MQTT_TOPIC
  --interval INTERVAL
```

But you must install the dependencies
```
pip3 install --user psutil paho-mqtt argparse
```

And then run 
```
python3 monitor.py --mqtt-host 192.168.0.23 --debug --interval 3 --mqtt-topic server/monitor
```

For debugging or for local server monitoring only you can disable mqtt publishing
```
python3 monitor.py --debug --interval 3 --disable-mqtt                   
```

## Building with Docker
The Docker image adds in the dependencies for you and is my preferred option
```
docker build -t servermon-mqtt .
```

## Running with Docker
```
docker run --rm servermon-mqtt --debug --mqtt-host 192.168.0.23 --mqtt-topic server/monitor --interval 3
```
