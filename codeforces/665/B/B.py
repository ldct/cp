#!/usr/bin/env pypy3

def ans(A, B):
	ret = 0
	pos_match = min(A[2], B[1])
	A[2] -= pos_match
	B[1] -= pos_match
	ret += 2*pos_match

	assert(sum(A) == sum(B))
	N = sum(A)

	x = B[2]
	y = A[1]

	neg_match = (x + y) - N
	if neg_match > 0:
		ret -= 2*neg_match

	return ret

T = int(input())
for t in range(T):
	A = input().split()
	A = list(map(int, A))

	B = input().split()
	B = list(map(int, B))

	print(ans(A, B))