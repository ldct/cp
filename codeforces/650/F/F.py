#!/usr/bin/env python3
	
def ans(A):
	if len(A) == 0: return 0
	if A[0] == min(A): return 1 + ans(A[1:])
	if A[-1] == max(A): return 1 + ans(A[0:len(A)-1])

	A.remove(min(A))

	return 1 + ans(A)


T = int(input())
for t in range(T):
	input()
	A = input().split(' ')
	A = [int(x) for x in A]
	print(ans(A))