#!/usr/bin/env pypy3

from sys import stdin, stdout
 
def input():
    return stdin.readline().strip()

N, D = input().split()
N = int(N)
D = int(D)
DD = D**2
ret = 0
for _ in range(N):
	x, y = input().split()
	x = int(x)
	y = int(y)
	dd = x*x + y*y
	if dd <= DD:
		# print(x, y)
		ret += 1
print(ret)