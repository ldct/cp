#!/usr/bin/env pypy3

for _ in range(int(input())):
	N = int(input())
	ret = -1
	for _ in range(N):
		ret = max(ret, int(input()))
	print(ret)