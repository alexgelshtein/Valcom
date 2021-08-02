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
    box1 = tk.Listbox(menu_window, selectmode=tk.MULTIPLE, height=3, width=80, exportselection=0)
    for v in menu[1]:
      box1.insert(tk.END, v)
    box1.grid(column=0, row=1)
    
    salad = tk.Label(menu_window, text='Салаты').grid(column=0, row=4)
    selectedSalad = tk.StringVar(menu_window)
    box2 = tk.Listbox(menu_window, selectmode=tk.MULTIPLE, height=4, width=80, exportselection=0)
    for v in menu[0]:
      box2.insert(tk.END, v)
    box2.grid(column=0, row=5)
    
    main_dish = tk.Label(menu_window, text='Горячее').grid(column=0, row=9)
    selectedMain = tk.StringVar(menu_window)
    box3 = tk.Listbox(menu_window, selectmode=tk.MULTIPLE, height=7, width=80, exportselection=0)
    for v in menu[2]:
      box3.insert(tk.END, v)
    box3.grid(column=0, row=10)
    
    side = tk.Label(menu_window, text='Гарнир').grid(column=0, row=17)
    selectedSide = tk.StringVar(menu_window)
    box4 = tk.Listbox(menu_window, selectmode=tk.MULTIPLE, height=5, width=80, exportselection=0)
    for v in menu[3]:
      box4.insert(tk.END, v)
    box4.grid(column=0, row=18)
    
    def ok():
      order = []
      for i in box1.curselection():
        order.append(box1.get(i))
      for i in box2.curselection():
        order.append(box2.get(i))
      for i in box3.curselection():
        order.append(box3.get(i))
      for i in box4.curselection():
        order.append(box4.get(i))
      if len(order) > 0 and len(order) < 5:
        print(order)
      else:
        print('Пожалуйста, выберите блюда снова')
      menu_window.quit()
    b = tk.Button(menu_window, text='Готово', command=ok)
    b.grid(column=0, row=23)

  btn = tk.Button(root, text='Ок', command=clicked)
  btn.grid(column=0, row=2)

  root.mainloop()

if __name__ == "__main__":
  main()