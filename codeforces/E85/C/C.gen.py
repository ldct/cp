#!/usr/bin/env pypy3

import random

T = 150000
N = 2
print(T)
for _ in range(T):
    print(N)
    for _ in range(N):
        a = random.randint(1, 10**12)
        b = random.randint(1, 10**12)
        print(a, b)