import openpyxl

wb = openpyxl.load_workbook(filename='C:\\Users\\laser\\Documents\\Программы для маркировки\\таблички\\Номера.xlsx')
sheet = wb['Лист1']

for i in range(2, 29):
  vals = [sheet.cell(row=i, column=j).value for j in range(1, 6)]
  name = vals[1]
  sn = vals[2]
  tag = vals[3]
  mass = vals[4]
  print(f'Name: {name}\nSerial number: {sn}\nTag: {tag}\nMass: {mass} kg\n')