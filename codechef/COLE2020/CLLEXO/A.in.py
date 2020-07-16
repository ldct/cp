#!/usr/bin/env pypy3

import random

N = 3*10**3
M = 3*10**3

print(1)
print(N, M)
for _ in range(N):
    print(''.join(random.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(M)))