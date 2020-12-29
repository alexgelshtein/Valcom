import tkinter as tk
import socket
import time
import re

HOST = '192.168.71.128'
PORT = 29999

command = [
  'robotmode', 
  'get serial number', 
  'get loaded program', 
  'programState'
  ]

# Connect to port 29999 (dashboard)
def dashboard_connection():

  s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
  s.settimeout(2.0)
  
  try:
    s.connect((HOST, PORT))
    return s
  except socket.error as e:
    s.close()
    prog.config(text=f'[ERROR] - {e}')
    return None

# Send command via dashboard and receive data
def send_string(s, cmd):
  
  cmd = cmd + '\n'
  s.sendall(cmd.encode())
  time.sleep(0.08)
  rcvd = s.recv(2048).decode().split()
  return rcvd

# Send list of commands and receive a list of data
def receive_data_list():

  data = []
  s = dashboard_connection()

  if s != None:
    for i in range(4):
      data.append(send_string(s, command[i]))  
  else:
    data.append('Robot is powered off')

  return data

# Parse received data into readable view
def parse_received_data_list():

  data = receive_data_list()

  if len(data) == 1:
    data = 'Robot is powered off'
  else:
    data[0] = data[0][-1]
    data[1] = data[1][0]
    if data[2][0] == 'No':
      data[2] = ' '.join(data[2])
    else:
      data[2] = re.findall(r'<?\w+>?.urp', data[2][-1])[0]
    data[3] = data[3][0]

  return data

# Update info in the main tk window
def tk_show_robot_data():

  data = parse_received_data_list()

  if type(data) is str:
    sn.config(text=data)
    timeout = 2000
  else:
    mode.config(text=data[0])
    sn.config(text=data[1])
    prog.config(text=data[2])
    state.config(text=data[3])
    timeout = 500

  window.after(timeout, tk_show_robot_data)
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

  # Create main window
  window = tk.Tk()
  window.title('Robot monitoring')
  window.resizable(False, False)

  # Create new window with log data
  def log_window():

    log = tk.Toplevel()
    log.title('Log')
    log.geometry('650x400')
    log.resizable(False, False)
    header_lbl = tk.Label(log, text='Robot log')
    text_box = tk.Text(log, height=log.winfo_screenmmheight() - 265, width=log.winfo_screenmmwidth())
    exit_btn = tk.Button(
      log, 
      text='Exit', 
      command=log.destroy, 
      relief='groove', 
      activebackground='lightgray'
      )

    # Insert new log data into window
    def read_data():

      with open('tmp.log', 'r') as l:
        data = l.readlines()
      text_box.delete(1.0, tk.END)
      text_box.insert(tk.END, ''.join(data))
      log.after(1000, read_data)

    header_lbl.pack()
    text_box.pack()
    exit_btn.pack(side='bottom')
    log.after(1000, read_data)
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
  quit_btn = tk.Button(
    window,
    text='Exit',
    command=window.destroy,
    relief='groove'
  )

  mode.pack()
  sn.pack()
  prog.pack()
  state.pack()
  log_btn.pack(side='left', expand=1, fill='x')
  quit_btn.pack(side='right', expand=1, fill='x')

  window.after(500, tk_show_robot_data)
  center_the_window(window)
  window.mainloop()