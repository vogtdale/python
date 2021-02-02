#!/bin/python3

import sys #allows us to enter commande line arguments
import socket
from datetime import datetime

# our commande line will be python3 portscanner.py <ip> 
# portscanner.py & <ip> we enter will be two arguments
#we need to check if there are any args when defining our target
if len(sys.argv) == 2: 
    target = socket.gethostbyname(sys.argv[1]) #declare our target translate a host name to IPV4
else:
    print("Invalide amount of arguments. ")
    print("Syntax should be python3 filename.py + <IP>")
    sys.exit() #closes the programm

#add a banner to make pretty
print("="*50)
print("Scanning target "+target)
print("Time started at: "+str(datetime.now()))
print("="*50)

try:
    for port in range(70,85): #need to grab ports to check if open by using a loop we check ports 70 to 85 only  because this is a shitty port scanner and slow to go from 0 to 655&something
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #create socket connection AF_INET is IPV4 & sock_STREAM is the port
        socket.setdefaulttimeout(1) #if it doesn't detect a port open will move on after a seconde or else will hang forever
        result = s.connect_ex((target,port)) #if there is an error on connection will return error indicator if there is no error returns 0
        print("Checking Port {}".format(port))
        if result == 0: 
            print("Port {} is open".format(port))
        s.close() #close program

except KeyboardInterrupt:
    print("\nExiting program.")
    sys.exit()
except socket.gaierror: #if we can't connect to the hostname
    print("Hostname couldn't be resolved")
    sys.exit()
except socket.error: #incase server is down for example
    print("Hostname couldn't be resolved")
    sys.exit()

