import sys, math, numpy
sys.path.append('..\\ur-interface')
import URBasic
from URBasic import kinematic

host = '169.254.54.9'

urModel = URBasic.robotModel.RobotModel()
robot = URBasic.urScriptExt.UrScriptExt(host=host, robotModel=urModel)
robot.reset_error()
home_pose = list(robot.get_actual_tcp_pose())
circle_pose = numpy.array(home_pose).tolist()

with open('coordinates.txt', 'w') as f:
  for y in numpy.linspace(-0.1, 0.1, 50):
    x = math.sqrt(0.1 ** 2 - y ** 2)
    circle_pose[0] = x + home_pose[0]
    circle_pose[1] = y + home_pose[1]
    circle_q = kinematic.Invkine_manip( target_pos=circle_pose, 
                                        init_joint_pos=robot.get_actual_joint_positions(), 
                                        tcpOffset=[0, 0, 0.05, 0, 0, 0])
    f.write(str(list(circle_q)) + '\n')

  for y in numpy.linspace(0.1, -0.1, 50):
    x = -math.sqrt(0.1 ** 2 - y ** 2)
    circle_pose[0] = x + home_pose[0]
    circle_pose[1] = y + home_pose[1]
    circle_q = kinematic.Invkine_manip( target_pos=circle_pose, 
                                        init_joint_pos=robot.get_actual_joint_positions(), 
                                        tcpOffset=[0, 0, 0.05, 0, 0, 0])
    f.write(str(list(circle_q)) + '\n')

with open('coordinates.txt', 'r') as f:
  coords = f.readlines()
  for each in coords:
    q = eval(each)
    robot.servoj(q=q, t=0.4, lookahead_time=0.03, gain=100)
  robot.stopj(0.5)

robot.movel(pose=home_pose, a=1.2, v=0.25)
robot.close()