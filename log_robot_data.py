import logging
import time
import socket

def get_info(error):
  prev = error
  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.settimeout(2)
  try:
    s.connect((host, port))
  except socket.error:
    error = True
  else:
    error = False

  def sendCommand(cmd):
    cmd = cmd + '\n'
    s.sendall(cmd.encode())
    time.sleep(0.08)
    rcvd = s.recv(4096)
    return rcvd.decode().split()

  command = [
    'robotmode', 
    'get serial number', 
    'get loaded program', 
    'programState'
    ]

  if not error:
    for i in range(4):
      command.append(sendCommand(command[i]))
    return command[4:]
  else:
    if prev != error:
      command.append('Robot is powered off')
      return command[4]

if __name__ == "__main__":

  logging.basicConfig(
    filename='tmp.log', 
    filemode='w', 
    level=logging.INFO, 
    format='%(asctime)s - %(levelname)s - "%(message)s"', 
    datefmt='%d-%b-%y %H:%M:%S'
    )
  
  host = '169.254.54.9'
  port = 29999
  error = False

  data = get_info(error)
  if len(data) > 1:
    if data[2][0] == 'No':
      logging.info('No program loaded')
    else:
      logging.info(f'{data[2][-1]} is loaded')
  else:
    logging.warn(data[0])
  time.sleep(1)
  prog_finished = False

  while True:
    new_data = get_info(error)
    if len(new_data) == 1 and new_data != data:
      logging.warn(new_data[0])
    elif len(new_data) > 1 and len(data) > 1 and (new_data[2] != data[2] or prog_finished):
      if new_data[2][0] == 'No':
        logging.info('No program loaded')
        prog_finished = False
      else:
        if not prog_finished:
          logging.info(f'{new_data[2][-1]} is loaded')
        prog = new_data[2][-1]
        cancel = False
        while new_data[3][0] != 'PLAYING':
          time.sleep(1)
          new_data = get_info(error)
          if new_data[2][-1] != prog:
            cancel = True
            break
        if not cancel:
          logging.info(f'{new_data[2][-1]} is playing')
          start = time.time()
          while new_data[3][0] == 'PLAYING' or new_data[3][0] == 'PAUSED':
            time.sleep(1)
            new_data = get_info(error)
          logging.info(f'{new_data[2][-1]} worked for {time.time() - start}')
          prog_finished = True
        else:
          break
    
    data = new_data