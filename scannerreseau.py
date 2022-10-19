from asyncore import write
import ipaddress
import netifaces
from netaddr import IPAddress
import scapy.all as scapy
import os

if not os.path.exists("log.txt"):
    with open("log.txt", 'w'):
        pass
file = open("log.txt", "w")

i = netifaces.interfaces()
print(i)
interfaces = str(input())
IpAddr = netifaces.ifaddresses(interfaces)[netifaces.AF_INET][0]['addr']
Netmask = netifaces.ifaddresses(interfaces)[netifaces.AF_INET][0]['netmask']
a = ipaddress.ip_network(
    IpAddr + '/'+str(IPAddress(Netmask).netmask_bits()), strict=False)
print(a)
ip = str(a)
print('----------------------------------')
scapy.arping(ip)
file.write(ans.summary())

file.close()
