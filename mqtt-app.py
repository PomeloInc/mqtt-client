#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import os
import socket
import logging
# import time
# import sys
# import random
import json

from time import sleep
import paho.mqtt.client as mqtt


def on_connect(client, userdata, flags, rc):
    '''TODO: documentation'''
    print("Connected with result code "+str(rc))
    client.publish(client.topic_reg, "Hello from " + os.getlogin() + "@" + socket.gethostname())

def on_publish(client, userdata, msg):
    '''TODO: documentation'''
    print("DEBUG: published message")

def read_config(path):
    '''TODO: documentation'''
    with open(path, encoding='UTF-8') as file:
        cfg = json.load(file)
    return cfg

def main():
    """ Main program """

    print("Starting Pomelo-MQTT-Client")
    print("Hello Bitbake")
    # setup client
    cfg = read_config("config_default.json")
    topic_reg = cfg['topic_general'] + '/' + cfg['topic_reg']
    topic_data = cfg['topic_general'] + '/' + cfg['topic_data']

    print(cfg)
    try:
        client = mqtt.Client(client_id=cfg['client_id'])
        client.topic_reg = topic_reg
        client.on_connect = on_connect
        client.on_publish = on_publish
    except BaseException as berr:
        print(berr)
        logging.exception(berr)

    # connect
    try:
        client.connect(cfg['broker_url'], cfg['broker_port'])
        client.loop_start()
    except BaseException as berr:
        print(berr)
        logging.exception(berr)

    # do stuff
    try:
        for i in range(0, 3):
            client.publish(topic_data, i)
            sleep(0.5)
    except BaseException as berr:
        print(berr)
        logging.exception(berr)

    sleep(2)

    # disconnect
    try:
        client.disconnect()
        client.loop_stop()
    except BaseException as berr:
        print(berr)
        logging.exception(berr)

    # end
    print("exiting..")
    return 0


if __name__ == "__main__":
    main()
