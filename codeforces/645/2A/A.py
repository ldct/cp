#!/usr/bin/env python3

import math

T = int(input())

def ans(n, m):
	return math.ceil(n*m / 2)

for t in range(T):
	n, m = input().split(' ')
	n, m = int(n), int(m)

	print(ans(n, m))