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

    soup = tk.Label(menu_window, text='Супы')
    selectedSoup = tk.StringVar(menu_window)
    soup1 = tk.Radiobutton(menu_window, text=menu[1][0], variable=selectedSoup, value=menu[1][0])
    soup2 = tk.Radiobutton(menu_window, text=menu[1][1], variable=selectedSoup, value=menu[1][1])
    soup3 = tk.Radiobutton(menu_window, text=menu[1][2], variable=selectedSoup, value=menu[1][2])
    soup.grid(column=0, row=0)
    soup1.grid(column=0, row=1, sticky='W')
    soup2.grid(column=0, row=2, sticky='W')
    soup3.grid(column=0, row=3, sticky='W')

    salad = tk.Label(menu_window, text='Салаты')
    selectedSalad = tk.StringVar(menu_window)
    salad1 = tk.Radiobutton(menu_window, text=menu[0][0], variable=selectedSalad, value=menu[0][0])
    salad2 = tk.Radiobutton(menu_window, text=menu[0][1], variable=selectedSalad, value=menu[0][1])
    salad3 = tk.Radiobutton(menu_window, text=menu[0][2], variable=selectedSalad, value=menu[0][2])
    salad4 = tk.Radiobutton(menu_window, text=menu[0][3], variable=selectedSalad, value=menu[0][3])
    salad.grid(column=0, row=4)
    salad1.grid(column=0, row=5, sticky='W')
    salad2.grid(column=0, row=6, sticky='W')
    salad3.grid(column=0, row=7, sticky='W')
    salad4.grid(column=0, row=8, sticky='W')

    main_dish = tk.Label(menu_window, text='Горячее')
    selectedMain = tk.StringVar(menu_window)
    main_dish1 = tk.Radiobutton(menu_window, text=menu[2][0], variable=selectedMain, value=menu[2][0])
    main_dish2 = tk.Radiobutton(menu_window, text=menu[2][1], variable=selectedMain, value=menu[2][1])
    main_dish3 = tk.Radiobutton(menu_window, text=menu[2][2], variable=selectedMain, value=menu[2][2])
    main_dish4 = tk.Radiobutton(menu_window, text=menu[2][3], variable=selectedMain, value=menu[2][3])
    main_dish5 = tk.Radiobutton(menu_window, text=menu[2][4], variable=selectedMain, value=menu[2][4])
    main_dish6 = tk.Radiobutton(menu_window, text=menu[2][5], variable=selectedMain, value=menu[2][5])
    main_dish7 = tk.Radiobutton(menu_window, text=menu[2][6], variable=selectedMain, value=menu[2][6])
    main_dish.grid(column=0, row=9)
    main_dish1.grid(column=0, row=10, sticky='W')
    main_dish2.grid(column=0, row=11, sticky='W')
    main_dish3.grid(column=0, row=12, sticky='W')
    main_dish4.grid(column=0, row=13, sticky='W')
    main_dish5.grid(column=0, row=14, sticky='W')
    main_dish6.grid(column=0, row=15, sticky='W')
    main_dish7.grid(column=0, row=16, sticky='W')

    side = tk.Label(menu_window, text='Гарнир')
    selectedSide = tk.StringVar(menu_window)
    side1 = tk.Radiobutton(menu_window, text=menu[3][0], variable=selectedSide, value=menu[3][0])
    side2 = tk.Radiobutton(menu_window, text=menu[3][1], variable=selectedSide, value=menu[3][1])
    side3 = tk.Radiobutton(menu_window, text=menu[3][2], variable=selectedSide, value=menu[3][2])
    side4 = tk.Radiobutton(menu_window, text=menu[3][3], variable=selectedSide, value=menu[3][3])
    side5 = tk.Radiobutton(menu_window, text=menu[3][4], variable=selectedSide, value=menu[3][4])
    side.grid(column=0, row=17)
    side1.grid(column=0, row=18, sticky='W')
    side2.grid(column=0, row=19, sticky='W')
    side3.grid(column=0, row=20, sticky='W')
    side4.grid(column=0, row=21, sticky='W')
    side5.grid(column=0, row=22, sticky='W')
    
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