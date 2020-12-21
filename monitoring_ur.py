import tkinter as tk
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
  except socket.error as e:
    error = True
    err_msg = e

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
    mode.config(text=command[4][-1])
    sn.config(text=command[5])
    if command[6][0] == 'No':
      prog.config(text=command[6])
    else:
      prog.config(text=command[6][-1])
    state.config(text=command[7][0])
  else:
    sn.config(text='Не удается получить информацию с робота :(')
    prog.config(text=err_msg)

  window.after(500, get_info)
  center_the_window(window)

# Layout main window in the center of the screen 
def center_the_window(root):

  root.update_idletasks()
  sizes = root.geometry().split('+')
  window_w = int(sizes[0].split('x')[0])
  window_h = int(sizes[0].split('x')[1])
  w = root.winfo_screenwidth() // 2
  h = root.winfo_screenheight() // 2
  w -= window_w // 2
  h -= window_h // 2
  root.geometry(f'+{w}+{h}')

if __name__ == "__main__":

  window = tk.Tk()
  window.title('Robot monitoring')
  window.resizable(False, False)

  def log_window():
    log = tk.Toplevel()
    log.title('Log')
    log.geometry('200x200')
    log.resizable(False, False)
    exit_btn = tk.Button(
      log, 
      text='Exit', 
      command=log.destroy, 
      relief='groove', 
      activebackground='lightgray'
      )
    exit_btn.pack(side='bottom')
    center_the_window(log)
    log.mainloop()

  mode = tk.Label(text='')
  sn = tk.Label(text='Loading...')
  prog = tk.Label(text='')
  state = tk.Label(text='')
  log_btn = tk.Button(
    window, 
    text='Log', 
    command=log_window, 
    relief='groove', 
    activebackground='lightgray'
    )

  mode.pack()
  sn.pack()
  prog.pack()
  state.pack()
  log_btn.pack(side='bottom')

  window.after(500, get_info)
  center_the_window(window)
  window.mainloop()