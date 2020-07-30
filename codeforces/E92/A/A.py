#!/usr/bin/env pypy3

from sys import stdin, stdout
 
def input():
    return stdin.readline().strip()

T = int(input())

for _ in range(T):
	l, r = input().split(' ')
	l = int(l)
	r = int(r)
	
	if 2*l <= r:
		print(l, 2*l)
	else:
		print(-1, -1)
