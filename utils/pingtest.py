#!/usr/bin/env python

import dpkt
import socket, random

echo = dpkt.icmp.ICMP.Echo()
echo.id = random.randint(0, 0xffff)
echo.seq = random.randint(0, 0xffff)
echo.data = 'hello world'

icmp = dpkt.icmp.ICMP()
icmp.type = dpkt.icmp.ICMP_ECHO
icmp.data = echo

#s = socket.socket(socket.AF_INET, socket.SOCK_RAW, dpkt.ip.IP_PROTO_ICMP)
#s.connect(('74.125.67.100', 1))
#sent = s.send(str(icmp))
#
#print 'sent %d bytes' % sent
