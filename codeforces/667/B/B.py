#!/usr/bin/env pypy3

import math

def ans2(a,b,x,y,n):
	gap = a-x
	a -= min(n, gap)
	n -= min(n, gap)

	gap = b-y
	b -= min(n, gap)
	n -= min(n, gap)

	return a*b

def ans(a,b,x,y,n):
	return min(ans2(a,b,x,y,n), ans2(b,a,y,x,n))


T = int(input())
for t in range(T):
	A, B, X, Y, N = input().split()
	A = int(A)
	B = int(B)
	X = int(X)
	Y = int(Y)
	N = int(N)

	print(ans(A,B,X,Y,N))