#!/usr/bin/env pypy3
	
import math

def ceil(a, b):
	return -(-a // b)

def ans(x, y, k):
	p = k+k*y
	return ceil((p-1), (x-1)) + k

T = int(input())
for t in range(T):
	x, y, k = input().split()
	x = int(x)
	y = int(y)
	k = int(k)
	print(ans(x,y,k))