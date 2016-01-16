# -*- coding: utf-8 -*-
"""
Server for network echo example

Created on Sat Jan 16 19:07:16 2016

@author: phil
"""

# Based on the Python docs

import SocketServer

class EchoServerHandler(SocketServer.BaseRequestHandler):
    def handle(self):
        message = self.request.recv(1024)
        self.request.sendall(message)
        

if __name__ == "__main__":
    HOST, PORT = "flaxandteal.co.uk", 9998
    
    server = SocketServer.TCPServer((HOST, PORT), EchoServerHandler)
    
    server.serve_forever()