# -*- coding: utf-8 -*-
"""
Client that executes requests to test latency.

@author: Phil Weir <phil.weir@flaxandteal.co.uk>
"""

import socket
import os
import logging

logger = logging.getLogger(__name__)

# Parameters
DEFAULT_HOST = 'localhost'
DEFAULT_PORT = 1234
DEFAULT_REPEATS = 10  # Keep this <= 10, please!
DEFAULT_TIMEOUT = 5  # Number of seconds until giving up on connection
DEFAULT_PAYLOAD_SIZE = 1024


class HttpEchoClient:
    """
    Echo server client, connecting over HTTP.
    """

    def __init__(self, config):
        self.config = config

    def create_connection(self):
        """
        Provide a context manager for establishing the connection.
        """

        host = self.config.get('http_echo_client_host', DEFAULT_HOST)
        port = self.config.get('http_echo_client_port', DEFAULT_PORT)

        # Recommended to include units in config setting, to avoid ambiguity
        timeout = self.config.get('http_echo_client_timeout_seconds', DEFAULT_TIMEOUT)

        return socket.create_connection(address=(host, port), timeout=timeout)

    def do_round_trip(self, cxn):
        """
        Define our actual measured operation.
        """

        payload_size = self.config.get('http_echo_client_payload_size_bytes', DEFAULT_PAYLOAD_SIZE)

        # Create a random message to test our connection
        payload = os.urandom(payload_size)

        # Network-limited part
        cxn.sendall(payload)
        received_payload = cxn.recv(payload_size)

        if received_payload != payload:
            raise RuntimeError("We received an incorrect echo")
