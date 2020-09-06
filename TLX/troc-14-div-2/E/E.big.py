#!/usr/bin/env pypy3

import random

N = 10**4
print(N)
print(*[random.randint(1,1) for _ in range(N)])
print(*([1]*N))
