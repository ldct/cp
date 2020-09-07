#!/usr/bin/env pypy3
	
from sys import stdin, stdout
 
def input():
    return stdin.readline().strip()

def ans(A):
	A = A[::-1]

	ret = float("-inf")
	s = 0
	for a in A:
		s += a
		ret = max(ret, s)

	return ret


T = int(input())
for t in range(T):
	input()
	A = list(map(int, input().split()))
	print(ans(A))
