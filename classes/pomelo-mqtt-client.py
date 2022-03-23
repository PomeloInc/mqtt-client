#!/usr/bin/env python3
# -*- coding: utf-8 -*-

class Pomelo_Client:
    # TODO: add inheritence logic, i.e. it should be possible to create sub-classes a'la "webapp-client, build-client etcpp."

    def __init__(id=0):
        """TODO: document"""
        self.id = id

    def __str__(self):
        return self.id


    def connect():
        """TODO: document"""
        return "connected"

    def disconnect():
        """TODO: document"""
        return "disconnected"
    
    def loop():
        """TODO: document"""
        return "loop"

    