import pyautogui
import time

# (338, 150) - open file
# (590, 773) - save
# (771, 772) - ok

time.sleep(5)

for i in range(45, 72):
  pyautogui.moveTo(434, 254)
  pyautogui.leftClick()
  pyautogui.PAUSE = 0.5
  pyautogui.typewrite(f'{i}.pcx')
  pyautogui.keyDown('Enter')
  pyautogui.PAUSE = 0.5
  pyautogui.moveTo(590, 773)
  pyautogui.leftClick()
  pyautogui.PAUSE = 0.25
  pyautogui.typewrite(f'{i}')
  pyautogui.keyDown('Enter')
  pyautogui.PAUSE = 0.25
  pyautogui.moveTo(771, 772)
  pyautogui.leftClick()
  pyautogui.PAUSE = 0.25