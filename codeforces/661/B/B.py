#!/usr/bin/env pypy3

def ans(A, B):

	ma = min(A)
	mb = min(B)

	ret = 0

	for a, b in zip(A, B):
		ret += max(a - ma, b - mb)

	return ret

T = int(input())
for t in range(T):
	input()
	A = list(map(int, input().split()))
	B = list(map(int, input().split()))

	print(ans(A, B))