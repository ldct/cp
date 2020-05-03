#!/usr/bin/env python3

T = int(input())

def solution(x, y, m):
	max_size = 0

	N = len(m)
	possible_positions = set([(x,y)])
	for i in range(N+1):
		if (0,0) in possible_positions: 
			# print("max size=", max_size)
			return i
		if i == N: 
			# print("max size=", max_size)
			return None

		if m[i] == 'N':
			possible_positions = set((x,y+1) for (x,y) in possible_positions)
		elif m[i] == 'S':
			possible_positions = set((x,y-1) for (x,y) in possible_positions)
		elif m[i] == 'E':
			possible_positions = set((x+1,y) for (x,y) in possible_positions)
		elif m[i] == 'W':
			possible_positions = set((x-1,y) for (x,y) in possible_positions)
		next_positions = set()
		for (x,y) in possible_positions:
			if max(abs(x), abs(y)) <= 2:
				next_positions.add((x,y))
			if x > 0 and abs(x) >= abs(y):
				next_positions.add((x-1,y))
			if x < 0 and abs(x) >= abs(y):
				next_positions.add((x+1,y))
			if y > 0 and abs(y) >= abs(x):
				next_positions.add((x,y-1))
			if y < 0 and abs(y) >= abs(x):
				next_positions.add((x,y+1))	
		possible_positions = next_positions
		max_size = max(len(possible_positions), max_size)

	return None



for t in range(T):
	[x, y, m] = input().split(' ')
	x = int(x)
	y = int(y)

	sol = solution(x,y,m)
	if sol is None:
		sol = "IMPOSSIBLE"
	else:
		sol = str(sol)

	print("Case #" + str(t+1) + ": " + sol)
