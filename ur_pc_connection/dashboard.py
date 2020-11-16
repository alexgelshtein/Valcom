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
  time.sleep(1)
  rcvd = s.recv(4096)
  print(rcvd.decode().split('\n')[1]) 

sendCommand('PolyscopeVersion')