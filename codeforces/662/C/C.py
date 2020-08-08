#!/usr/bin/env pypy3

from sys import stdin, stdout
 
def input():
    return stdin.readline().strip()

from collections import defaultdict, Counter

def ans(A):
	cA = Counter(A)
	max_freq = max(cA.values())

	ret = -1
	fodder = 0

	for c in cA:
		if cA[c] == max_freq:
			ret += 1
		else:
			fodder += cA[c]

	max_freq -= 1
	assert(max_freq >= 0)

	return ret + (fodder // max_freq)

T = int(input())
for _ in range(T):
	input()
	A = list(map(int, input().split()))
	print(ans(A))