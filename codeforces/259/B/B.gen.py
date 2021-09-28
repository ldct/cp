#!/usr/bin/env pypy3

import random

N = 10
print(N)
tc = [random.randint(1, 30) for _ in range(N)]
print(*tc)