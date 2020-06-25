#!/usr/bin/env python3

from collections import defaultdict

N = int(input())
points = []

for _ in range(N):
	x, y = input().split()
	x, y = int(x), int(y)
	points += [(x, y)]

def ans1(points):
	ans = 0
	for i in range(len(points)):
		for j in range(i+1, len(points)):
			X, Y = points[i]
			x, y = points[j]

			if x == X or y == Y:
				ans += 1
	return ans

def ans2(points):

	ys_of = defaultdict(list)
	xs_of = defaultdict(list)
	same_points = defaultdict(int)

	ans = 0

	for x, y in points:
		xs_of[y] += [x]
		ys_of[x] += [y]
		same_points[(x, y)] += 1

	for v in xs_of.values():
		n = len(v)
		if n < 2: continue
		ans += n * (n-1) // 2

	for v in ys_of.values():
		n = len(v)
		if n < 2: continue
		ans += n * (n-1) // 2

	for n in same_points.values():
		if n < 2: continue
		ans -= n * (n-1) // 2

	return ans

print(ans2(points))
