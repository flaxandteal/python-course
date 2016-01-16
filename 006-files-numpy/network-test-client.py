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
host = 'flaxandteal.co.uk'
port = 9998
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
        raise RuntimeError("We received an incorrect echo")


# Use a `with` context to make sure the socket automatically
# gets cleaned up
try:
    with socket.create_connection(address=(host, port), timeout=timeout) as skt:
        logger.info("Created connection")
        # This is going to add a bit of misleading overhead, but for this
        # purpose we'll use lambda for simplicity
        return_time = timeit.timeit(
            lambda: round_trip(skt),
            number=repeats
        )
        logger.info("Completed trial")
        
except OSError as e:
    logger.error(
        "We could not create a socket connection to the "
        "remote echo server"
    )
    raise e

logger.info("Average time taken: {delay} ms".format(delay=return_time))