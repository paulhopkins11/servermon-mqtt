# servermon-mqtt

This is a simple server monitoring application written in Python. A request will be made every <interval> seconds for server status and then posted to the <mqtt-topic> as json.

I developed this to assist with monitoring my home server using [Mosquitto](https://github.com/eclipse/mosquitto) and [Home Assistant](https://www.home-assistant.io/)

## Running locally

You can run using python3

```
> python3 monitor.py --help
usage: monitor.py [-h] [--data-path DATA_PATH] [--mqtt-host MQTT_HOST]
                  [--debug] [--mqtt-topic MQTT_TOPIC] [--interval INTERVAL]

optional arguments:
  -h, --help            show this help message and exit
  --data-path DATA_PATH
  --mqtt-host MQTT_HOST
  --debug
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

## Building with Docker
The Docker image adds in the dependencies for you and is my preferred option
```
docker build -t servermon-mqtt .
```

## Running with Docker
```
docker run --rm servermon-mqtt --debug --mqtt-host 192.168.0.23 --mqtt-topic server/monitor --interval 3
```
