#!/usr/bin/env python3

T = int(input())

memo = {}

def fillable(empty_points, current_block, block_size):

	args = (empty_points, current_block, block_size)

	if args in memo:
		return memo[args]

	if len(current_block) == block_size:
		memo[args] = fillable(empty_points - current_block, frozenset(), block_size)
		return memo[args]

	if len(empty_points) == 0 and len(current_block) == 0:
		return True

	if len(empty_points) == 0 and len(current_block) > 0:
		return False

	if len(current_block) == 0:
		for p in empty_points:
			if fillable(empty_points - frozenset([p]), current_block | frozenset([p]), block_size):
				memo[args] = True
				return True

	for x, y in current_block:
		neighbours = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
		for neighbour in neighbours:
			if neighbour in empty_points and fillable(empty_points - frozenset([neighbour]), current_block | set([neighbour]), block_size):
				memo[args] = True
				return True

	memo[args] = False
	return False

def can_richard_win(empty_points, current_block, block_size):
	if len(current_block) == block_size:
		return not fillable(empty_points, current_block, block_size)

	for x, y in current_block:
		neighbours = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
		for neighbour in neighbours:
			if neighbour in empty_points and can_richard_win(empty_points - frozenset([neighbour]), current_block | set([neighbour]), block_size):
				return True

	return False


def make_empty_board(R, C):
	board = set()

	for i in range(R):
		for j in range(C):
			board.add((i, j))

	return frozenset(board)

print(fillable(make_empty_board(4, 4), frozenset(), 13))

for t in range(T):

	X, R, C = input().split(' ')

	X = int(X)
	R = int(R)
	C = int(C)

	print(can_richard_win(make_empty_board(R, C), frozenset(), X))

	# print(X, R, C)