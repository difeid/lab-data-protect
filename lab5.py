#!/usr/bin/env python3
file_r = open('encrypt1.txt', 'r', encoding='iso8859-1')
file_w = open('open.txt', 'w')
text = file_r.read()
file_r.close()
for s in text :
    r = ord(s)-19
    if r < 0 : r = 256+r
    sim=str(bytes([r]).decode('cp866'))
    if ord(sim) == 1118 : sim = '\n' #костыль из-за кодировок
    file_w.write(sim)
file_w.close()
