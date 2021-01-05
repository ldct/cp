#!/usr/bin/env pypy3

from heapq import *

from sys import stdin, stdout

def input():
    return stdin.readline().strip()

def fits(small, large):
	(sx, sy) = small
	(lx, ly) = large

	return sx < lx and sy < ly

def fits2(small, large):
	(sx, sy) = small
	(lx, ly) = large

	return fits(small, large) or fits((sy, sx), large) or fits(small, (ly, lx)) or fits((sy, sx), (ly, lx))

def ans(friends):
	friends = [tuple(sorted([x, y])[::-1]) for (x, y) in friends]
	ret = [-1]*len(friends)
	friends = [(f, i) for i, f in enumerate(friends)]
	friends = sorted(friends)

	# friends is now in increasing fatness

	candidates = []

	lazy = []
	last_fatness = -1

	for (y, x), i in friends:

		if y > last_fatness:
			for l in lazy:
				heappush(candidates, l)
			lazy = []

		# print(f"when considering {i} the candidates are {candidates}" )
		if len(candidates):
			best = candidates[0]
			(bx, bi) = best
			if bx < x:
				ret[i] = bi+1

		lazy += [(x, i)]

		last_fatness = y

	return ret

def ans_slow(friends):
	ret = []
	for sz in friends:
		res = -1
		for i in range(len(friends)):
			if fits2(friends[i], sz):
				res = i+1
				break
		ret += [res]
	return ret

# tc = [(9, 5), (9, 7), (6, 8)]
# print(ans_slow(tc))
# print(ans(tc))

# import random
# for _ in range(10000):
# 	N = 5
# 	testcase = [(random.randint(1, 10), random.randint(1, 10)) for _ in range(N)]

# 	slow = ans_slow(testcase)
# 	fast = ans(testcase)

# 	for i in range(len(slow)):
# 		if slow[i] == -1:
# 			if not (fast[i] == -1):
# 				print(testcase)
# 		else:
# 			if not (fast[i] != -1):
# 				print(testcase)

for _ in range(int(input())):
	N = int(input())
	friends = []
	for _ in range(N):
		[h, w] = list(map(int, input().split()))
		friends += [tuple(sorted([h, w])[::-1])]
	print(*ans(friends))