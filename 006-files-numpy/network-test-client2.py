# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 16:10:51 2016

@author: phil
"""

import socket
import os
import timeit
import logging
import threading
import numpy as np

# Set up the logging
logging.basicConfig(
    format="%(asctime)s - %(threadName)s - %(message)s",
    level=logging.DEBUG,
)
logger = logging.getLogger(__name__)

# Parameters
host = 'flaxandteal.co.uk'
port = 9998
repeats = 10  # Keep this <= 10, please!
thread_count = 10  # Keep this <= 10, please!
timeout = 5  # Number of seconds until giving up on connection
output_filename = "latency"


# Define our actual measured operation
def round_trip(skt):
    # Create a random message to test our connection
    payload = os.urandom(1024)
    
    # Network-limited part
    skt.sendall(payload)
    received_payload = skt.recv(1024)
    
    if received_payload != payload:
        raise RuntimeError("We received an incorrect echo")


# This is essentially the code from our previous experiment
def run():
    currentThread = threading.currentThread()

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

    # Strictly, a lock isn't required for accessing a dict, but this is an
    # opportunity to demonstrate the use of locks
    with lock:
        results.append((currentThread.index, return_time))
        
    logger.info("Average time taken: {delay} ms".format(delay=return_time))
    

# Store the results in this list
results = []
lock = threading.Lock()
thread_indices = range(1, thread_count + 1)

# Threads are given names as integers 1-N
# This is easier to handle in numpy
threads = {i: threading.Thread(target=run) for i in thread_indices}

# The items method turns a module into pairs (tuples) of key and value
for idx, thread in threads.items():
    thread.index = idx
    thread.start()

# values just returns the values
for thread in threads.values():
    thread.join()

# Now we switch our results (2xthread_count) list to a numpy structure
data = np.array(results)

logger.info("All threads completed")
logger.info("Average time : %lf ms" % data[1].mean())

# However, we are likely to want to play around with the statistics, in
# Jupyter or elsewhere, so we save them...
np.save(output_filename, data)
# This saves in a numpy-specific format - if you want CSV, try savetxt, or
# savez for a compressed version