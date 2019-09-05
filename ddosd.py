#!/usr/bin/env python
import sys
import struct
import os

from scapy.all import sniff, sendp, hexdump, get_if_list, get_if_hwaddr, packet
from scapy.all import Packet, IPOption
from scapy.all import ShortField, IntField, IPField, LongField, BitField, FieldListField, FieldLenField, PacketListField, ByteField, LEFieldLenField
from scapy.all import IP, TCP, UDP, Raw
from scapy.layers.inet import _IPOption_HDR

def get_if():
    ifs=get_if_list()
    iface=None
    for i in get_if_list():
        if "eth0" in i:
            iface=i
            break;
    if not iface:
        print "Cannot find eth0 interface"
        exit(1)
    return iface

class alarm(Packet):
    name = "alarm"
    fields_desc = [ IPField("ip_alarm", None)]
    def extract_padding(self, p):
                return "", p

class DDOSD(Packet):
    name = "DDOSD"
    fields_desc = [ IntField("pkt_num", None),
                    IntField("src_entropy", None),
                    IntField("src_ewma", None),
                    IntField("src_ewmmd", None),
                    IntField("dst_entropy", None),
                    IntField("dst_ewma", None),
                    IntField("dst_ewmmd", None),
                    ByteField("alarm", None),
                    ByteField("protocol", None),
                    FieldLenField("count_ip", None, count_of="IPs"),
                    PacketListField("IPs",
                                  [],
                                  alarm,
                                  count_from=lambda pkt:pkt.count_ip)
                                   ]

packet.bind_layers(IP, DDOSD, proto=253)
packet.bind_layers(DDOSD, TCP, protocol=6)

def handle_pkt(pkt):
    if DDOSD in pkt:
        print "   "
        print "   "
        print "####################################"
        print "#          DDOS DETECTION          #"
        print "#           ALARM PACKET           #"
        print "####################################"
        pkt.show2()
        #    hexdump(pkt)
        sys.stdout.flush()
        print "####################################"


def main():

    ifaces = filter(lambda i: 'eth' in i, os.listdir('/sys/class/net/'))
    iface = ifaces[0]
    print "waiting for message on %s" % iface
    sys.stdout.flush()
    sniff(iface = iface,
          prn = lambda x: handle_pkt(x))

if __name__ == '__main__':
    main()
