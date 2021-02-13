#!/usr/bin/env pypy3

from sys import stdin, stdout

def input():
    return stdin.readline().strip()

def ans(A, B):
	A = sorted(A)
	B = sorted(B)[::-1]

	advantage = sum(B) - sum(A)
	ret = 0
	N = min(len(A), len(B))
	i = 0

	while True:
		if advantage < 0: break
		if i == N: return -1

		advantage -= 2*B[i]
		advantage += 2*A[i]
		i += 1
		ret += 1

		if advantage < 0: break
		if i == N: return -1


	return ret



	return A, B

for _ in range(int(input())):
	input()
	A = list(map(int, input().split()))
	B = list(map(int, input().split()))
	print(ans(A, B))
