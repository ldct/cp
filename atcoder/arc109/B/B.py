#!/usr/bin/env pypy3

from math import floor, isqrt
import sys

def ok(n, k):
	return n*(n+1) <= (n - k + 2)*(n + k + 1)

def ans(n):
	k = (isqrt(8*n + 9) + 1) // 2
	return n + 2 - floor(k)

N = int(input())
print(ans(N))
