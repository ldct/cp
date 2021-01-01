#!/usr/bin/env pypy3

import itertools

def ok(S):
	for i in range(len(S)):
		s = S[i:i+3]
		if len(set(s)) < len(s): return False
	return True

def cost(a, b):
	pairs = zip(a, b)
	return len([1 for (p, q) in pairs if p != q])
def ans(A):
	candidates = itertools.product('abcd', repeat=len(A))
	candidates = [''.join(c) for c in candidates if ok(c)]
	return min(cost(c, A) for c in candidates)

for _ in range(int(input())):
	A = input()
	print(ans(A))