#!/usr/bin/env pypy3

from sys import stdin, stdout

def input():
    return stdin.readline().strip()

def split_pred(arr, pred):
	ret = []
	lazy = []

	for a in arr:
		if pred(a):
			if len(lazy):
				ret += [lazy]
			lazy = []
		else:
			lazy += [a]

	if len(lazy):
		ret += [lazy]

	return ret

def colour(r, c):
	r %= 2
	c %= 2
	if r == c:
		return 1
	else:
		return -1

def ok(run):
	if len(run) == 0: return True # should never happen
	c0, r0 = min(run)
	run = [(c-c0, r) for c, r in run]

	if len(run) % 2 == 1:
		return False

	for i in range(len(run) // 2):
		x, y = run[2*i]
		xx, yy = run[2*i + 1]

		sc = colour(x, y) + colour(xx, yy)

		if sc != 0:
			return False

	return True

def ans(N, blocked):

	blocked_top = []
	blocked_bottom = []

	for r, c in blocked:
		if r == 1:
			blocked_top += [c]
		else:
			blocked_bottom += [c]

	pillars = set(blocked_top) & set(blocked_bottom)

	blocked = sorted([(c, r) for (r, c) in blocked])

	blocked = split_pred(blocked, lambda cr: cr[0] in pillars)

	for run in blocked:
		if not ok(run):
			return "NO"

	return "YES"


for _ in range(int(input())):
	input()
	[N, M] = list(map(int, input().split()))
	blocked = []
	for _ in range(M):
		[x, y] = list(map(int, input().split()))
		x -= 1
		y -= 1
		blocked += [(x, y)]
	print(ans(N, blocked))