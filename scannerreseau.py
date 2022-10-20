from asyncore import write
import ipaddress
import netifaces
from netaddr import IPAddress
from scapy.all import *
import os
import threading
import sys

def ARPrequest():
    i = netifaces.interfaces()
    print(i)
    interfaces = str(input())
    IpAddr = netifaces.ifaddresses(interfaces)[netifaces.AF_INET][0]['addr']
    Netmask = netifaces.ifaddresses(interfaces)[netifaces.AF_INET][0]['netmask']
    a = ipaddress.ip_network(
    IpAddr + '/'+str(IPAddress(Netmask).netmask_bits()), strict=False)
    ip = str(a)
    ans,unans = arping(ip)
    ans.summary()

def TCPrequest():
    i = netifaces.interfaces()
    print(i)
    interfaces = str(input())
    IpAddr = netifaces.ifaddresses(interfaces)[netifaces.AF_INET][0]['addr']
    Netmask = netifaces.ifaddresses(interfaces)[netifaces.AF_INET][0]['netmask']
    a = ipaddress.ip_network(
        IpAddr + '/'+str(IPAddress(Netmask).netmask_bits()), strict=False)
    ip = str(a)

def Portrequest():
    print("work")

def argumentstart(args):
    if args == "-h" or "-help":
        print("-a : make arp request to all network"+"\n"+"-t : make tcp request to all network"+"\n"+"-p : scan port of choose ip")
        return "help"
    elif args == "-t":
        return "TCP"
    elif args == "-p":
        return "Port"
    elif args == "-a":
        return "ARP"
    else :
        print("please enter a valid argument")
        print("-a : make arp request to all network"+"\n"+"-t : make tcp request to all network"+"\n"+"-p : scan port of choose ip"+"\n"+"-h : show command")
        return "invalidargs"


if len(sys.argv) < 1:
    args = str(sys.argv[1])
    resarg = argumentstart(args)
    if resarg == "TCP":
        TCPrequest()
    elif resarg == "ARP":
        ARPrequest()
    elif resarg == "Port":
        Portrequest()
        







# PING_TIMEOUT = 1

# i = netifaces.interfaces()
# print(i)
# interfaces = str(input())
# IpAddr = netifaces.ifaddresses(interfaces)[netifaces.AF_INET][0]['addr']
# Netmask = netifaces.ifaddresses(interfaces)[netifaces.AF_INET][0]['netmask']
# a = ipaddress.ip_network(
#     IpAddr + '/'+str(IPAddress(Netmask).netmask_bits()), strict=False)
# print(a)
# ip = str(a)
# print('----------------------------------')
# #for iparp in ans:
# #    print(iparp)

# #ans.summary( lambda s,r : r.sprintf("%IP.src% is alive") )
# #ans.summary()


# print(a)
# ip = str(a)
# print('----------------------------------')
# ans, unans = arping(ip)
# print(type(ans))
# print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
# print(str(ans))
# u = re.findall(r'[0-9]+(?:\.[0-9]+){3}', ans.summary())
# print("^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^")
# print(u)
# # ans, unans = sr(IP(dst=ip)/TCP(dport=53), loop=1)
# a = ans.summary()
# print(a)
