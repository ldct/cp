#!/usr/bin/env pypy3

from collections import Counter

def score(cN, target):
	ret1 = 0
	ret2 = 0
	for k in cN:
		if 2*k == target:
			ret1 += cN[k] // 2
		else:
			l = target - k
			ret2 += min(cN[k], cN[l])
	return ret1 + ret2//2

def ans(N):
	N = sorted(N)
	cN = Counter(N)

	return max(score(cN, target) for target in range(2, 101))

T = int(input())
for t in range(T):
	input()
	N = list(map(int, input().split()))
	
	print(ans(N))