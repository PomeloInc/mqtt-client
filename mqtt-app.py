#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys
from time import sleep
import paho.mqtt.client as mqtt
import random


# def on_connect(client, userdata, flags, rc):
# def publish(client):
# def subscribe(client: mqtt_client):
# def on_message(client, userdata, msg):
# def on_message(client, userdata, msg):

def main():
    """ Main program """

   
    broker_url = "test.mosquitto.org"
    broker_port = 1883  
    client_id = f'python-mqtt-{random.randint(0, 1000)}'
    client = mqtt.Client(client_id=client_id)
    client.connect(broker_url, broker_port)
    topic = "/pomelo/client_1"
    client.publish(topic="TestingTopic", payload="TestingPayload", qos=0, retain=False)

    try:
        for i in range(0, 5):
            client.publish(topic, "Hello from BBB!")
            sleep(0.5)
    except BaseException as berr:
        print(berr)

    client.disconnect()

    return 0

if __name__ == "__main__":
    main()