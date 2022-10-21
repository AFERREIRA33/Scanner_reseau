import ipaddress
import netifaces
from netaddr import IPAddress
import re
from scapy.all import *
import sys
from scapy.layers.inet import IP, ICMP


def ARPrequest():
    intertable = netifaces.interfaces()
    print(intertable)
    interfaces = str(input())
    if interfaces in intertable:
        IpAddr = netifaces.ifaddresses(
            interfaces)[netifaces.AF_INET][0]['addr']
        Netmask = netifaces.ifaddresses(
            interfaces)[netifaces.AF_INET][0]['netmask']
        a = ipaddress.ip_network(
            IpAddr + '/'+str(IPAddress(Netmask).netmask_bits()), strict=False)
        ip = str(a)
        ans, _ = arping(ip)
        ans.summary()
    else:
        print("please enter a valid interface")
        ARPrequest()


def osrequest():
    os = ''
    target = str(input("Enter the Ip address:"))
    reg = r"^(([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])\.){3}([0-9]|[1-9][0-9]|1[0-9]{2}|2[0-4][0-9]|25[0-5])$"
    if re.match(reg, target):
        pack = IP(dst=target)/ICMP()
        resp = sr1(pack, timeout=3)
        if resp:
            if IP in resp:
                ttl = resp.getlayer(IP).ttl
                print(ttl)
                if ttl == 64:
                    os = 'Linux'
                    print(
                        f'\n\nTTL = {ttl} \n*{os}* Operating System is Detected \n\n')
                elif ttl == 128:
                    os = 'Windows'
                    print(
                        f'\n\nTTL = {ttl} \n*{os}* Operating System is Detected \n\n')
                elif ttl == 255:
                    os = 'Cisco Routeur'
                    print(
                        f'\n\nTTL = {ttl} \n*{os}* Operating System is Detected \n\n')
                else:
                    print('Not Found')
    else:
        print("please enter a valid ip")
        osrequest()


def Portrequest():
    print("work")
    print("Choose an IP to scan :")
    ip = str(input())
    try:
        sync = IP(dst=ip) / TCP(dport=[22, 80, 443], flags="S")
    except socket.gaierror:
        raise ValueError('Hostname {} could not be resolved.'.format(ip))
    ans, _ = sr(sync, timeout=2, retry=1)
    print("-------------")
    print(str(ans[0].answer))
    print("-------------")
    print(ans[1])
    print("-------------")
    print(ans[2])


def argumentstart(args):
    if args == "-h":
        print("-a : make arp request to all network"+"\n" +
              "-o : find the os of the choose ip"+"\n"+"-p : scan port of choose ip")
        return "help"
    elif args == "-o":
        return "os"
    elif args == "-p":
        return "Port"
    elif args == "-a":
        return "ARP"
    else:
        print("please enter a valid argument"+"\n")
        print("-a : make arp request to all network"+"\n"+"-o : find the os of the choose ip" +
              "\n"+"-p : scan port of choose ip"+"\n"+"-h : show command")
        return "invalidargs"


if len(sys.argv) <= 2 or len(sys.argv) > 1:
    args = str(sys.argv[1])
    resarg = argumentstart(args)
    if resarg == "os":
        osrequest()
    elif resarg == "ARP":
        ARPrequest()
    elif resarg == "Port":
        Portrequest()
elif len(sys.argv) >= 3:
    print("too many argument"+"\n")
    print("-a : make arp request to all network"+"\n"+"-o : find the os of the choose ip" +
          "\n"+"-p : scan port of choose ip"+"\n"+"-h : show command")
else:
    print("please enter a argument"+"\n")
    print("-a : make arp request to all network"+"\n"+"-o : find the os of the choose ip" +
          "\n"+"-p : scan port of choose ip"+"\n"+"-h : show command")
