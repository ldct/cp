#!/usr/bin/env pypy3

def rs(A):
	for i in range(len(A) - 1):
		if not (A[i] > A[i+1]):
			return False
	return True
	
def ans(A):
	if rs(A):
		return "NO"
	return "YES"

T = int(input())
for t in range(T):
	input()
	A = list(map(int, input().split()))
	print(ans(A))
