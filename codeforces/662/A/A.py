#!/usr/bin/env pypy3

import math

def ans(N):
	return N//2 + 1


T = int(input())
for t in range(T):
	N = int(input())
	print(ans(N))
