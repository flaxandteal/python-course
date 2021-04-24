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
# host = 'TBC'
host = '127.0.0.1'
port = 1234
repeats = 100  # Keep this <= 100, please!
timeout = 5  # Number of seconds until giving up on connection

def round_trip(skt):
    payload = os.urandom(1024)

    skt.sendall(payload)
    received_payload = skt.recv(1024)

    if received_payload != payload:
        raise IOError("We received an incorrect echo")

try:
    with socket.create_connection(address=(host, port), timeout=timeout) as skt:
        logger.info("Created connection")
        round_trip(skt)
        logger.info("Completed trial")
except ConnectionRefusedError as e:
    logger.error(
        "We could not create a socket connection to the "
        "remote echo server"
    )
    raise e

# logger.info("Average time taken: {delay} ms".format(delay=average_return_time))
