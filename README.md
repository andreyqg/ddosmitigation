# Implementing DDoS Detection

## Getting Started

This project is based on DDoS Detection Project from Ângelo Lapolli [angello](https://github.com/aclapolli)

### Prerequisites
We have extended both the behavioral model and the P4 reference compiler (p4c) to support hashing as required by our count sketch.
First, clone our forked repositories and follow the installation guidelines within:

- [behavioral-model](https://github.com/andreyqg/behavioral-model)
- [p4c](https://github.com/andreyqg/p4c)

#### Quick Start
YFeel free to do MAKE. This compiles our P4 code, create the network devices in Mininet and load the necessary rules on the switches.

This is the proposed topology
![topology](./Topology.png)


The last package of every observation window will be forwarded to the appropiates switches containing the following custom header:
```
// EtherType 0xFD /** 253 - Used for experimentation and testing (RFC 3692 - Chap. 2.1) */
header ddosd_t {
    bit<32> packet_num;    // The packet number within the observation window (always equal to m)
    bit<32> src_entropy;   // The last observation window entropy of source IP addresses (scaled by 2^4)
    bit<32> src_ewma;      // The current EWMA for the entropy of source IP address (scaled by 2^18)
    bit<32> src_ewmmd;     // The current EWMMD for the entropy of source IP address (scaled by 2^18)
    bit<32> dst_entropy;   // The last observation window entropy of destination IP addresses (scaled by 2^4)
    bit<32> dst_ewma;      // The current EWMA for the entropy of destination IP address (scaled by 2^18)
    bit<32> dst_ewmmd;     // The current EWMMD for the entropy of destination IP address (scaled by 2^18)
    bit<8> alarm;          // It is set to 0x01 to indicate the detection of a DDoS attack
    bit<16> ether_type;    // Indicates the following header EtherType
}
```
