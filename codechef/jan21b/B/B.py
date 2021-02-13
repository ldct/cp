#!/usr/bin/env pypy3

from sys import stdin, stdout

def input():
    return stdin.readline().strip()

# returns True iff some subset of B can be added to some number in [target_low, target_high]
def ss(target_low, target_high, B):

	if not (target_low <= target_high): return False

	import array
	possible = array.array('b', [1] + [0]*target_low)

	for b in B:
		next_possible = array.array('b', possible)
		for i in range(len(possible)):
			if possible[i] != 1: continue
			if i + b > target_high: continue
			if target_low <= i + b <= target_high:
				return True
			if i + b < target_low:
				next_possible[i+b] = 1
		possible = next_possible

	return False

def ans(H, K):
	H = sorted(H)[::-1]
	if len(H) < 2: return -1
	if H[0] >= K and H[1] >= K: return 2
	if H[0] >= K:
		ret = 1
		rest = K
		for i in range(1, len(H)):
			rest -= H[i]
			ret += 1
			if rest <= 0:
				return ret
		return -1

	for h in H:
		if not (h < K): return -1

	def ok(i):
		useable = H[:i]

		if len(useable) < 2: return False

		return ss(K, sum(useable) - K, useable)

	low = 0
	high = len(H)

	if not ok(high): return -1

	if ok(low): return -1
	if not ok(high): return -1

	while high - low > 3:
		mid = (low + high) // 2
		if ok(mid):
			high = mid
		else:
			low = mid

	for i in range(low, low+10):
		if ok(i):
			return i

	return -1

def read_line():
	return list(map(int, input().split()))

def read_int():
	return int(input())

for _ in range(int(input())):
	[N, K] = read_line()
	H = read_line()
	print(ans(H, K))
