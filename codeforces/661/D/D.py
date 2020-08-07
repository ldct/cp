#!/usr/bin/env pypy3

from sys import stdin, stdout
 
def input():
    return stdin.readline().strip()

def ans(S):

	num_0 = []
	num_1 = []

	ret = []

	for c in S:
		if c == '0':
			if len(num_1) == 0:
				# create new
				num_0 += [(len(num_0) + len(num_1))]
			else:
				num_0 += [num_1.pop()]

			ret += [num_0[-1] + 1]


		else:
			assert(c == '1')

			if len(num_0) == 0:
				# create new
				num_1 += [(len(num_0) + len(num_1))]
			else:
				num_1 += [num_0.pop()]

			ret += [num_1[-1] + 1]


	return len(num_0) + len(num_1), ret


	return S

T = int(input())
for t in range(T):
	input()
	S = input()
	
	p, q = ans(S)
	print(p)
	print(*q)
