# -*- coding: utf-8 -*-
"""
Created on Sat Jan 16 16:10:51 2016

@author: phil
"""

import threading
import logging
import time

# Set up the logging
logging.basicConfig(
    format="%(asctime)s - %(message)s",
    level=logging.DEBUG,
)
logger = logging.getLogger(__name__)

thread_count = 10  # Keep this <= 10, please!

data = []

lock = threading.Lock()

# Our in-thread routine
def run():
    current_thread = threading.currentThread()

    time.sleep(0.3)

    with lock:
        data.append(current_thread.index)

    logging.info("Hi, my name is %s and %s", current_thread.getName(), current_thread.index)

thread_indices = range(1, thread_count + 1)
threads = {i: threading.Thread(target=run) for i in thread_indices}

for idx, thread in threads.items():
    thread.index = idx
    thread.start()

for thread in threads.values():
    thread.join()
    
logging.info("COMPLETE: %s", str(data))