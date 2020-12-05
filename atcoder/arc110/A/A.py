#!/usr/bin/env python3

def ok(x, N):
	for y in range(2, N+1):
		if x % y != 1: return False
	return True

import math

def lcm2(a, b):
	return a*b // math.gcd(a, b)

def lcm(lst):
	ret = 1
	for l in lst:
		ret = lcm2(ret, l)
	return ret

def ans(N):
	return 1 + lcm(range(1,N+1))

N = int(input())
print(ans(N))