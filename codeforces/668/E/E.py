#!/usr/bin/env pypy3
	
from sys import stdin, stdout
 
def input():
    return stdin.readline().strip()

N, Q = input().split()
N = int(N)
Q = int(Q)

A = list(map(int, input().split()))

for _ in range(Q):
	x, y = input().split()
	x = int(x)
	y = int(y)

	ret = 0
	v = x+1
	for i in range(x, N-y):
		if v <= A[i] and A[i] <= i+1:
			ret += 1
		else:
			v += 1
	
	print(ret)
