#!/usr/bin/env python3

T = int(input())

def ans(A):
	A = sorted(A)
	seq = range(1, len(A) + 1)

	for a, b in reversed(list(zip(A, seq))):
		if b >= a:
			return b+1
	return 1

for t in range(T):
	n = input()
	A = input().split(' ')
	A = [int(x) for x in A]

	print(ans(A))