#!/usr/bin/env pypy3

from sys import stdin, stdout
 
def input():
    return stdin.readline().strip()

import bisect

def choose(n, pA, cA, A, repeat_a, repeat_b):
	
	n -= 1
	ret = repeat_a

	i = bisect.bisect_left(A, -repeat_b)

	if (i == len(A) or -A[i] < repeat_a):
		n += 1
		i = min(i, n)
		return -pA[i] + (n-i)*repeat_b
	else:
		i = min(i, n)
		return -pA[i] + (n-i)*repeat_b + repeat_a

def ans(n, flowers):
	ret = float("-inf")
	A = [-a for (a, b) in flowers]
	A = sorted(A)
	pA = [0]
	for a in A:
		pA += [pA[-1] + a]
	for i in range(len(flowers)):
		ret = max(ret, choose(n, pA, None, A, flowers[i][0], flowers[i][1]))
	return ret

T = int(input())
for t in range(T):
	if t > 0: input()
	n, m = input().split(' ')
	n = int(n)
	m = int(m)
	flowers = []
	for _ in range(m):
		a, b = input().split(' ')
		a = int(a)
		b = int(b)
		flowers += [(a, b)]
	print(ans(n, flowers))