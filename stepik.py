from bs4 import BeautifulSoup
import requests

url = 'http://piter-lanch.ru/menu/set_lunch.php?date=10.03.2021'

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
  print(filteredMenu[i])