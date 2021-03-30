# Generates program for laser.

with open('C:\\Users\\laser\\Desktop\\markirivka.lsc', 'w') as f:
  f.write('power 10\nspeed 500\nfreq 50\nvpa 0, 25\n\n')
  for i in range(45, 72, 2):
    f.write(f'include "C:\\\\Users\\\\laser\\\\Documents\\\\Программы для маркировки\\\\таблички\\\\{i}.VEC"\nvpr 0, -45\ninclude "C:\\\\Users\\\\laser\\\\Documents\\\\Программы для маркировки\\\\таблички\\\\{i+1}.VEC"\nvpr 0, 45\n\nsync 1\n')