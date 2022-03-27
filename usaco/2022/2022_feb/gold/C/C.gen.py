#!/usr/bin/env pypy3

import random

N = 10**5
print(N)
for _ in range(N):
    x = random.randint(0, 10**6)
    y = random.randint(0, 9)
    print(x, y)