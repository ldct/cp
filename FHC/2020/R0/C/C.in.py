#!/usr/bin/env pypy3

N = 800000
bounds = 500000000

import random

print(1)
print(N)
for _ in range(N):
	P = random.randint(-bounds, bounds)
	H = random.randint(1, bounds)
	print(P, H)
