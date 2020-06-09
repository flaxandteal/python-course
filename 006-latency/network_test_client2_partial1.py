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
    # Get the current thread    
    currentThread = threading.currentThread()
    
    # Send out a message
    logging.info("Hi, my name is {name}".format(
        name=currentThread.getName()
    ))
    
# Threads are given identifiers as integers 1-N
# This is easier to handle in numpy
threads = [threading.Thread(target=run) for i in range(thread_count)]

# The items method turns a module into pairs (tuples) of key and value
for thread in threads:
    thread.start()

# Wait for all threads to complete
for thread in threads:
    thread.join()

logging.info("COMPLETE")
