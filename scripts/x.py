#!/usr/bin/env python

import argparse
import sys
import socket
import random
import struct

from scapy.all import sendp, send, hexdump, get_if_list, get_if_hwaddr
from scapy.all import Packet, IPOption
from scapy.all import Ether, IP, UDP, TCP

from time import sleep

def get_if():
    ifs=get_if_list()
    iface=None # "h1-eth0"
    for i in get_if_list():
        if "eth0" in i:
            iface=i
            break;
    if not iface:
        print "Cannot find eth0 interface"
        exit(1)
    return iface

def main():

    if len(sys.argv)<3:
        print 'pass 2 arguments: <destination> "<message>"'
        exit(1)

    addr = socket.gethostbyname(sys.argv[1])
    iface = get_if()

    #hexdump(pkt)
    try:
      for i in range(int(sys.argv[3])):
        w=random.randint(1,250)
        x=random.randint(1,250)
        y=random.randint(1,250)
        z=random.randint(1,250)

        pkt = pkt =  Ether(src=get_if_hwaddr(iface), dst='ff:ff:ff:ff:ff:ff') / IP(
            src='111.11.1.{}'.format(z), dst=addr) / TCP(dport=1234, sport=random.randint(49152,65535)) / sys.argv[2]

        sendp(pkt, iface=iface)
        sleep(0.01)
    except KeyboardInterrupt:
        raise


if __name__ == '__main__':
    main()
