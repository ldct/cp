#!/usr/bin/env pypy3

import random

N = 10**7
S = ''.join(random.choice("()") for _ in range(N))
Q = 10**6
queries = [random.randint(1,N) for _ in range(Q)]
print(1)
print(S)
print(Q)
print(*queries)
