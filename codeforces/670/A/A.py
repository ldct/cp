#!/usr/bin/env pypy3

from collections import Counter

def mex(A):
	sA = set(A)
	for i in range(0, 200):
		if i not in sA:
			return i
			
def ans(A):
	cA = Counter(A)
	A = []
	B = []
	for i in range(0, 200):
		if cA[i] >= 2:
			A += [i]
			B += [i]
		elif cA[i] == 1:
			B += [i]

	return mex(A) + mex(B)

T = int(input())
for t in range(T):
	input()
	A = list(map(int, input().split()))
	print(ans(A))
