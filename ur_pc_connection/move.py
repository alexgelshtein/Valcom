"""
This program uses coordinates after get_coordinates.py program
and executes movel on robot.
"""

import socket
import time
import struct

HOST = "169.254.54.9"
PORT_30003 = 30003

print ("Starting Program")
count = 0
with open('coordinates.txt', 'r') as f:
	while count < 10:
		pose = eval(f.readline())
		print(pose)
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.settimeout(10)
			s.connect((HOST, PORT_30003))
			time.sleep(1)
			s.send(f'movel(p{pose}, 0.1, 0.2)\n'.encode())
			time.sleep(4)
			count += 1

			s.close()
		except socket.error as socketerror:
			print ("Error: ", socketerror)
		count+=1
print ("\nProgram finish")