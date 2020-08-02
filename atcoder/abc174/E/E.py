#!/usr/bin/env pypy3

import math

def num_cuts(A, ml):
	ret = 0
	for a in A:
		ret += (math.ceil(a / ml) - 1)
	return ret

def ok(A, ml):
	return num_cuts(A, ml) <= K

def ans(A, K):

	low = min(A) / (K+5)
	high = max(A)+1

	assert(not(ok(A, low)))
	assert(ok(A, high))

	while (high - low) > 0.1:
		mid = (low + high) / 2
		if ok(A, mid):
			high = mid
		else:
			low = mid

	low = max(1, math.floor(low) - 5)

	for i in range(100):
		p = low + i/2
		if ok(A, p):
			return math.ceil(p)

	assert(False)


N, K = input().split()
N = int(N)
K = int(K)

A = list(map(int, input().split()))

print(ans(A, K))