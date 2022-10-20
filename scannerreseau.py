from asyncore import write
import ipaddress
import netifaces
from netaddr import IPAddress
<<<<<<< HEAD
#import scapy.all as scapy
from scapy.all import *
=======
import scapy.all as scapy
from scapy import sendrecv
>>>>>>> 5c9ed866d396524e8fe652750725ccda6e096291
import os
import logging

<<<<<<< HEAD

=======
if not os.path.exists("log.txt"):
    with open("log.txt", 'w'):
        pass
file = open("log.txt", "w")
logging.getLogger("scapy")
>>>>>>> 5c9ed866d396524e8fe652750725ccda6e096291
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
<<<<<<< HEAD
ans,unans = arping(ip)
#ans, unans = sr(IP(dst=ip)/TCP(dport=53))
ans.summary()              
=======
ans, unans = sr(scapy.arping(ip))
ans.show()
unans.show()
scapy.arping(ip)
file.close()
>>>>>>> 5c9ed866d396524e8fe652750725ccda6e096291
