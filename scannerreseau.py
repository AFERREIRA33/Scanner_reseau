import ipaddress
import netifaces
from netaddr import IPAddress
from scapy.all import *
import sys


def ARPrequest():
    i = netifaces.interfaces()
    print(i)
    interfaces = str(input())
    IpAddr = netifaces.ifaddresses(interfaces)[netifaces.AF_INET][0]['addr']
    Netmask = netifaces.ifaddresses(
        interfaces)[netifaces.AF_INET][0]['netmask']
    a = ipaddress.ip_network(
        IpAddr + '/'+str(IPAddress(Netmask).netmask_bits()), strict=False)
    ip = str(a)
    ans, _ = arping(ip)
    ans.summary()


def TCPrequest():
    i = netifaces.interfaces()
    print(i)
    interfaces = str(input())
    IpAddr = netifaces.ifaddresses(interfaces)[netifaces.AF_INET][0]['addr']
    Netmask = netifaces.ifaddresses(
        interfaces)[netifaces.AF_INET][0]['netmask']
    a = ipaddress.ip_network(
        IpAddr + '/'+str(IPAddress(Netmask).netmask_bits()), strict=False)
    ip = str(a)


def Portrequest():
    print("work")
    print("Choose an IP to scan :")
    ip = str(input())
    port = IP(dst=ip) / TCP(dport=[22, 443], flags="S")
    ans, _ = sr(port, timeout=2, retry=1)
    for sent, received in ans:
        if received[TCP].flags == "SA":
            print(received[TCP].sport)


def argumentstart(args):
    if args == "-h":
        print("-a : make arp request to all network"+"\n" +
              "-t : make tcp request to all network"+"\n"+"-p : scan port of choose ip")
        return "help"
    elif args == "-t":
        return "TCP"
    elif args == "-p":
        return "Port"
    elif args == "-a":
        return "ARP"
    else:
        print("please enter a valid argument"+"\n")
        print("-a : make arp request to all network"+"\n"+"-t : make tcp request to all network" +
              "\n"+"-p : scan port of choose ip"+"\n"+"-h : show command")
        return "invalidargs"


if len(sys.argv) <= 2:
    args = str(sys.argv[1])
    resarg = argumentstart(args)
    if resarg == "TCP":
        TCPrequest()
    elif resarg == "ARP":
        ARPrequest()
    elif resarg == "Port":
        Portrequest()
elif len(sys.argv) >= 3:
    print("too many argument"+"\n")
    print("-a : make arp request to all network"+"\n"+"-t : make tcp request to all network" +
          "\n"+"-p : scan port of choose ip"+"\n"+"-h : show command")
else:
    print("please enter a argument"+"\n")
    print("-a : make arp request to all network"+"\n"+"-t : make tcp request to all network" +
          "\n"+"-p : scan port of choose ip"+"\n"+"-h : show command")


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
