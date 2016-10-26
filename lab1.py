#!/usr/bin/env python3
from random import choice
import string
for i in range(36):
    print(''.join(choice(string.ascii_lowercase + string.digits) for j in range(7)))
