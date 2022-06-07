#!/usr/bin/env pypy3

import random

N = 3*10**5
tc = [random.randint(1, 1.5*10**7) for _ in range(N)]
print(N)
print(*tc)