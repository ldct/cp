#!/usr/bin/env python3

def ans(A, x):
	if sum(A) % x != 0:
		return len(A)
	for i in range(len(A)):
		if A[i] % x != 0: break
		if A[len(A)-i-1] % x != 0: break
	if len(A)-i-1 == 0:
		return -1
	return len(A)-i-1

T = int(input())
for t in range(T):
	n, x = input().split(' ')
	x = int(x)
	A = input().split(' ')
	A = [int(x) for x in A]

	print(ans(A, x))