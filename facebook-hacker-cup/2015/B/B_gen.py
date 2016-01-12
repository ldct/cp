#!/usr/bin/env python3

from random import randint

T = 40

print(T)
for _ in range(T):
	N = 100000
	P = 1000000000
	a = 1
	b = 1000000000
	print(N, P)
	print(' '.join(str(randint(a, b)) for i in range(N)))