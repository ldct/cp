#!/usr/bin/env pypy3

def score(A):
	ret = 0
	rs = 0
	for a in A:
		rs += a
		ret = max(ret, rs)
	return ret

def ans(A, B):
	return score(A) + score(B)

for _ in range(int(input())):
	input()
	A = list(map(int, input().split()))
	input()
	B = list(map(int, input().split()))
	print(ans(A, B))