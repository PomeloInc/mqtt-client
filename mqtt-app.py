#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from time import sleep
import paho.mqtt.client as mqtt
import random
import os
import socket
import logging
import time

# static stuff
broker_url = "test.mosquitto.org"
broker_port = 1883  
client_id = f'python-mqtt-{random.randint(0, 1000)}'
topic = "/pomelo/client_1"

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.publish(topic, "Hello from " + os.getlogin() + "@" + socket.gethostname())

def on_publish(client, userdata, msg):
    print("published message")

def main():
    """ Main program """

    print("Hello World")

    # setup client
    try:
        
        client = mqtt.Client(client_id=client_id)
        client.on_connect = on_connect
        client.on_publish = on_publish
    except BaseException as berr:
        print(berr)

    # connect
    try:
        client.connect(broker_url, broker_port)
        client.loop_start()
    except BaseException as berr:
        print(berr)

    # do stuff
    try:
        for i in range(0, 3):
            client.publish(topic, i)
            sleep(0.5)
    except BaseException as berr:
        print(berr)

    sleep(2)

    # disconnect
    client.disconnect()
    client.loop_stop()

    # end
    print("exiting..")
    return 0


if __name__ == "__main__":
    main()