#!/usr/bin/env pypy3

import random

print(1)
N = 100
K = 100
L = 109
print(N, K, L)

print(*[random.randint(1, 100) for _ in range(N)])