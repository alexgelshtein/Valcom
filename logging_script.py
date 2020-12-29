from robot_monitoring_app import *
import logging
import time
import sys

def update_log():

  logging.basicConfig(
    filename='tmp.log', 
    filemode='w', 
    level=logging.INFO, 
    format='%(asctime)s - [%(levelname)s] - %(message)s', 
    datefmt='%d-%b-%y %H:%M:%S'
    )
    
  old_data = None

  while True:
    try:
      new_data = parse_received_data_list()
      if new_data != old_data:
        if type(new_data) is str:
          logging.warn('Robot is powered off')
        else:
          if new_data[2] != 'No program loaded':
            logging.info(f'{new_data[2]} is loaded ({new_data[3]})')
          else:
            logging.info(new_data[2])
      old_data = new_data
      time.sleep(1.0)
    except KeyboardInterrupt:
      print('\n...Program stopped manually')
      sys.exit()

if __name__ == "__main__":
  
  update_log()