#!/usr/bin/env pypy3

def explore(ocean, x, y, M):
	R = len(ocean)
	C = len(ocean[1])

	frontier = set([(x, y)])

	for m in M:
		if len(frontier) == 0: return frontier
		next_frontier = set()
		for x, y in frontier:
			this_next = set()
			if m == "N" or m == "?":
				this_next.add((x-1, y))
			if m == "S" or m == "?":
				this_next.add((x+1, y))
			if m == "E" or m == "?":
				this_next.add((x, y+1))
			if m == "W" or m == "?":
				this_next.add((x, y-1))
			for new_x, new_y in this_next:
				if not (0 <= new_x < R): continue
				if not (0 <= new_y < C): continue
				if ocean[new_x][new_y] == '#': continue
				next_frontier.add((new_x, new_y))
		frontier = next_frontier

	return frontier

def ans(ocean, M):
	R = len(ocean)
	C = len(ocean[1])

	frontier = set()

	for x in range(R):
		for y in range(C):
			if ocean[x][y] == "#": continue
			frontier.add((x, y))

	for m in M:
		if len(frontier) == 0: return 0
		next_frontier = set()
		for x, y in frontier:
			this_next = set()
			if m == "N" or m == "?":
				this_next.add((x-1, y))
			if m == "S" or m == "?":
				this_next.add((x+1, y))
			if m == "E" or m == "?":
				this_next.add((x, y+1))
			if m == "W" or m == "?":
				this_next.add((x, y-1))
			for new_x, new_y in this_next:
				if not (0 <= new_x < R): continue
				if not (0 <= new_y < C): continue
				if ocean[new_x][new_y] == '#': continue
				next_frontier.add((new_x, new_y))
		frontier = next_frontier

	return len(frontier)

R, C, M = input().split(' ')
R = int(R)
C = int(C)
M = int(M)

ocean = []
for _ in range(R):
	ocean += [input()]

M = input()

print(ans(ocean, M))