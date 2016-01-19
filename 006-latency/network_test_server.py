# -*- coding: utf-8 -*-
"""
Server for network echo example

Created on Sat Jan 16 19:07:16 2016

@author: phil
"""

# Based on the Python docs

import socketserver
import logging

logging.basicConfig()
logger = logging.getLogger(__name__)


class EchoServerHandler(socketserver.BaseRequestHandler):
    def handle(self):
        logger.info("New connection")
        while True:
            message = self.request.recv(1024)
            if not message:
                break
            self.request.sendall(message)


if __name__ == "__main__":
    HOST, PORT = '143.117.100.160', 443

    server = socketserver.TCPServer((HOST, PORT), EchoServerHandler)

    server.serve_forever()
