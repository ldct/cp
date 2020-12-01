#!/usr/bin/env pypy3

T = int(input())
for _ in range(T):
	x, y = input().split()
	x = int(x)
	y = int(y)
	print(x-1, y)
