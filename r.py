
import socket
import time
HOST = '169.254.54.9'
PORT = 29999
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(10)
s.connect((HOST, PORT))
print('Starting UR program...\n')
time.sleep(0.08)
s.send('running\n'.encode())
# FIXME: timeout might not work sometimes, so that program halts.
time.sleep(1)
data = s.recv(2048).decode().split()[-1]
print(data)