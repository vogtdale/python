#!/bin/python3

import sys;
import socket;
from datetime import datetime;

if len(sys.argv) == 2:
    target = socket.gethostbyname(sys.argv[1])
else:
    print("Invalide Args")
    print("The sytaxe should be pyton3 filename <IP>")
    sys.exit()

print("="*50)
print("scanning target"+target)
print("Time Started at: "+str(datetime.now()))
print("="*50)


try:
    for port in range(75,85):
        s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        socket.setdefaulttimeout(1)
        result=s.connect_ex((target,port))
        print("checking Port {} ".format(port))
        if (result == 0):
            print("Port {} is open".format(port))
        s.close()
except KeyboardInterrupt:
    print("\nExiting program")
    sys.exit()

except socket.gaierror:
    print("Hostname couldnt be found")
    sys.exit()

except socket.error:
    print("Host couldnt be found")