# -*- coding: utf-8 -*-
"""
Client that executes requests to test latency.

@author: Phil Weir <phil.weir@flaxandteal.co.uk>
"""

import pytest
from unittest.mock import patch

from latency.runner import ParallelRunner


@pytest.fixture
def config():
    return {
        'caller_count': 10
    }

@pytest.fixture
def run_cb():
    return lambda identifier, client, config: 0.1

def test_can_create_parallel_runner(config):
    """Check basic instantiation. """

    ParallelRunner(config)

def test_runner_can_generate_callers(config, run_cb):
    """Check we can create a set of concurrent callers."""

    runner = ParallelRunner(config)

    results = []

    # Ensure we have our identifiers as strings, as these will be treated as names.
    caller_indices = ['1', '2', '3', 'test']
    create_client = lambda config: None

    # Don't generally need (or should) test private methods - they're internal concerns,
    # but should test combined functionality
    # with patch('threading.Thread') as thread_mock, patch('threading.Lock') as thread_lock:
    callers = runner.generate_callers(caller_indices, run_cb, create_client, results)

    assert type(callers) is dict

    assert all([type(identifier) is str for identifier in callers])

    for idx, thread in callers.items():
        thread.index = idx
        thread.start()
        thread.join()


def test_runner_threads_require_an_index(config, run_cb):
    runner = ParallelRunner(config)

    results = []

    # Ensure we have our identifiers as strings, as these will be treated as names.
    caller_indices = ['1', '2', '3', 'test']
    create_client = lambda config: None

    # Don't generally need (or should) test private methods - they're internal concerns,
    # but should test combined functionality
    # with patch('threading.Thread') as thread_mock, patch('threading.Lock') as thread_lock:
    callers = runner.generate_callers(caller_indices, run_cb, create_client, results)

    for thread in callers.values():
        thread.start()
        thread.join()