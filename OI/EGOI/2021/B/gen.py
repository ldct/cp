#!/usr/bin/env pypy3

import random

N = 500000
A = []
for i in range(N):
    A += [i+1, i+1]
random.shuffle(A)
print(N)
print(*A)