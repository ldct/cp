#!/usr/bin/env pypy3

def next(c):
	if c == "b": return "c"
	return "b"

def ans(A):
	ret = ["a"*60]
	for p in A:
		last = ret[-1]
		last = list(last)
		last[p] = next(last[p])
		ret += [''.join(last)]

	for s in ret:
		print(s)

T = int(input())

for _ in range(T):
	input()
	A = input().split(' ')
	A = list(map(int, A))
	ans(A)