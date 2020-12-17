"""
A Universal Robot can be controlled from remote by sending simple commands to the GUI over a TCP/IP socket.
This interface is called the "DashBoard server". 
The server is running on port 29999 on the robots IP address. 
Each command should be terminated by a ‘\n’ also called a newline.

Command examples: load <program.urp>, play (starts the loaded program), 
stop (stops program execution), running (returns if the program is running), 
get loaded program (returns the loaded program).
"""

import socket
import time

host = '169.254.54.9'
port = 29999

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(2)
s.connect((host, port))

def sendCommand(cmd):
  cmd = cmd + '\n'
  s.sendall(cmd.encode())
  time.sleep(0.08)
  rcvd = s.recv(4096)
  print(rcvd.decode().split()[-1]) 

sendCommand('running')