#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import json
import paho.mqtt.client as mqtt

class PomeloClient:
    # TODO: add inheritence logic, i.e. it should be possible to create sub-classes a'la "webapp-client, build-client etcpp."

    def __init__(self, id=0, cfg=None):
        """TODO: document"""
        try:
            self.id = id
            self.cfg = PomeloClient.Config(self.read_config(cfg))
            self.client = mqtt.Client()
        except BaseException as berr:
            return berr

    def __str__(self):
        """TODO: document"""
        return self.id
        
    def read_config(path):
        '''TODO: documentation'''
        try:
            with open(path, encoding='UTF-8') as file:
                cfg_dict = json.load(file)

            config = PomeloClient.Config(
                id=cfg_dict['client_id'],
                port=cfg_dict['broker']['port'],
                broker_address=cfg_dict['broker']['url'],
                topics=cfg_dict['topics']
            )
            return config
        except BaseException as berr:
            return berr
    
    def connect(self):
        """TODO: document"""
        try:
            self.client.connect(self.cfg.boker, self.cfg.port)
            self.client.loop_start()
        except BaseException as berr:
            return berr

    def disconnect():
        """TODO: document"""
        return "disconnected"
    
    def loop():
        """TODO: document"""
        return "loop"

    class Config:
        # TODO:
        def __init__(self, broker, port, client_id, topics, client_secret=None):
            """TODO: document"""
            try:
                self.id = client_id
                self.boker = broker
                self.port = port
                self.topics = topics
                self.client_secret = client_secret
            except BaseException as berr:
                return berr

        def __str__(self):
            """TODO: document"""
            return self.id + self.broker_addr
