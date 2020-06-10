# -*- coding: utf-8 -*-
"""
Parallel executor, which kicks off a series of calls and aggregates their results.

@author: Phil Weir <phil.weir@flaxandteal.co.uk>
"""

import logging
import threading
import numpy as np # note ordering

DEFAULT_CALLER_COUNT = 10

logger = logging.getLogger(__name__)

class ParallelRunner:
    """
    Runner for tests that calculate average latency to a server.
    """

    def __init__(self, config):
        self._config = config

    @staticmethod
    def run_caller(run_cb, create_client, lock, results, config):
        """
        Launch an individual parallel call (runs in thread).
        """

        # Here is an example of where Python's EAFP philosophy can make it difficult
        # to document hidden expectations (as opposed to an interface-heavy language)
        # Here, we expect create_client to take one argument - the config.
        client = create_client(config)
        identifier = threading.currentThread().index
        result = run_cb(identifier, client, config)

        with lock:
            results.append((identifier, float(result)))

    def generate_callers(self, caller_indices, run_cb, create_client, results):
        """
        Create a set of concurrent callers to spread out the requests to a caller.
        """

        lock = threading.Lock()

        # Threads are given names as integers 1-N
        # This is easier to handle in numpy
        # We could abstract this further, but this may give diminishing returns
        # However, by factoring this into a separate method, we allow for
        # extension by subclassing, perhaps replacing threads with subprocesses
        # Note the assumption that accessing self._config is thread-safe built in here
        # Conventionally, using shorter names than elsewhere is acceptable in a comprehension
        threads = {
            i: threading.Thread(
                target=self.run_caller,
                args=(run_cb, create_client, lock, results, self._config)
            )
            for i in caller_indices
        }

        return threads

    def execute(self, run_cb, create_client):
        """
        Run the tests for latency.
        """

        # Store the results in this list.
        results = []

        caller_count = self._config.get('caller_count', DEFAULT_CALLER_COUNT)

        # Ensure we have our identifiers as strings, as these will be treated as names.
        caller_indices = map(str, range(1, caller_count + 1))

        callers = self.generate_callers(caller_indices, run_cb, create_client, results)

        # The items method turns a module into pairs (tuples) of key and value
        for idx, caller in callers.items():
            caller.index = idx
            caller.start()

        # values just returns the values
        for thread in callers.values():
            thread.join()

        logger.info("All threads completed")

        # Now we switch our results (2xthread_count) list to a numpy structure
        data = np.array([trip_time for identifier, trip_time in results])

        average_time = data.mean()

        # It is recommended to use logging's in-built string interpolation
        # rather than format strings, or directly formatting into the string.
        logger.info("Average time : %lf s", average_time)

        return data
