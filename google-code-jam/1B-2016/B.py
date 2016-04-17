#!/usr/bin/env python3

T = int(input())

def printGrid(grid):
	for row in grid:
		print(' '.join(str(x) for x in row))

def ans(N, rows):

	grid = []
	for _ in range(N):
		row = [-1] * N
		grid += [row]

	printGrid(grid)

	return rows

for t in range(T):
	N = int(input())
	rows = []
	for _ in range(2*N-1):
		row = [int(x) for x in input().split(' ')]
		rows += [row]
	print("Case #{0}: {1}", ans(N, rows))