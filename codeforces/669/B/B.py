#!/usr/bin/env pypy3

import math

def ans(A):
	old_A = A[:]

	A = [(e, i) for (i, e) in enumerate(A)]
	
	running_gcd = 0

	ret = []
	while len(A):
		A = sorted(A)[::-1]
		running_gcd = math.gcd(running_gcd, A[0][0])
		ret += [A[0][1]]
		A = [(math.gcd(running_gcd, e), i) for (e, i) in A]
		A = A[1:]

	ret = [old_A[i] for i in ret]
	print(*ret)


T = int(input())
for t in range(T):
	input()
	A = list(map(int, input().split()))
	ans(A)