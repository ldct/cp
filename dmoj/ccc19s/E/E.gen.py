#!/usr/bin/env pypy3

import io, os
from sys import stdin, stdout

import random
N = 3000
K = N//2
print(N, K)
for i in range(N):
    print(*[random.randint(10**8, 10**9) for _ in range(i+1)])