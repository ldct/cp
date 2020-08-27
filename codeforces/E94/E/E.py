#!/usr/bin/env pypy3

from collections import Counter

from sys import stdin, stdout
 
def input():
    return stdin.readline().strip()

import operator as op
from functools import reduce

def ncr(n, r):
	if r > n: return 0

	r = min(r, n-r)
	numer = reduce(op.mul, range(n, n-r, -1), 1)
	denom = reduce(op.mul, range(1, r+1), 1)
	return numer // denom  # or / in Python 2

def ans_seg(A):	
	if len(A) == 0: return 0

	option1 = len(A)
	
	m = min(A)

	for i in range(len(A)):
		A[i] -= m

	option2 = m + ans(A)

	return min(option1, option2)

def ans(A):

	last_seg = []
	segs = []

	for a in A:
		if a == 0:
			segs += [last_seg]
			last_seg = []
		else:
			last_seg += [a]

	if len(last_seg):
		segs += [last_seg]

	return sum(ans_seg(seg) for seg in segs)

N = int(input())
S = list(map(int, input().split()))

print(ans(S))

for _ in range(1000):
	import random
	test_case = [random.randint(30, 40) for _ in range(50000)]
	print(ans(test_case))