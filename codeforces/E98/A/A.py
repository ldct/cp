#!/usr/bin/env pypy3

def ans(x, y):
	m = min(x, y)
	ret = 2*min(x, y)
	x -= m
	y -= m
	rest = x+y
	if rest == 0:
		return ret
	return ret + 2*rest - 1

T = int(input())
for _ in range(T):
	[x, y] = input().split()
	print(ans(int(x), int(y)))