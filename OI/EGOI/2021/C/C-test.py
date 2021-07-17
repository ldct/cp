#!/usr/bin/env pypy3

def fprint(*args):
	print(*args, flush=True)

### CODE HERE

from itertools import chain, combinations

def ss(B):

	if not sum(B) % 2 == 0: return False
	target = sum(B) // 2

	import array
	possible = array.array('b', [1] + [0]*target)

	for b in B:
		next_possible = array.array('b', possible)
		for i in range(len(possible)):
			if possible[i] != 1: continue
			if i + b > target: continue
			if target == i + b:
				return True
			if i + b < target:
				next_possible[i+b] = 1
		possible = next_possible

	return False

def subsets(iterable, low=0, high=None):
    "subsets([1,2,3]) --> () (1,) (2,) (3,) (1,2) (1,3) (2,3) (1,2,3)"
    s = list(iterable)
    if high is None:
        high = len(s)
    return chain.from_iterable(combinations(s, r) for r in range(low, high+1))

def get_ss(B):
	for ss in subsets(B):
		if sum(ss) == sum(B)//2: return ss
	return False

def ok(B):
	if len(B) <= 1: return False
	if sum(B) % 2 != 0: return False
	if ss(B):
		assert(get_ss(B))
		return True
	return False

def tries(N):
	import random
	B = []
	low = 1
	while True:
		if ok(B):
			return B
		B += [random.randrange(low, low+N)]
		low += N

def avg_tries(N):
	sample = [len(tries(N)) for _ in range(100)]
	return sum(sample)/len(sample)

for N in [1, 2, 25, 200, 1000, 5000]:
	print(N, avg_tries(N))