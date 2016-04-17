#!/usr/bin/env python3

import math, heapq

T = int(input())

for t in range(T):

	input()
	piles = [-int(x) for x in input().split(' ')] + [0]

	heapq.heapify(piles)

	splits = 0

	while True:

		print(piles)

		t1 = -heapq.heappop(piles)
		t2 = -heapq.heappop(piles)

		# max time without doing anything is t1

		time_with_split = 1 + max(t2, math.ceil(t1 / 2))

		if time_with_split > t1:
			heapq.heappush(piles, -t1)
			heapq.heappush(piles, -t2)
			break
		else:
			splits += 1
			heapq.heappush(piles, -t2)
			heapq.heappush(piles, -math.ceil(t1 / 2))
			heapq.heappush(piles, -math.floor(t1 / 2))

	# print(piles)

	t1 = -heapq.heappop(piles)
	ans = t1 + splits

	print("Case #%d: %d + %d" % (t + 1, ans))