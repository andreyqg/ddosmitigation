# Implementing DDoS Attacks Collaborative Mitigation Mechanism

This project is based on "[Offloading Real-time DDoS Attack Detection to Programmable Data Planes](https://ieeexplore.ieee.org/document/8717869)" (IM 2019) Project from [Ângelo Lapolli](https://github.com/aclapolli) and [Jonatas Marques](https://github.com/jonadmark/)

### Prerequisites
We have extended both the behavioral model and the P4 reference compiler (p4c) to support hashing as required by our count sketch (For Attack Detection), in our Heavy Hitters Detection and our Bloom Filter implementation.
First, clone our forked repositories and follow the installation guidelines within:

- [Behavioral Model](https://github.com/andreyqg/behavioral-model)
- [P4_16 compiler](https://github.com/andreyqg/p4c)

#### Quick Start
Feel free to do MAKE. This compiles our P4 code, create the network devices in Mininet and load the necessary rules on each switch (via CLI and Runtime).

This is the proposed topology (The red color indicates that device is running our mechanism)

![topology](./Topology.png)

The Detection  Mechanism is configured with '8192' (2<sup>14</sup>) packet for each observation window

In case of Attack Detection, the last package of every observation window will be forwarded to the appropiates switches containing the following custom header:
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
The main goal of the proposed mitigation mechanism is once the attack is detected, to identify the suspect IPs, and propagate them to the upstream switches to mitigate the attack each time closer to the source, following a [PushBack Strategy](https://www.researchgate.net/publication/242106891_Controlling_High_Bandwidth_Aggregates_in_the_Network_Extended_Version).

The proposed mechanism contains different components described below, following the flow for an incoming packet.

When an incoming packet arrives, the switch verifies if the source IP is recognized as a suspect address. For this, the mitigation mechanism incorporates as first component a suspect list with all suspect IP addresses identified. If the IP address matches in the suspect list, the packet is sent to the second component or filtering strategy component, to determine if the packet is dropped or can continue the flow. If the IP address no matches in the suspect list, the packet is sent to the third component.

The mechanism contains a third component to determine suspect IPs; all the packets that did not match the suspect list arrive here. In the switch where the victim is linked, this component keeps flow statistics. This component determines the IP suspects of causing the attack based on the numbers of packets seen from each source IP. If an IP address is identified as a suspect, it is included in the suspect list. This component works differently in other switches; in theirs, this component maintains an IP list to inspect, created for the IP addresses accused of downstream switches.  If an IP address matches the inspection list, it is immediately included in the suspect list. After going through this component, the package goes to the fourth component.

The fourth component refers to the entropy-based detection component. All packets not dropped arrives here. At the final of the monitoring window (a determined number of packets forwarded) is calculated the entropy value.  At that moment, we go to the fifth component. But if it is not yet the end of the monitoring window, the packet is sent to the destination.

At the final of the monitoring window is calculated the entropy value; with this value, the fifth component determines if the switch is under attack. If the switch is under attack, it generates an alarm packet, including all the suspect IPs identified in the monitoring window. The alarm packet is sent to the upstream switches to advise about the attack and the IPs causing it. Also is generated a notification alarm when there are downstream switches.

When a switch receives an alarm packet, if the attack was not detected yet, the detection mechanism values are adjusted to try to discover the attack. Also, the IP addresses included in the alarm packet are saved in the inspection list.  On the other hand, if a notification packet is received from all the upstream switches, containing the same IP address, it is erased from the suspect list in the switch that is receiving the notification package.

Our Heavy Hitter Detection Mechanism supports '8400' slots and our IPBlockers supports '1400' slots currently. You can change this support into our modified hash functions, before the compiling Behavioral Model and P4C.


