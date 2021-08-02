# Saves table images to proper format for marking.

import pyautogui
import time

# (238, 281) - open file
# (592, 774) - save
# (769, 775) - ok

time.sleep(5)

for i in range(1, 46):
  pyautogui.moveTo(238, 281)
  pyautogui.leftClick()
  pyautogui.PAUSE = 0.5
  pyautogui.typewrite(f'{i}.pcx')
  pyautogui.keyDown('Enter')
  pyautogui.PAUSE = 0.5
  pyautogui.moveTo(592, 774)
  pyautogui.leftClick()
  pyautogui.PAUSE = 0.25
  pyautogui.typewrite(f'{i}')
  pyautogui.keyDown('Enter')
  pyautogui.PAUSE = 0.25
  pyautogui.moveTo(769, 775)
  pyautogui.leftClick()
  pyautogui.PAUSE = 0.25