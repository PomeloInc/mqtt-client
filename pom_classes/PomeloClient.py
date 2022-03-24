#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TODO: DOCUMENT AND COPYRIGHT/LICENSE
"""

import json
import socket
import paho.mqtt.client as mqtt
from time import sleep
import os

def read_config(path):
        '''TODO: documentation'''
        try:
            with open(path, encoding='UTF-8') as file:
                cfg_dict = json.load(file)

            config = PomeloClientConfig(
                broker=cfg_dict['broker']['url'],
                port=cfg_dict['broker']['port'],
                id=cfg_dict['client_id'],
                topics=cfg_dict['topics']
            )
            return config
        except BaseException as berr:
            return berr

# put in extra library
def on_connect(client, userdata, flags, rc):
    '''TODO: documentation'''
    print("DEBUG: Connected with result code "+str(rc))

# put in extra library
def on_publish(client, userdata, mid):
    '''TODO: documentation'''
    # print("DEBUG: Client '" + str(client.client_id) + "' published message: " + str(msg))
    print("DEBUG: Client published message: " + str(mid))

# put in extra library
def on_message(client, userdata, mid):
    '''TODO: documentation'''
    print("DEBUG: Client received message: " + str(mid.payload))

# put in extra library
def on_subscribe(client, userdata, mid, granted_qos):
    '''TODO: documentation'''
    print("DEBUG: Client subscribed to topic: ")

class PomeloClient:
    # TODO: add inheritence logic, i.e. it should be possible to create sub-classes a'la "webapp-client, build-client etcpp."
    """TODO: add documentation"""

    def __init__(self, cfg=None):
        """TODO: document"""
        try:
            self.cfg = read_config(cfg)
            self.client = mqtt.Client()
            self.topic_home = self.cfg.topics['clients']+'/'+self.cfg.id
            self.client.on_connect = on_connect
            self.client.on_publish = on_publish
            self.client.on_message = on_message
            self.client.on_subscribe = on_subscribe
        except BaseException as berr:
            return berr

    def __str__(self):
        """TODO: document"""
        return self.cfg
    
    def idle(self, i):
        """TODO: document"""
        try:
            # print("DEBUG: sent message on topic: " + self.cfg.topics['data'])
            self.client.publish(self.cfg.topics['data']+'/'+self.cfg.id, i)
            sleep(0.5)
        except BaseException as berr:
            return berr

    def register_client(self):
        """TODO: document"""
        self.client.publish(self.cfg.topics['reg'], "Hello from " + os.getlogin() + "@" + socket.gethostname())
        # TODO implement logic to send a command to another client

    def setup(self):
        """TODO: document"""
        self.client.subscribe(self.topic_home)

    def send_msg_client(self, client, msg):
        """TODO: document"""
        # print("DEBUG: sent message on topic: " + self.cfg.topics['clients']+'/'+self.cfg.id)
        self.client.publish(self.cfg.topics['clients']+'/'+client, msg)
        # TODO implement logic to send a command to another client
    
    def connect(self):
        """TODO: document"""
        try:
            self.client.connect(self.cfg.broker, self.cfg.port)
            self.setup()
            self.client.loop_start()
        except BaseException as berr:
            return berr

    def disconnect(self):
        """TODO: document"""
        try:
            self.client.disconnect()
            self.client.loop_stop()
        except BaseException as berr:
            return berr
    

class PomeloClientConfig:
    """ TODO: document """

    def __init__(self, broker, port, id, topics, client_secret=None):
        """TODO: document"""
        try:
            self.id = id
            self.broker = broker
            self.port = port
            self.topics = topics
            self.client_secret = client_secret
        except BaseException as berr:
            return berr

    def __str__(self):
        """TODO: document"""
        return self.id + self.broker
