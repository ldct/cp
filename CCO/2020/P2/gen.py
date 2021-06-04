#!/usr/bin/env pypy3

import random

N = 100
print(N)
print(*[random.randint(N//2, N) for _ in range(N)])