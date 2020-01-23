#!/usr/bin/python

from scapy.all import rdpcap,wrpcap

pcapin = 'eddostrace.to-victim.20070804_140436.pcap'
pcapout = 'ddostrace.to-victim.20070804_140436_out.pcap'

newipdest = '10.0.53.99'

print '     '
print 'Importing',pcapin
source_pcap = rdpcap(pcapin)
print 'Imported',pcapin
print '     '

max = len(source_pcap)

print 'We are going to rewrite',max,'entries in',pcapin,'are you sure?'
print '     '
raw_input("Press Enter to proceed...")

for x in range(0,max):
		
		y = x+1
		ipdest = source_pcap[x]['IP'].dst
		print  'Rewriting destination source',ipdest, '->',newipdest, 'in line:', y 
		source_pcap[x]['IP'].dst = newipdest

print '     '
print 'Done!! Generating',pcapout

wrpcap(pcapout,source_pcap)

print '     '

raw_input("Finished. Press Enter to exit")