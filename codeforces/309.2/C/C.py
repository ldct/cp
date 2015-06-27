#!/usr/bin/env python3

from collections import defaultdict
from copy import deepcopy

k = int(input())
c = [int(input()) for i in range(k)]

def max_candidate(candidate, start=k):
	for c in range(start, 0, -1):
		if candidate[c] > 0:
			return c

def min_candidate(candidate):
	for c in range(1, k+1):
		if candidate[c] > 0:
			return c

def len_candidate(candidate):
	ret = 0
	for k in candidate:
		ret += candidate[k]
	return ret

def ways(prefix, candidates):
	if len_candidate(candidates) == 0:
		return [prefix]
	if len(prefix) == 0:
		mx = max_candidate(candidates)
		candidates[mx] -= 1
		return ways([mx], candidates)
	if 1 not in prefix:
		last = prefix[-1]
		last_s = last - 1
		# next one can be either last or last_s
		ret = []
		if candidates[last] > 0:
			new_candidates = deepcopy(candidates)
			new_candidates[last] -= 1
			ret += ways(prefix + [last], new_candidates)

		if candidates[last_s] > 0:
			new_candidates = deepcopy(candidates)
			new_candidates[last_s] -= 1
			ret += ways(prefix + [last_s], new_candidates)
		return ret
	else:
		ret = []
		for c in candidates:
			if candidates[c] > 0:
				new_candidates = deepcopy(candidates)
				new_candidates[c] -= 1
				ret += ways(prefix + [c], new_candidates)
		return ret


candidates = defaultdict(int)
for i, n in enumerate(c):
	candidates[i+1] = n


W = ways([], candidates)
print(len(W))

from itertools import permutations
for w in permutations(W[0]):
	first_one = w.index(1)
	print(w, w[0:first_one + 1])