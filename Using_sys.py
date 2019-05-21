#!/usr/bin/env python3
import sys

print('Аргументы командной строки:')
for i in sys.argv:
    print(i)

print('\n\nпеременная PYTHONPATH содержит',sys.path,'\n')
