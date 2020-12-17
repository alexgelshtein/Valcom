# Generates program for laser.

with open('C:\\Users\\laser\\Desktop\\marker.lsc', 'w') as f:
  f.write('power 50\nspeed 1000\nfreq 50\n\n')
  for i in range(45, 72):
    f.write(f'include "C:\\\\Users\\\\laser\\\\Documents\\\\Программы для маркировки\\\\HSHI 11.11.2020\\\\{i}.VEC"\nsync 1\n\n')