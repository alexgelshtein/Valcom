import openpyxl

wb = openpyxl.load_workbook(filename='C:\\Users\\laser\\Documents\\Программы для маркировки\\metal_labels_15811.5.xlsx')
sheet = wb['Sheet1']

with open('C:\\Users\\laser\\Desktop\\tables.lsc', 'w') as f:
  f.write('power 50\nspeed 500\nfreq 50\nvpa 0, 0\n\nttfont "Times New Roman", 3.5, 3, 20\n\n')
  for i in range(2, 33):
    vals = [sheet.cell(row=i, column=j).value for j in range(2, 3)]
    f.write(f'setblock 1\ntext "{vals[0]}"\nbreakonlast\nvpr 0, -45\nendblock\n\nsync 1\nblock 1, 2\nvpr 0, 45\n\n')