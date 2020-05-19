#!/usr/bin/env python3

import math

T = int(input())

def ans(n):
	r = 1 / (2*math.sin(math.pi/(2*n)))
	if n % 2 == 1:
		return 2*r*math.cos(math.pi / (4*n))
	return 2*math.sqrt(r*r - 0.25)

for t in range(T):
	n = int(input())
	print(ans(n))