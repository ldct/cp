#!/usr/bin/env python

from itertools import *
from collections import *

def powerset(iterable):
    s = list(iterable)
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

T = int(raw_input())

def is_ok(schedule, K):

	# jp

	c_jp_combos = Counter([(j, p) for (j, p, s) in schedule])
	if len(c_jp_combos) and max(c_jp_combos.values()) > K:
		return False

	# js

	c_js_combos = Counter([(j, s) for (j, p, s) in schedule])
	if len(c_js_combos) and max(c_js_combos.values()) > K:
		return False

	# ps

	c_ps_combos = Counter([(p, s) for (j, p, s) in schedule])
	if len(c_ps_combos) and max(c_ps_combos.values()) > K:
		return False

	return True

def ans(J, P, S, K):
	if K >= 3:
		return [(j, p, s) for j in range(1, J+1) for p in range(1, P+1) for s in range(1, S+1)]
	# if (J, P, S) == (3, 3, 3):
	# 	return []

	outfits = [(j, p, s) for j in range(1, J+1) for p in range(1, P+1) for s in range(1, S+1)]
	ok_schedules = [schedule for schedule in powerset(outfits) if is_ok(schedule, K)]

	return ok_schedules[-1]


for t in range(T):
	J, P, S, K = [int(x) for x in raw_input().split(' ')]
	schedule = ans(J,P,S,K)
	print("Case #{0}: {1}".format(t+1, len(schedule)))
	for day in schedule:
		print(' '.join(str(i) for i in day))

