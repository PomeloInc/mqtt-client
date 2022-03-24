#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TODO: DOCUMENT AND COPYRIGHT/LICENSE
"""


import logging
from pom_classes.PomeloClient import PomeloClient

# Debug
from time import sleep


def main():
    """ Main program """

    # Hello
    print("Starting Pomelo-MQTT-Client")

    # setup client & connect
    cfg = "config_default.json"
    
    print(cfg)
    try:
        pom_client = PomeloClient(cfg)
        pom_client.connect()
    except BaseException as berr:
        logging.exception(berr)

    # do stuff
    try:
        for i in range(0, 3):
            pom_client.loop(i)
            sleep(0.5)
    except BaseException as berr:
        print(berr)
        logging.exception(berr)

    sleep(2)

    # disconnect
    try:
        pom_client.disconnect()
    except BaseException as berr:
        logging.exception(berr)
    

    # end
    print("exiting..")
    return 0


if __name__ == "__main__":
    main()
