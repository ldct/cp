#!/usr/bin/env pypy3

import math

from sys import stdin, stdout
 
def input():
    return stdin.readline().strip()	

def ans(N, K, a, b, c, d):
	i1 = (a, b)
	i2 = (c, d)
	[i1, i2] = sorted([i1, i2])
	(a, b) = i1
	(c, d) = i2

	curr_intersection = max(0, b - c)
	if curr_intersection * N >= K:
		return 0

	K -= curr_intersection*N
	assert(K > 0)

	matchcost = 0

	if b < c:
		matchcost += c-b
		if b-a > d-c:
			# extend b
			b = c
		else:
			# extend c
			c = b

	front = c - a
	assert(front >= 0)
	back = abs(d - b)
	cheap = front+back

	# from now on, you can pay `matchcost` on a pair to activate them, after which
	# you can work up to `cheap` from them

	# do a match
	spent = matchcost
	N -= 1

	# work cheap
	if cheap >= K:
		return spent+K
	else:
		K -= cheap
		spent += cheap

	# now you also can always pay 2
	# print(cheap, matchcost)
	# if (cheap) / (cheap + matchcost) > 2:
	# 	print('hi')
	# 	return spent+2*K

	# num_activations = math.ceil(K / cheap)
	# if (num_activations <= N):
	# 	return spent+K+matchcost*num_activations

	# return '?'

	while True:
		if N == 0: return spent+2*K
		if 2*K <= matchcost:
			return spent+2*K

		# print("matching")
		N -= 1
		spent += matchcost

		if cheap >= K:
			return spent + K
		
		K -= cheap
	

T = int(input())

for _ in range(T):
	N, K = input().split(' ')
	N = int(N)
	K = int(K)
	a, b = input().split(' ')
	a = int(a)
	b = int(b)
	c, d = input().split(' ')
	c = int(c)
	d = int(d)
	print(ans(N, K, a, b, c, d))