#!/usr/bin/env pypy3

import random

N = 2000

print(N, N)

for _ in range(N):
	print(''.join(random.choice("abcdefghijklmnopqrstuvwxyz") for _ in range(N)))