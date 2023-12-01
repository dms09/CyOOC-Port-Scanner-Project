#!/usr/bin/python3
import pyfiglet
import sys
import socket
from datetime import datetime

#Creates an application banner
display = pyfiglet.figlet_format("CyOOC" "\n""Port Scanner")
print(display)

#User Input for target IP address and Scan option
print("Select your scan type: ")
print("[#] Select 1 for 1 - 1024 (well-known ports)")
print("[#] Select 2 for 1 - 65535 port scaning")
mode = int(input("[+] Select any option: "))
print()

ip= input(str("Target IP: "))


# Display a Banner with a timestap of when the scan started 
print("#" * 100)
print("Scanning the following Target: " + ip)
print("Scanning started at:" + str(datetime.now()))
print("#" * 100)

#Script to detect open ports on target

if mode == 1:
    try:
        # Scan ports
        for port in range(1, 65536):  # Changed the range to include port 65535
            # Tells Python we will be using IPv4
            sckt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            # Sets timeout in seconds (*must use a float value) - Values set to 0.1 for speed scan results
            socket.setdefaulttimeout(0.1)

            # If connection to open port is successful (Ex: ==0), display open port to the user
            result = sckt.connect_ex((ip, port))
            if result == 0:
                print("[+] Port {} is open".format(port))
        
        print("Scanning complete\n" + str(datetime.now()))

    except KeyboardInterrupt:
        print("[-] Scan interrupted by user")
    except socket.error:
        print("[-] Host seems down.......")
    finally:
        # Close the connection at the end of the scan
        sckt.close()
if mode == 2:
    try:
        # Scan ports
        for port in range(1, 1024):  # Changed the range to port 1024
            sckt = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            socket.setdefaulttimeout(0.1)

            result = sckt.connect_ex((ip, port))
            if result == 0:
                print("[+] Port {} is open".format(port))
        
        print("Scanning complete\n" + str(datetime.now()))

    except KeyboardInterrupt:
        print("[-] Scan interrupted by user")
    except socket.error:
        print("[-] Host seems down.......")
    finally:
        sckt.close()
