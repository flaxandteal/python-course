# -*- coding: utf-8 -*-
"""
Timer that averages repeated runs, to speed-test a client executing its requests.

@author: philtweir
"""

import logging
import timeit

logger = logging.getLogger(__name__)

DEFAULT_TIMER_REPEATS = 10

def timer_run(identifier, client, config):
    """
    Time the round-trip using the passed client.

    In other languages, this might quickly become a class, but in
    Python we note that no state is being stored, nor (even if there
    is a conceptual timer entity) do we have a "thing" doing multiple
    "actions". This is a bit of a grey area, but Python errs on the side
    of succinctness.
    """

    repeats = config.get('timer_repeats', DEFAULT_TIMER_REPEATS)

    # Use a `with` context to make sure the socket automatically
    # gets cleaned up
    try:
        # Note that we have moved away from the solution-focused `skt` to the
        # problem-focused `cxn`
        with client.create_connection() as cxn:
            logger.info("[%s] Created connection", identifier)

            # This is going to add a bit of misleading overhead, but for this
            # purpose we'll use lambda for simplicity
            return_time_total = timeit.timeit(
                lambda: client.do_round_trip(cxn),
                number=repeats
            )
    except OSError as exc:
        logger.error(
            "We could not create a socket connection to the "
            "remote echo server"
        )
        raise exc

    average_return_time = return_time_total / repeats

    logger.info(
        "[%s] Completed trial in %lf s (%d repeats)",
        identifier,
        average_return_time,
        repeats
    )

    return average_return_time
