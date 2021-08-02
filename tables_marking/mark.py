# Generates program for laser.

with open('C:\\Users\\laser\\Desktop\\markirovka.lsc', 'w') as f:
  f.write('power 10\nspeed 500\nfreq 50\nvpa 0, 25\n\n')
  for i in range(1, 46):
    f.write(f'include "C:\\\\Users\\\\laser\\\\Documents\\\\Программы для маркировки\\\\румы\\\\{i}.VEC"\n\nsync 1\n')