#!/usr/bin/env pypy3

def ans(A):
	ret = set()
	for a in A:
		for b in A:
			if b > a:
				ret.add(abs(b-a))
	return len(ret)

for _ in range(int(input())):
	input()
	A = list(map(int, input().split()))
	print(ans(A))