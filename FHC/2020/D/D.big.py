#!/usr/bin/env pypy3

import random

N = 10**6
M = 10**3

print(1)
print(N, M)
for _ in range(N):
	print(random.choice([0, random.randint(0, 10**9)]))