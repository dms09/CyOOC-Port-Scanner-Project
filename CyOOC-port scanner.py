#!/usr/bin/python3
import pyfiglet
import sys
import socket
from datetime import datetime

#Creates an application banner
display = pyfiglet.figlet_format("CyOOC" "\n""Port Scanner")
print(display)

#User Input for target IP address 
ip= input(str("Target IP: "))

# Display a Banner with a timestap of when the scan started 
print("#" * 100)
print("Scanning the following Target: " + ip)
print("Scanning started at:" + str(datetime.now()))
print("#" * 100)

#Script to detect open ports on target

try:
    #Scan ports
    for port in range(1,65535):
        # Tells python we will be using Ipv4
        sckt = socket.socket(socket.AF_INET, socket.SOCK_STREAM) 
        #sets timeout in seconds (*must use a float value) - Values set to 0.1 t speed scan results
        socket.setdefaulttimeout(0.1)

        #If connection to open port is succesful (Ex: ==0) will Display open port to user
        result =  sckt.connect_ex((ip,port))
        if result == 0:
            print("[-] Port {} is open".format(port))
        #Closes connection and continious to next port
        sckt.close()

except KeyboardInterrupt:
        print("\n .......Closing Program ......")
        sys.exit()
except socket.error:
        print("\n .....Host is not up ......")
        sys.exit()
