#!/usr/bin/env pypy3

def ans(A):
	N = len(A)
	max_amax = sum(A) / (N-1)
	if max(A) <= max_amax:
		N -= 1
		if sum(A)%N == 0: return 0
		return N - (sum(A) % N)
	return max(A)*(N-1) - sum(A)

T = int(input())
for _ in range(T):
	input()
	A = list(map(int, input().split()))
	print(ans(A))
