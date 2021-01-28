'''
This script allows you to put focus on a specific browser tab.
Useful for verification of links that open in a new browser tab by default.
Replace <your tab title> below.
'''
#!/usr/bin/python
#-*- coding: utf-8 -*-

import logging
import time

log = logging.getLogger(__name__)

def run(context):
    driver = context.get_driver()
    driver.switch_to_window_by_title("DS-11 Application for a U.S. Passport ")
    context.get_all_elements()
