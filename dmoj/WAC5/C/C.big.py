#!/usr/bin/env pypy3

import random

N = 2*10**5
B = [random.randint(1, 5) for _ in range(N)]

print(N)
print(*B)