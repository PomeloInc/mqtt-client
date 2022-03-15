#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from time import sleep
import paho.mqtt.client as mqtt
import random
import os
import socket
import time

# def on_connect(client, userdata, flags, rc):
# def publish(client):
# def subscribe(client: mqtt_client):
# def on_message(client, userdata, msg):
# def on_message(client, userdata, msg):

# static stuff
broker_url = "test.mosquitto.org"
broker_port = 1883  
client_id = f'python-mqtt-{random.randint(0, 1000)}'
topic = "/pomelo/client_1"

def main():
    """ Main program """

    print("Hello World")

    # setup client
    try:
        
        client = mqtt.Client(client_id=client_id)
        client.connect(broker_url, broker_port)

        # client.publish(topic="TestingTopic", payload="TestingPayload", qos=0, retain=False)
        # print("Sucessfully connected")
    except BaseException as berr:
        print(berr)

    # do stuff
    try:
        for i in range(0, 3):
            client.publish(topic, i)
            sleep(0.5)
    except BaseException as berr:
        print(berr)

    # disconnect
    client.disconnect()

    # end
    print("exiting..")

    return 0

def on_connect(client, userdata, flags, rc):
    print("Connected with result code "+str(rc))
    client.publish(topic, "Hello from " + os.getlogin() + "@" + socket.gethostname())

def on_message(client, userdata, msg):
    print("published message")

if __name__ == "__main__":
    main()