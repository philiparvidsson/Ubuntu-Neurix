#!/usr/bin/env python

#-------------------------------------------------
# IMPORTS
#-------------------------------------------------

import socket
import sys

#-------------------------------------------------
# CONSTANTS
#-------------------------------------------------

# Li-duino is the light managing Arduino device on the network.
LIDUINO_IP   = "192.168.1.7"
LIDUINO_PORT = 23

#-------------------------------------------------
# FUNCTIONS
#-------------------------------------------------

def send_command(s):
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    sock.connect((LIDUINO_IP, LIDUINO_PORT))
    sock.send(s + "\n")

    sock.close()
    sock = None

#-------------------------------------------------
# SCRIPT
#-------------------------------------------------

if __name__ == "__main__":
    cmd = " ".join(sys.argv[1:])

    if len(cmd) == 0:
        print """no command to send

usage:

lm <on/off> <group> <socket>

example:

lm on d 1
lm off a 2

light table:

a 2 - tv
a 3 - monitor in bed room
b 1 - uv light
b 2 - living room ceiling light
d 1 - above couch
d 2 - bed lights
"""
    else:
        send_command(cmd)
