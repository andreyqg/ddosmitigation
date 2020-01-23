#!/usr/bin/python

from scapy.all import rdpcap,wrpcap

pcapin = 'equinix-chicago.dirA.20160406-130300.UTC.anon.pcap'
pcapout = 'equinix-chicago.dirA.20160406-130300.UTC.anon_out.pcap'

newipdest1 = '10.0.53.90'
newipdest2 = '10.0.53.91'
newipdest3 = '10.0.53.92'
newipdest4 = '10.0.53.93'
newipdest5 = '10.0.53.94'
newipdest6 = '10.0.53.95'
newipdest7 = '10.0.53.96'
newipdest8 = '10.0.53.97'
newipdest9 = '10.0.53.98'
newipdest10 = '10.0.53.99'


print '     '
print 'Importing',pcapin
source_pcap = rdpcap(pcapin)
print(animation[idx % len(animation)], end="\r")
print 'Imported',pcapin
print '     '

max = len(source_pcap)

print 'We are going to rewrite',max,'entries in',pcapin, 'are you sure?'
print '     '
raw_input("Press Enter to proceed...")

for x in range(0,max,10):
		
		y = x+1
		ipdest = source_pcap[x]['IP'].dst
		print  'Rewriting destination IP',ipdest, '->',newipdest1, 'in line:', y 
		source_pcap[x]['IP'].dst = newipdest1

for x in range(1,max,10):
		
		y = x+1
		ipdest = source_pcap[x]['IP'].dst
		print  'Rewriting destination IP',ipdest, '->',newipdest2, 'in line:', y 
		source_pcap[x]['IP'].dst = newipdest2

for x in range(2,max,10):
		
		y = x+1
		ipdest = source_pcap[x]['IP'].dst
		print  'Rewriting destination IP',ipdest, '->',newipdest3, 'in line:', y 
		source_pcap[x]['IP'].dst = newipdest3

for x in range(3,max,10):
		
		y = x+1
		ipdest = source_pcap[x]['IP'].dst
		print  'Rewriting destination IP',ipdest, '->',newipdest4, 'in line:', y 
		source_pcap[x]['IP'].dst = newipdest4

for x in range(4,max,10):
		
		y = x+1
		ipdest = source_pcap[x]['IP'].dst
		print  'Rewriting destination IP',ipdest, '->',newipdest5, 'in line:', y 
		source_pcap[x]['IP'].dst = newipdest5

for x in range(5,max,10):
		
		y = x+1
		ipdest = source_pcap[x]['IP'].dst
		print  'Rewriting destination IP',ipdest, '->',newipdest6, 'in line:', y 
		source_pcap[x]['IP'].dst = newipdest6

for x in range(6,max,10):
		
		y = x+1
		ipdest = source_pcap[x]['IP'].dst
		print  'Rewriting destination IP',ipdest, '->',newipdest7, 'in line:', y 
		source_pcap[x]['IP'].dst = newipdest7

for x in range(7,max,10):
		
		y = x+1
		ipdest = source_pcap[x]['IP'].dst
		print  'Rewriting destination IP',ipdest, '->',newipdest8, 'in line:', y 
		source_pcap[x]['IP'].dst = newipdest8

for x in range(8,max,10):
		
		y = x+1
		ipdest = source_pcap[x]['IP'].dst
		print  'Rewriting destination IP',ipdest, '->',newipdest9, 'in line:', y 
		source_pcap[x]['IP'].dst = newipdest9

for x in range(9,max,10):
		
		y = x+1
		ipdest = source_pcap[x]['IP'].dst
		print  'Rewriting destination IP',ipdest, '->',newipdest10, 'in line:', y 
		source_pcap[x]['IP'].dst = newipdest10

print '     '
print 'Done!! Generating out.pcap'

wrpcap(pcapout,source_pcap)

print '     '

raw_input("Finished. Press Enter to exit")