#!/usr/bin/env python3

# -*- coding: utf-8 -*-
"""
Server for network echo example

Created on Sat Jan 16 19:07:16 2016

@author: phil
"""

# Based on the Python documenation
# https://docs.python.org/3/library/asyncio-protocol.html

import argparse
import logging
import asyncio

DELAY = 0.01

logging.basicConfig()
logger = logging.getLogger(__name__)


class EchoServerClientProtocol(asyncio.Protocol):
    """Return message to client"""
    transport = None

    def connection_made(self, transport):
        """Store the transport for communication"""
        self.transport = transport

    def data_received(self, data):
        """Handle new message"""
        asyncio.async(self.respond(data))
        
    @asyncio.coroutine
    def respond(self, data):
        yield from asyncio.sleep(DELAY)
        self.transport.write(data)


def parse_args():
    """Parse arguments from CL"""
    parser = argparse.ArgumentParser()
    parser.add_argument('--host', required=True)
    parser.add_argument('--port', type=int, required=True)

    return parser.parse_args()


def run():
    """Run server with host and port"""
    args = parse_args()
    host, port = args.host, args.port

    loop = asyncio.get_event_loop()
    coro = loop.create_server(EchoServerClientProtocol, host, port)
    server = loop.run_until_complete(coro)

    try:
        loop.run_forever()
    except KeyboardInterrupt:
        pass

    server.close()
    loop.run_until_complete(server.wait_closed())
    loop.close()


if __name__ == "__main__":
    run()
