from bs4 import BeautifulSoup
import requests
import tkinter as tk
from tkinter.ttk import Combobox
import datetime

def get_menu(date):

  url = 'http://piter-lanch.ru/menu/set_lunch.php?date=' + date

  page = requests.get(url)

  print(page.status_code)

  menu = [[] for i in range(4)]
  filteredMenu = [[] for i in range(4)]

  soup = BeautifulSoup(page.text, 'html.parser')
  for i in range(4):
    menu[i] = soup.findAll('tr', class_=f'rubrika{i}')
    for item in menu[i]:
      if item.find('td', class_='menutab3') is not None:
        filteredMenu[i].append(item.text.strip())

  return filteredMenu

def main():

  root = tk.Tk()

  root.geometry('200x100')
  root.title('Заказ обедов')
  lbl = tk.Label(root, text='Выберите дату:')
  lbl.grid(column=0, row=0)

  combo = Combobox(root)
  vals = []

  for i in range(1, 7):
    day = datetime.date.today() + datetime.timedelta(i)
    if day.weekday() not in [5, 6]:
      vals.append(day.strftime('%d.%m.%Y'))
  
  combo['values'] = vals
  combo.current(0)
  combo.grid(column=0, row=1)

  def clicked():
    date = combo.get()
    menu = get_menu(date)
    menu_window = tk.Tk()
    menu_window.geometry('600x750')
    menu_window.title(f'Меню на {date}')

    soup = tk.Label(menu_window, text='Супы').grid(column=0, row=0)
    selectedSoup = tk.StringVar(menu_window)
    for i in range(3):
      tk.Radiobutton(menu_window, text=menu[1][i], variable=selectedSoup, value=menu[1][i]).grid(column=0, row=i+1, sticky='W')

    salad = tk.Label(menu_window, text='Салаты').grid(column=0, row=4)
    selectedSalad = tk.StringVar(menu_window)
    for i in range(4):
      tk.Radiobutton(menu_window, text=menu[0][i], variable=selectedSalad, value=menu[0][i]).grid(column=0, row=i+5, sticky='W')

    main_dish = tk.Label(menu_window, text='Горячее').grid(column=0, row=9)
    selectedMain = tk.StringVar(menu_window)
    for i in range(7):
      tk.Radiobutton(menu_window, text=menu[2][i], variable=selectedMain, value=menu[2][i]).grid(column=0, row=i+10, sticky='W')

    side = tk.Label(menu_window, text='Гарнир').grid(column=0, row=17)
    selectedSide = tk.StringVar(menu_window)
    for i in range(5):
      tk.Radiobutton(menu_window, text=menu[3][i], variable=selectedSide, value=menu[3][i]).grid(column=0, row=i+18, sticky='W')
    
    def ok():
      print(selectedSoup.get())
      print(selectedSalad.get())
      print(selectedMain.get())
      print(selectedSide.get())
      menu_window.quit()
    b = tk.Button(menu_window, text='Готово', command=ok)
    b.grid(column=0, row=23)

  btn = tk.Button(root, text='Ок', command=clicked)
  btn.grid(column=0, row=2)

  root.mainloop()

if __name__ == "__main__":
  main()