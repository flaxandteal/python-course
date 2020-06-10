# -*- coding: utf-8 -*-
"""
Configuration options for the network latency tester

@author: philtweir
"""

import logging

from .client import HttpEchoClient
from .config import get_config
from .runner import ParallelRunner
from .timer import timer_run

DEFAULT_CALLER_COUNT = 10

logger = logging.getLogger(__name__)

def run_latency_tests(config):
    """
    Run and retrieve results for the latency tests.

    A more involved implementation might allow switching between
    various clients or parallelism implementations here.
    """

    # Why create a function to create a class, when it is
    # sufficient to pass the class, and let it be instantiated?
    # Arguably to be fully expressive, but Python prioritises
    # clear and concise, so this is more reasonable than in some
    # language ecosystems.
    create_client = HttpEchoClient

    runner = ParallelRunner(config)

    results = runner.execute(timer_run, create_client)

    return results

if __name__ == '__main__':
    default_config = get_config()
    output_results = run_latency_tests(default_config)
    print(output_results)
