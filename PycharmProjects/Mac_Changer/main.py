#!/usr/bin/env python

import subprocess
import optparse
import re

# Refactor code


def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface of which you want to Change MAC Address")
    parser.add_option("-m", "--mac", dest="new_mac_value", help="New MAC Address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please specify an interface")
    elif not options.new_mac_value:
        parser.error("[-] Please specify a new MAC")
    return options


def change_mac(interface, new_mac_value):
    print("[+] Changing MAC Address for " + interface + " to " + new_mac_value )
    subprocess.call(["ifconfig", interface, "down"])
    subprocess.call(["ifconfig", interface, "hw", "ether", new_mac_value])
    subprocess.call(["ifconfig", interface, "up"])


def get_current_mac(interface):
    # universal_newlines = True is used because if this value is set to False then the output returned is in bytes
    ifconfig_result = subprocess.check_output(['ifconfig', interface], universal_newlines=True)
    mac_address_search_result = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", ifconfig_result)
    if mac_address_search_result:
        return mac_address_search_result.group(0)
    else:
        print('[-] Could not read the MAC Address')


options = get_arguments()

current_mac = get_current_mac(options.interface)
print("Current MAC =" + current_mac)

change_mac(options.interface, options.new_mac_value)

current_mac = get_current_mac(options.interface)
if current_mac == options.new_mac_value:
    print("[+] MAC Address was successfully changed to " + current_mac)
else:
    print("[-] MAC Address did not changed")