#!/usr/bin/env python

# before starting exclude cmd:- iptables -I FORWARD -j NFQUEUE --queue-num 0
# the above command will create a queue table
# if testing on your own machine then use:-
# iptables -I OUTPUT -j NFQUEUE --queue-num 0 and iptables -I INPUT -j NFQUEUE --queue-num 0

import netfilterqueue


def process_packet(packet):
    print(packet)
    # packet.drop() # packet will drop as a result it will not reach the destination(target)
    packet.accept() # packet will be sent forward thus allow the target to access internet

queue = netfilterqueue.NetfilterQueue()
queue.bind(0, process_packet)
queue.run()