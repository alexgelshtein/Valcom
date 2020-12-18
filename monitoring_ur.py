import tkinter as tk
import tkinter.messagebox
import socket
import time

def get_info():

  host = '169.254.54.9'
  port = 29999
  error = False

  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.settimeout(2)
  try:
    s.connect((host, port))
  except OSError:
    error = True

  def sendCommand(cmd):
    cmd = cmd + '\n'
    try:
      s.sendall(cmd.encode())
      time.sleep(0.08)
      rcvd = s.recv(4096)
      return rcvd.decode().split()
    except socket.timeout:
      error = True

  command = [
    'robotmode', 
    'get serial number', 
    'get loaded program', 
    'programState'
    ]

  for i in range(4):
    command.append(sendCommand(command[i]))
  
  if not error:
    mode.config(text=command[4][-1])
    sn.config(text=command[5])
    if command[6][0] == 'No':
      prog.config(text=command[6])
    else:
      prog.config(text=command[6][-1])
    state.config(text=command[7][0])
  else:
    sn.config(text='Не удается получить информацию с робота :(')

  window.after(500, get_info)

if __name__ == "__main__":

  window = tk.Tk()

  mode = tk.Label(text='')
  sn = tk.Label(text='Loading...')
  prog = tk.Label(text='')
  state = tk.Label(text='')

  mode.pack()
  sn.pack()
  prog.pack()
  state.pack()

  window.after(500, get_info)
  window.mainloop()