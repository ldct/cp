#!/usr/bin/env pypy3

def ans(A, x):
	if A == sorted(A): return 0
	i = 0
	ret = 0
	while i < len(A) and A != sorted(A):
		if x < A[i]:
			ret += 1
			x, A[i] = A[i], x
			i += 1
		else:
			i += 1
			continue
	if A == sorted(A):
		return ret
	return -1

T = int(input())
for _ in range(T):
	_, x = input().split()
	x = int(x)
	A = list(map(int, input().split()))
	print(ans(A, x))
