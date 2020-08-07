#!/usr/bin/env pypy3

def ans(A):
	A = sorted(A)

	for i in range(len(A)-1):
		if abs(A[i] - A[i+1]) > 1: return "NO"
	return "YES"

	return A

T = int(input())
for t in range(T):
	input()
	A = list(map(int, input().split()))
	print(ans(A))