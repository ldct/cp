#!/usr/bin/env pypy3
	
T = int(input())
for t in range(T):
	input()
	P = input().split()
	print(*(P[::-1]))