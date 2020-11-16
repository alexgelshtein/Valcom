import pyautogui
import time
import openpyxl

time.sleep(5)

wb = openpyxl.load_workbook(filename='C:\\Users\\laser\\Documents\\Программы для маркировки\\таблички\\Номера.xlsx')
sheet = wb['Лист1']

for i in range(22, 29):
  vals = [sheet.cell(row=i, column=j).value for j in range(1, 6)]
  num = vals[0]
  name = vals[1]
  sn = vals[2]
  tag = vals[3]
  mass = vals[4]
  pyautogui.moveTo(853, 519)
  pyautogui.leftClick()
  pyautogui.doubleClick()
  pyautogui.doubleClick()
  pyautogui.typewrite(f'{name}')
  pyautogui.moveTo(742, 594)
  pyautogui.doubleClick()
  pyautogui.typewrite(f'{sn}')
  pyautogui.moveTo(1080, 732)
  pyautogui.doubleClick()
  pyautogui.typewrite(f'{mass}')
  pyautogui.moveTo(1086, 594)
  pyautogui.doubleClick()
  pyautogui.typewrite(f'{tag}')
  pyautogui.moveTo(901, 426)
  pyautogui.doubleClick()
  pyautogui.moveTo(27, 31)
  pyautogui.leftClick()
  pyautogui.moveTo(115, 386)
  pyautogui.leftClick()
  pyautogui.PAUSE = 0.5
  pyautogui.typewrite(f'{num}')
  pyautogui.keyDown('Enter')
  pyautogui.PAUSE = 0.25
  pyautogui.moveTo(870, 525)
  pyautogui.leftClick()
  pyautogui.moveTo(892, 545)
  pyautogui.leftClick()
  pyautogui.keyDown('Enter')
  pyautogui.PAUSE = 0.25