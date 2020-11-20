import socket
import sys
import time
from robot_vision.detection import detect

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(2)
s.connect(('169.254.54.9', 29999))
s.sendall('play\n'.encode())
s.close()

HOST = "169.254.54.150" 
PORT = 30003

count = 0

print ("Connecting to robot")

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((HOST, PORT)) 
s.listen(5)
c, addr = s.accept()
print ("Connected by ", addr)

while count < 5:
  
  try:
    msg = c.recv(1024)
    print ("Starting detection")
    
    detect(0)

    c.send(b"(1)")
    print("Stopping robot")
    count += 1

  except socket.error as socketerror:
    print (socketerror)
    break
 
c.close()
s.close()
print ("Disconnected")