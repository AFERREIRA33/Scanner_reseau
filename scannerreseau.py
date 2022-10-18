import netifaces

interfaces = netifaces.interfaces()

print(netifaces.ifaddresses(str(interfaces[1])))
# ip = str(input("ip : "))


# for ip in ipaddress.IPv4Network(ip):
    # response = os.popen(f"ping {ip}").read()
    # print(ip)
