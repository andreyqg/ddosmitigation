#!/usr/bin/python3

import argparse
import os

def run_tshark(in_pcap, out_txt):
    command = "tshark -q -z 'io,stat,109' -r " + in_pcap + " > " + out_txt
    os.system(command)

def main():


    parser = argparse.ArgumentParser(description="Obtain statistics from a PCAP file generated and outputs a TXT file containing " + 
                                                 "Interval - Frames - Bytes")
    parser.add_argument("-i", "--in_pcap", help="PCAP file to process")
    parser.add_argument("-o", "--out_txt", help="TXT file to save results to")
    args = parser.parse_args()

    assert os.path.isfile(args.in_pcap)
    assert not os.path.isfile(args.out_txt) 
        
    run_tshark(args.in_pcap, args.out_txt) 
        
if __name__ == '__main__':
    main()
