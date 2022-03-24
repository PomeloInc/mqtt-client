#!/usr/bin/env python3
# -*- coding: utf-8 -*-

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

            config = PomeloClient.Config(
                broker=cfg_dict['broker']['url'],
                port=cfg_dict['broker']['port'],
                id=cfg_dict['client_id'],
                topics=cfg_dict['topics']
            )
            return config
        except BaseException as berr:
            return berr


class PomeloClient:
    # TODO: add inheritence logic, i.e. it should be possible to create sub-classes a'la "webapp-client, build-client etcpp."
    """TODO: add documentation"""

    def __init__(self, cfg=None):
        """TODO: document"""
        try:
            self.id = id
            self.cfg = read_config(cfg)
            self.client = mqtt.Client()
            self.client.on_connect = self.on_connect
            self.client.on_publish = self.on_publish
        except BaseException as berr:
            return berr

    def __str__(self):
        """TODO: document"""
        return self.id

    def register(self):
        """TODO: document"""
        self.client.publish(self.cfg.topics['reg'], "Hello from " + os.getlogin() + "@" + socket.gethostname())
        # TODO implement logic to send a command to another client

    def send_command(self, client, cmd):
        """TODO: document"""
        self.client.publish("pomelo/", "Hello from " + os.getlogin() + "@" + socket.gethostname())
        # TODO implement logic to send a command to another client

    def receive_command(self):
        """TODO: document"""
        # TODO: implement logic to receive a command
        
    def work_task(self):
        """TODO: document"""
        # TODO: perform task

    # debug
    def on_connect(client, userdata, flags, rc):
        '''TODO: documentation'''
        print("DEBUG: Connected with result code "+str(rc))

    # debug
    def on_publish(client, userdata, msg):
        '''TODO: documentation'''
        print("DEBUG: published message: " + msg)

    def on_message(client, userdata, msg):
        '''TODO: documentation'''
        print("DEBUG: published message: " + msg)
    
    def connect(self):
        """TODO: document"""
        try:
            self.client.connect(self.cfg.broker, self.cfg.port)
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
    
    def idle(self, i):
        """TODO: document"""
        try:
            print(self.cfg.topics['data'])
            self.client.publish(self.cfg.topics['data'], i + 'Idle')
            sleep(0.5)
        except BaseException as berr:
            return berr

    class Config:
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
