#!/usr/bin/env python3

def intersects1(l, r, interval):
	(x, y) = interval
	low = max(l, x)
	high = min(r, y)

	return low <= high

def intersects2(l, r, intervals):
	for interval in intervals:
		if intersects1(l, r, interval):
			return True
	return False

def count(intervals):
	changes = []
	for (a, b) in intervals:
		changes += [(a, 1)]
		changes += [(b+1, -1)]

	changes = sorted(changes)

	num_intervals = 0
	last_pos = None

	ret = 0

	for (pos, delta) in changes:
		if num_intervals > 0:
			if last_pos == pos:
				continue	
			# print(f"counting [{last_pos}, {pos})")
			ret += (pos - last_pos)
			
		num_intervals += 1
		last_pos = pos

	return ret


def ans(n, x, lr):
	
	possible = [(x, x)]

	for (l, r) in lr:
		if intersects2(l, r, possible):
			possible += [(l, r)]

	return count(possible)

T = int(input())
for t in range(T):
	n, x, m = input().split(' ')
	n = int(n)
	x = int(x)
	m = int(m)
	lr = []
	for _ in range(m):
		l, r = input().split(' ')
		l = int(l)
		r = int(r)
		lr += [(l, r)]
	print(ans(n, x, lr))