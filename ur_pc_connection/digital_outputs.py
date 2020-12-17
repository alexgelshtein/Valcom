"""
This program connects to the robot via RT connection and retrieves 
current robot mode and values of digital outputs.
"""

import socket
import time
import struct

HOST = "169.254.54.9"
PORT_30003 = 30003

print ("Starting Program\n")

robot_mode = {
  -1: 'ROBOT_MODE_NO_CONTROLLER',
  0: 'ROBOT_MODE_DISCONNECTED',
  1: 'ROBOT_MODE_CONFIRM_SAFETY',
  2: 'ROBOT_MODE_BOOTING',
  3: 'ROBOT_MODE_POWER_OFF',
  4: 'ROBOT_MODE_POWER_ON',
  5: 'ROBOT_MODE_IDLE',
  6: 'ROBOT_MODE_BACKDRIVE',
  7: 'ROBOT_MODE_RUNNING',
  8: 'ROBOT_MODE_UPDATING_FIRMWARE'
}

def format_outputs(outputs):
  outputs = bin(int(outputs))[:1:-1]
  if len(outputs) != 8:
    outputs += '0' * (8 - len(outputs))
  # print(outputs)
  count = 0
  print('---\nDIGITAL OUTPUTS\n---\n')
  for i in outputs:
    print(f'Output {count}: {bool(int(i))}')
    count += 1

try:
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.settimeout(10)
  s.connect((HOST, PORT_30003))
  time.sleep(1)
  data = s.recv(1116)
  mode = struct.unpack('!d', data[756:764])[0]
  outputs = struct.unpack('!d', data[1044:1052])[0]
  format_outputs(outputs)
  print('\n' + robot_mode[int(mode)])

  s.close()
except socket.error as socketerror:
  print ("Error: ", socketerror)

print ("\nProgram finish")