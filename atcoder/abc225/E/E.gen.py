#!/usr/bin/env pypy3

import random

N = 2*10**5
print(N)

for _ in range(N):
    x = random.randint(1, 10**9)
    y = random.randint(1, 10**9)

    print(x, y)