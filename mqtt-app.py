#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TODO: DOCUMENT AND COPYRIGHT/LICENSE
"""


import logging
from pom_classes.PomeloClient import PomeloClient
from pom_classes.PomeloFlashClient import PomeloFlashClient

# Debug
from time import sleep


def main():
    """ Main program """

    # Hello
    print("Starting Pomelo-MQTT-Client")

    # setup client & connect
    base_cfg = "template_config_base.json"
    flash_cfg = 'template_config_flash.json'
    try:
        # test base client
        pom_client = PomeloClient(base_cfg)
        pom_client.connect()
        # test flash client
        flash_client = PomeloFlashClient(flash_cfg)
        flash_client.connect()
    except BaseException as berr:
        logging.exception(berr)

    # registration
    try:
        # test base client
        pom_client.register_client()
        # test flash client
        flash_client.register_client()
    except BaseException as berr:
        logging.exception(berr)

    # test functionality
    try:
        # base client
        pom_client.idle("test_data")
        pom_client.send_msg_client('build_server', 'perform_task')

        # flash client
        flash_client.flash_target("bbb_v0")
        
    except BaseException as berr:
        print(berr)
        logging.exception(berr)

    sleep(10)

    # disconnect
    try:
        pom_client.disconnect()
        flash_client.disconnect()
    except BaseException as berr:
        logging.exception(berr)
    

    # end
    print("exiting..")
    return 0


if __name__ == "__main__":
    main()
