#!/usr/bin/env python3

from random import randint

N = 200000
print(N)
print(' '.join(str(randint(2, N)) for i in range(N)))