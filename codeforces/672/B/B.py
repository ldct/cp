#!/usr/bin/env pypy3

from collections import Counter

def ans(A):
	A = [len("{0:b}".format(a)) for a in A]
	cA = Counter(A)

	ret = 0

	for k in cA:
		v = cA[k]
		ret += (v*(v-1))//2
	return ret

T = int(input())
for t in range(T):
	input()
	A = list(map(int, input().split()))
	print(ans(A))
