#!/usr/bin/env pypy3

import random

N = 3
M = 10**6

print(N, M)

for _ in range(N):
    print(''.join(random.choice("01") for _ in range(M)))