#!/usr/bin/env pypy3

import random

N = random.randint(10, 20)
Q = 200
X = random.randint(1, N)

P = list(range(1, N+1))
random.shuffle(P)

print(N, Q, X)
print(*P)
for _ in range(Q):
    c = random.randint(1, 2)
    l = random.randint(1, N)
    r = random.randint(l, N)
    print(c, l, r)