with open('coordinates.txt', 'r') as f:
  data = f.readlines()

with open('robot.script', 'w') as f:
  for each in data:
    q = eval(each)
    f.write(f'servoj({q}, t=0.08, lookahead_time=0.1, gain=300)\n')