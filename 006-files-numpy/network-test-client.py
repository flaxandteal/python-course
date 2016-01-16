# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 16:10:51 2016

@author: phil
"""

import socket
import os
import timeit
import logging

# Parameters
host = 'flaxandteal.co.uk'
port = 9998

# Set up the logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Create a random message to test our connection
payload = os.urandom(1024)

# This tool measures time to call a function - it has built-in args for
# repetition and other handy features
timer = timeit.Timer()

# Define our actual measured operation
def round_trip(skt):
    skt.sendall(payload)
    received_payload = skt.recv(1024)
    
    if received_payload != payload:
        raise RuntimeError("We received an incorrect echo")

# Use a `with` context to make sure the socket automatically gets cleaned up
try:
    with socket.create_connection(address=(host, port)) as skt:
        # This is going to add a bit of misleading overhead, but for this
        # purpose we'll use lambda for simplicity
        return_time = timer.timeit(lambda: round_trip(skt))
        
except OSError as e:
    logger.exception(
        "We could not create a socket connection to the"
        "remote echo server"
    )
    # RMV do i need raise?

logger.info("Time taken: {delay} ms".format(delay=return_time))