#!/usr/bin/env pypy3

from sys import stdin, stdout

def input():
    return stdin.readline().strip()


def ans(A):
	A = sorted(A)
	ret = set()
	for a in A:
		if not (a in ret):
			ret.add(a)
		elif not ((a+1) in ret):
			ret.add(a+1)
	return len(ret)

for _ in range(int(input())):
	input()
	A = list(map(int, input().split()))
	print(ans(A))