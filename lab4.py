#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from string import ascii_lowercase
ABC = ascii_lowercase + ' '
while True :
    action = input('Кодировать - c, Декодировать - d, Выход - q: ')
    if (action != 'c') and (action != 'd') : break
    file_r = open('text.txt', 'r')
    line = file_r.readline().rstrip()
    file_r.close()
    file_w = open('text.txt', 'w')
    if action == 'c' :
        try : file_w.write( ''.join(ABC[(ABC.index(s) + 4) % 27] for s in line) + '\n')
        except ValueError : file_w.write(line + '\n')
    elif action == 'd' :
        try : file_w.write( ''.join(ABC[(ABC.index(s) - 4)] for s in line) + '\n')
        except ValueError : file_w.write(line + '\n')
    file_w.close()
