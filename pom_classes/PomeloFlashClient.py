#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
TODO: DOCUMENT AND COPYRIGHT/LICENSE
"""

from pom_classes.PomeloClient import PomeloClient

# TODO: replace development config with real logic
flash_cfg = 'template_config_flash.json'

class PomeloFlashClient(PomeloClient):
    """TODO: Document"""

    def __init__(self, cfg=flash_cfg):
        super().__init__(cfg)

    # def setup(self):
    #     """TODO: Document"""
    #     print("DEBUG: Setting up FlashClient")

    def flash_target(self, target):
        """TODO: Document"""
        self.send_msg_client(self.cfg.id, 'flash ' + target)
        
        # TODO: implement
        # # get_image
        # # get_bootloader
        # # get_SPL
        # # get_IPL
        # # get_kernel
        # # call_flashing_scripts
