#!/usr/bin/env pypy3

import random

N = 10**5
K = N-1
Z = 5

print(1)
print(N, K, Z)
print(' '.join(str(random.randint(1, 10**4)) for _ in range(N)))