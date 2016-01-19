# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 16:10:51 2016

@author: phil
"""

import threading
import logging

# Set up the logging
logging.basicConfig(
    format="%(asctime)s - %(message)s",
    level=logging.DEBUG,
)
logger = logging.getLogger(__name__)

thread_count = 10  # Keep this <= 10, please!


# Our in-thread routine
def run():
    pass
    
# THREADING CONTROL CODE HERE
    
logging.info("COMPLETE")