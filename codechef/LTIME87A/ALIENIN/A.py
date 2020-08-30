#!/usr/bin/env pypy3

from heapq import heapify, heappush, heappop
from sys import stdin, stdout
 
def input():
    return stdin.readline().strip()

def ans(D, C):

	import random
	C = [random.randint(1, 10**9) for _ in range(10000)]

	# priorities:
	# - 0: recharged
	# - 1: expires
	# - 2: incoming

	events = []
	for c in C:
		events += [(c, 2, "incoming")]
		events += [(c+D, 1, "expire")]

	def ok(recharge_time):
		worklist = events[:]
		heapify(worklist)
		ready = True

		tokill = 0
		killed_not_expired = 0
		
		while len(worklist):
			[t, _, kind] = heappop(worklist)

			# print(t, kind, ready, tokill)

			if kind == "incoming":
				if ready:
					# kill
					killed_not_expired += 1
					ready = False
					heappush(worklist, (t + recharge_time, 0, "recharge"))
				else:
					tokill += 1
			elif kind == "recharge":
				ready = True
				if tokill > 0:
					# kill
					killed_not_expired += 1
					ready = False
					heappush(worklist, (t + recharge_time, 0, "recharge"))
					tokill -= 1
			else:
				assert(kind == "expire")
				killed_not_expired -= 1
				if killed_not_expired < 0:
					return False

		return True

	low = 1e-7
	high = 1e9

	assert(ok(low))
	assert(not ok(high))
	assert(low < high)

	EPS = 1e-7
	count = 0
	while high - low > EPS: # 60 iterations
		mid = (low + high) / 2
		if ok(mid):
			low = mid
		else:
			high = mid
			
	return (low + high) / 2

	return ok(2.01)

T = int(input())
for t in range(T):
	N, D = input().split()
	D = int(D)
	C = list(map(int, input().split()))
	print(ans(D, C))