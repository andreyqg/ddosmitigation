# BUNGEE

BUNGEE is an in-network, collaborative pushback mechanism for DDoS attack mitigation that runs entirely in the data plane. This mechanism is able to, locally at a given switch, identify suspect IP addresses (through the use of continuous IP entropy analysis) and propagate them to other switches. The different switches that are made aware of the suspects enforce a pushback strategy for repelling potential attacks.

## Implementing DDoS Attacks Collaborative Mitigation Mechanism

This project implementation refers to [BUNGEE: An Adaptive Pushback Mechanism for DDoS Detection and Mitigation in P4 Data Planes](https://ieeexplore.ieee.org/document/9463992)

Entropy analysis component for DDoS detection, mentioned in our work, is based on [Offloading Real-time DDoS Attack Detection to Programmable Data Planes](https://ieeexplore.ieee.org/document/8717869) Project from [Ângelo Lapolli](https://github.com/aclapolli) and [Jonatas Marques](https://github.com/jonadmark/)

### Prerequisites
We have extended both the behavioral model (BM) and the P4 reference compiler (p4c) to support hashing as required by our count sketch (For Attack Detection), in our Heavy Hitters Detection and our Bloom Filter implementation.

First, clone our forked repositories and follow the installation guidelines within:

- [Behavioral Model](https://github.com/andreyqg/behavioral-model)
- [P4_16 compiler](https://github.com/andreyqg/p4c)

You can use our [install.sh](https://github.com/andreyqg/ddosmitigation/blob/master/install.sh) to install all you need to run our project. We strongly recommend use [Linux Ubuntu 18.04 LTS](https://releases.ubuntu.com/18.04/ubuntu-18.04.6-desktop-amd64.iso) since it was the OS where we ran our avaliation.

#### Quick Start
Feel free to do MAKE. This compiles our P4 code, create the network devices in Mininet and load the necessary rules on each switch (via CLI and Runtime). In the folder [sw_rules](https://github.com/andreyqg/ddosmitigation/tree/master/sw_rules) you find the table rules for each switch, they are configured according the topology, if you alter this topology you must update these rules, so that the proper functioning of our mechanism.

This is the proposed topology, using Mininet.

![topology](./topology.png)

You can use the [included scripts](https://github.com/andreyqg/ddosmitigation/tree/master/scripts) to test your lab, sending and receiving packet from/to hosts. You can also use this [lightweight workload](https://github.com/andreyqg/ddosmitigation/blob/master/fastest.tar.gz) to test connectivity (via the tcpreplay command)

Detection  mechanism is configured with '8192' (2<sup>14</sup>) packets for each monitoring window.

In case of attack detection, the last package of every monitoring window will be cloned and forwarded to the appropiates switches containing the following custom header:
```
// EtherType 0xFD /* 253 - Used for experimentation and testing (RFC 3692 - Chap. 2.1) */
header DDOSD {
    bit<32> packet_num;    // The packet number within the observation window (always equal to m)
    bit<32> src_entropy;   // The last observation window entropy of source IP addresses (scaled by 2^4)
    bit<32> src_ewma;      // The current EWMA for the entropy of source IP address (scaled by 2^18)
    bit<32> src_ewmmd;     // The current EWMMD for the entropy of source IP address (scaled by 2^18)
    bit<32> dst_entropy;   // The last observation window entropy of destination IP addresses (scaled by 2^4)
    bit<32> dst_ewma;      // The current EWMA for the entropy of destination IP address (scaled by 2^18)
    bit<32> dst_ewmmd;     // The current EWMMD for the entropy of destination IP address (scaled by 2^18)
    bit<8> alarm;          // It is set to 0x01 to indicate the detection of a DDoS attack
    bit<8> protocol;       // Indicates the following header TCP
    bit<8> count_ip;       // Number of IP Address in alarm packet
    
header ALARM {
    bit<32> ip_alarm;      // IP Address suspects pool for checking
}
```
