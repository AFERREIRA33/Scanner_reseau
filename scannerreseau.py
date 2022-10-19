import ipaddress
import netifaces
from netaddr import IPAddress
import os
import scapy
from scapy.all import ARP, Ether, srp

print(scapy.__version__)
interfaces = netifaces.ifaddresses(
    str(netifaces.gateways()['default'][netifaces.AF_INET][1]))
IpAddr = interfaces[netifaces.AF_INET][0]['addr']
Netmask = interfaces[netifaces.AF_INET][0]['netmask']
a = ipaddress.ip_network(
    IpAddr + '/'+str(IPAddress(Netmask).netmask_bits()), strict=False)
print(a)
print('----------------------------------')
for ip in ipaddress.IPv4Network(a):
    response = os.popen(f"ping {ip} 0-n 1").read()
    print(response)
