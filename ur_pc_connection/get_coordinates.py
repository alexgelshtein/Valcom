import socket
import time
import struct

HOST = "169.254.54.9"
PORT_30003 = 30003

print ("Starting Program")
count = 0
with open('coordinates.txt', 'w') as f:
	while count < 10:
		current_pose = []
		try:
			s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
			s.settimeout(10)
			s.connect((HOST, PORT_30003))
			time.sleep(1)
			data = s.recv(1024)
			for i in range(444, 485, 8):
				param = struct.unpack('!d', data[i:i+8])[0]
				current_pose.append(round(param, 3))
			f.write(str(current_pose) + '\n')

			count += 1

			s.close()
		except socket.error as socketerror:
			print ("Error: ", socketerror)

print ("\nProgram finish")