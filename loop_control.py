import socket
import time
import sys
sys.path.append('.\\ur-interface')
import URBasic

HOST = '169.254.54.9'
PORT = 29999

urModel = URBasic.robotModel.RobotModel()
robot = URBasic.urScriptExt.UrScriptExt(host=HOST, robotModel=urModel)

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.settimeout(10)
s.connect((HOST, PORT))
print('Starting UR program...\n')
time.sleep(1)

s.send('play\n'.encode())
time.sleep(0.08)

s.send('running\n'.encode())
time.sleep(0.08)
data = s.recv(128).decode().split()

cycle = 0
start = time.time()

while data[-1] == 'true':
  reg = urModel.OutputIntRegister0()
  if cycle < reg:
    cycle = reg
    print(f'Marking detail № {reg}')
  s.send('running\n'.encode())
  time.sleep(0.08)
  data = s.recv(128).decode().split()

print(f'\n{cycle} details are done!')
print('It took ' + str(round((time.time() - start), 2)) + ' sec\n')
s.close()
robot.close()