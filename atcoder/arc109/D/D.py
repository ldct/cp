#!/usr/bin/env python3

def l(d):
	return (d - 1) % 4

def r(d):
	return (d + 1) % 4

def f(d):
	return (d + 2) % 4

def edges(x, y, d):
	if d == 0:
		return [
			(x, y, l(d)),
			(x, y, r(d)),
			(x+1, y, l(d)),
			(x+1, y, f(d)),
			(x, y+1, r(d)),
			(x, y+1, f(d)),
			(x+1,y+1, f(d))
		]
	rr = 0
	while d != 0:
		x, y, d = y, -x, r(d)
		rr += 1

	ret = edges(x, y, d)

	while rr != 0:
		ret = [(-y, x, l(d)) for x, y, d in ret]
		rr -= 1

	return ret


frontiers = []
frontier = set([(0, 0, 3)])
visited = set(frontier)

for _ in range(10):
	frontiers += [frontier]
	next_frontier = set([])
	for (x, y, d) in frontier:
		for nx, ny, nd in edges(x, y, d):
			p = (nx, ny, nd)
			if p in visited: continue
			visited.add(p)
			next_frontier.add(p)
	frontier = next_frontier

for i, frontier in enumerate(frontiers):
	md = max(x + y for (x, y, _) in frontier)
	print(i, [(x, y, d) for (x, y, d) in frontier if x + y == md])
