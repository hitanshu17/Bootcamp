#!/usr/bin/env python

import scapy.all as scapy


def scan(ip):
    # Using ARP to ask who has target IP
    arp_request = scapy.ARP(pdst=ip)
    # arp_request.show()

    # Set destination MAC to broadcast MAC
    broadcast = scapy.Ether(dst="ff:ff:ff:ff:ff:ff")
    # broadcast.show()
    # combination of above 2
    arp_request_broadcast = broadcast / arp_request
    # scapy.ls(scapy.Ether())
    # print(arp_request.summary())
    # scapy.ls(scapy.ARP())
    # print(broadcast.summary())
    # print (arp_request_broadcast.summary())
    # arp_request_broadcast.show()
    # answered, unanswered = scapy.srp(arp_request_broadcast, timeout=1)
    answered_list = scapy.srp(arp_request_broadcast, timeout=1, verbose=False)[0]
    print("--------------------------------------")
    print("IP\t\t\tMAC Address\n--------------------------------------")
    for element in answered_list:
        print(element[1].psrc + "\t\t" + element[1].hwsrc)


scan("10.0.2.1/24")
