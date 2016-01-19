# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 16:10:51 2016

@author: phil
"""

import socket
import os
import timeit
import logging

# Set up the logging
logging.basicConfig(
    format="%(asctime)s - %(message)s",
    level=logging.DEBUG,
)
logger = logging.getLogger(__name__)

# Parameters
host = '143.117.100.160'
port = 443
repeats = 100  # Keep this <= 100, please!
timeout = 5  # Number of seconds until giving up on connection


# Define our actual measured operation
def round_trip(skt):
    # Create a random message to test our connection
    payload = os.urandom(1024)
    
    # Network-limited part
    skt.sendall(payload)
    received_payload = skt.recv(1024)
    
    if received_payload != payload:
        raise IOError("We received an incorrect echo")

logger.info("Average time taken: {delay} ms".format(delay=average_return_time))
