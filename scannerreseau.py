from asyncore import write
import ipaddress
import netifaces
from netaddr import IPAddress
import scapy.all as scapy
from scapy import *
import os
import logging

if not os.path.exists("log.txt"):
    with open("log.txt", 'w'):
        pass
file = open("log.txt", "w")
logging.getLogger("scapy")
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
ans, unans = sr(scapy.arping(ip))
ans.show()
unans.show()
scapy.arping(ip)
file.close()
