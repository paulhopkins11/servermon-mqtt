import psutil
import paho.mqtt.publish as publish
import argparse
from time import sleep
import json 

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('--data-path', type=str, default='/')
    parser.add_argument('--mqtt-host', type=str)
    parser.add_argument('--debug', action='store_true', default=False)
    parser.add_argument('--mqtt-topic', type=str)
    parser.add_argument('--interval', type=int, default=10)
    args = parser.parse_args()
    while True:
        res = {}
        res['cpu_perc'] = psutil.cpu_percent(interval=1, percpu=True)
        res['memory_perc'] = psutil.virtual_memory().percent
        res['swap_perc'] = psutil.swap_memory().percent
        du = psutil.disk_usage(args.data_path)
        res['disk_total'] = du.total
        res['disk_used'] = du.used
        res['disk_free'] = du.free
        res['disk_perc'] = du.percent
        if args.debug:
            print(f'pub -> {args.mqtt_host} {args.mqtt_topic} {res}', flush=True)

        publish.single(args.mqtt_topic, json.dumps(res), hostname=args.mqtt_host)
        sleep(args.interval)

if __name__ == "__main__":
    main()