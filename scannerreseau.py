import ipaddress
import netifaces
from netaddr import IPAddress
import os
from ipaddress import IPv4Network

interfaces = netifaces.gateways()['default'][netifaces.AF_INET][1]
interfaces = netifaces.ifaddresses(str(interfaces))
IpAddr = interfaces[netifaces.AF_INET][0]['addr']
Netmask = interfaces[netifaces.AF_INET][0]['netmask']
print('ip :' + IpAddr)

print('netmask :'+Netmask)
a = ipaddress.ip_network(
    IpAddr + '/'+str(IPAddress(Netmask).netmask_bits()), strict=False)
print(a)
print('----------------------------------')
# a = IpAddr + '/' + ipaddress(Netmask).netmask_bits()
for ip in ipaddress.IPv4Network(a):
    response = os.popen(f"ping {ip} -n 1").read()
    print(response)
