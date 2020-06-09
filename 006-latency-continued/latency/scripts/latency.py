# -*- coding: utf-8 -*-
"""
Latency Tester

This tool checks latency, spread across parallel
executions and averaged over repeated attempts,
returning an average round trip time.

@author: philtweir
"""

# Note there is a recommended import order!
import logging

import numpy as np
import click

from latency.tester import run_latency_tests
from latency.config import get_config

@click.option('--output-file', '-o', default=None)
@click.option('--config-file', '-c', default=None)
@click.command()
def cli(output_file=None, config_file=None):
    """
    Entry-point to run the latency tester
    """

    config = get_config(config_file)

    # Set up the logging
    # Perhaps this uses certain config settings
    logging.basicConfig(
        format="%(asctime)s - %(threadName)s - %(message)s",
        level=logging.DEBUG,
    )

    results = run_latency_tests(config)

    # We are likely to want to play around with the statistics, in
    # Jupyter or elsewhere, so we save them...
    if output_file:
        np.save(output_file, results)
        # This saves in a numpy-specific format - if you want CSV, try savetxt, or
        # savez for a compressed version
