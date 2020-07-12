#!/usr/bin/env python3

def ans(X, A):
	A = sorted(A)[::-1]

	i = 0
	ret = 0

	curr_length = 0
	curr_min = None
	
	while i < len(A):
		curr_length += 1
		curr_min = A[i]
		i += 1

		if curr_length*curr_min >= X:
			ret += 1
			curr_length = 0
			curr_min = None

	return ret

T = int(input())
for t in range(T):
	N, X = input().split(' ')
	N = int(N)
	X = int(X)
	A = input().split(' ')
	A = list(map(int, A))
	print(ans(X, A))