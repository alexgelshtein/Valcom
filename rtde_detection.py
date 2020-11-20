import socket
import time
import sys
sys.path.append('.\\ur-interface')
import URBasic
from robot_vision.detection import detect

HOST = '169.254.54.9'
PORT = 29999
PORT_30002 = 30003

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

secondary = """sec secondaryProgram():
write_output_integer_register(0, 400)
end"""

while data[-1] == 'true':
  reg = urModel.OutputIntRegister0()
  if reg == 111:
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    soc.settimeout(10)
    soc.connect((HOST, PORT_30002))
    time.sleep(0.08)
    print('Starting detection')
    detect(0)
    soc.send(f'{secondary}\n'.encode())
    time.sleep(0.08)
    soc.close()
  s.send('running\n'.encode())
  time.sleep(0.08)
  data = s.recv(128).decode().split()

s.close()
robot.close()