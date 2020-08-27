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

def ans_slow(N, A):
	ret = 0
	for i in range(N):
		for j in range(i+1, N):
			for k in range(j+1, N):
				for l in range(k+1, N):
					if A[i] == A[k] and A[j] == A[l]: ret += 1
	return ret

def ans_fast(N, A):
	cA = Counter(A)
	front = Counter()

	num_closes = [0]*(N+10)

	front_weight = []
	last = []

	for i in range(0, N+10):
		row = [0]*(N+10)
		front_weight += [row]
		row2 = [0]*(N+10)
		last += [row2]

	ret = 0

	for a in A:
		front[a] += 1
		for i in range(1, N+1):
			if a == i: continue
			
			front_weight[a][i] += last[a][i] * num_closes[a]

			back_weight = cA[i] - front[i]

			if front_weight[a][i] + back_weight > 0:
				# if (a, i) == (1, 3): print("contrib", a, i, front_weight[a][i], back_weight)
				ret += front_weight[a][i]*back_weight

			last[a][i] = 0
			last[i][a] += 1
		
		num_closes[a] += 1

	for k in cA:
		v = cA[k]
		ret += ncr(v, 4)


	return ret
			

def ans(N, A):
	return ans_fast(len(A), A)

T = int(input())
for t in range(T):
	N = int(input())
	S = list(map(int, input().split()))

	print(ans(N, S))