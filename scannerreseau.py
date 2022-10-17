import ipaddress
import socket 
hostname = socket.gethostname()    
IPAddr = socket.gethostbyname(hostname)   
print("Your Computer IP Address is:" + IPAddr) 
# for ip in ipaddress.IPv4Network('192.168.1.0/24'):
#     print(ip)