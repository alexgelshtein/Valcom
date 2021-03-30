# RTDE connection for getting and executing coordinates on robot using ur-interface library.

import sys, time
sys.path.append('..\\ur-interface')
import URBasic

host = '169.254.54.9'
acc = 0.9
vel = 0.9

# This function reads coordinates and writes them to .txt file.
def get_coordinates(robot):
  timeout = 10
  time.sleep(1)
  start = time.time()
  robot.freedrive_mode()
  print("Let's go!")
  with open('coordinates.txt', 'w') as f:
    while time.time() < start + timeout:
      f.write('[{}, {}, {}, {}, {}, {}]\n'.format(*robot.get_actual_joint_positions()))
      time.sleep(0.05)
  robot.end_freedrive_mode()

def generate_script():
  with open('coordinates.txt', 'r') as f:
    with open('C:\\Users\\laser\\Desktop\\servoj.script', 'w') as scrpt:
      coords = f.readlines()
      q=eval(coords[0])
      scrpt.write(f'movej({q})\nstopj(0.5)\n')
      for each in coords[1:]:
        pose = eval(each)
        scrpt.write(f'servoj(q={pose}, t=0.08, lookahead_time=0.1, gain=300)\n')
      scrpt.write('stopj(0.5)')

# Sends servoj command to move robot smoothly between coordinates.
def move_robot(robot):
  with open('coordinates.txt', 'r') as f:
    coords = f.readlines()
    robot.movej(q=eval(coords[0]))
    robot.stopj(0.5)
    for each in coords[1:]:
      pose = eval(each)
      robot.servoj(q=pose, t=0.4, lookahead_time=0.03, gain=100)
    robot.stopj(0.5)

def main():
  urModel = URBasic.robotModel.RobotModel()
  robot = URBasic.urScriptExt.UrScriptExt(host=host, robotModel=urModel)
  robot.reset_error()

  func = sys.argv[1]

  # Write --coordinates to get them into .txt file and then
  # --move to execute servoj.
  if not func:
    print('usage: {--coordinates | --move | --script}')
    sys.exit(1)

  if func == '--coordinates':
    get_coordinates(robot)
  elif func == '--move':
    move_robot(robot)
  elif func == '--script':
    generate_script()
  else:
    print('Error')
    sys.exit(1)

  robot.close()

if __name__ == "__main__":
  main()