FROM python:slim

RUN ["pip3", "install", "--user", "psutil", "paho-mqtt", "argparse"]

ADD *.py /
ENTRYPOINT ["python3", "monitor.py"]
