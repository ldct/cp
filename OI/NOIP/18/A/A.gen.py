#!/usr/bin/env pypy3

import random

N = 10**4
print(N)
tc = list(range(N))[::-1]
# tc = [random.randint(1, 100) for _ in range(N)][::-1]
print(*tc)

# print(*list(range(N)))