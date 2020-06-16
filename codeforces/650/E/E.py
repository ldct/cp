#!/usr/bin/env python3
	
from collections import Counter

def factors(n):
	ret = []
	for i in range(1, n+1):
		if n % i == 0:
			ret += [i]
	return ret

def ok(S, f, i):
	# its ok to split S into piles of height at least i
	numPiles = 0
	for s in S:
		numPiles += s // i
	return f <= numPiles

def maxCopies(S, f):
	for i in range(1, 10000000):
		if not ok(S, f, i):
			return i-1
	assert(False)

def ans(S, K):

	ret = float("-inf")

	for f in factors(K):
		ret = max(ret, f*maxCopies(S, f))
	
	return ret

T = int(input())
for t in range(T):
	N, K = input().split(' ')
	K = int(K)
	S = input()
	S = sorted(list(Counter(S).values()))[::-1]
	print(ans(S, K))