#!/usr/bin/python

import random
from scapy.all import rdpcap,wrpcap

pcapin = 'legitimate_00005_20160406100318_ipv4.pcap'
pcapout = 'legitimate_20160406100318.pcap'

print '     '
print 'Importing',pcapin
source_pcap = rdpcap(pcapin)

print 'Imported',pcapin
print '     '

max = len(source_pcap)

print 'We are going to rewrite',max,'entries in',pcapin, 'are you sure?'
print '     '
raw_input("Press Enter to proceed...")

for x in range(0,max):
		
		w=random.randint(80,99)
		newdst='10.0.51.{}'.format(w)
		
		y = x+1
		ipdest = source_pcap[x]['IP'].dst
		print  'Rewriting in line:', y, '/',max,'destination IP',ipdest, '->',newdst
		source_pcap[x]['IP'].dst = newdst

print '     '
print 'Done!! Generating',pcapout

wrpcap(pcapout,source_pcap)

print '     '

print 'Concluded'
