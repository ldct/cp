#!/usr/bin/env pypy3

import random
N = 2*10**5
Q = 10**5
print(N, Q)
print(*[random.randint(1, 10**9) for _ in range(N)])
for _ in range(Q):
    l = random.randint(0, N-2)
    r = random.randint(l+1, N-1)
    print(l, r, random.randint(1, 10**9))