#!/usr/bin/env python3

N = int(input())
A = list(map(int, input().split(' ')))

def rotate(A):
	return [(a + (-1)**i) % N for i, a in enumerate(A)]

def ok(A):
	while True:
		A = rotate(A)
		if A[0] == 0:
			return A == list(range(N))

if ok(A):
	print('Yes')
else:
	print('No')