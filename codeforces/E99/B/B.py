#!/usr/bin/env pypy3

def in_reachable(t, n):
	largest = n*(n+1)//2
	if t > largest: return False
	if t == largest: return True
	if t == largest-1: return False
	if t < largest - 1: return True
	assert(False)

def ans(n):
	for i in range(1, 2*n):
		if in_reachable(n, i):
			return i

T = int(input())
for _ in range(T):
	print(ans(int(input())))
