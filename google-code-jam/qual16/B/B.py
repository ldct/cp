#!/usr/bin/env python3

import queue, random

def is_all_happy(pancakes):
	for p in pancakes:
		if p == '-': return False
	return True

def flipped(t, pancakes):
	# return the stack with the top i pancakes flipped

	ps = list(pancakes)

	top = ps[0:t]
	ps[0:t] = top[::-1]

	for i in range(t):
		ps[i] = '+' if ps[i] == '-' else '-'

	return ''.join(ps)

def min_flips(pancakes): # BFS

	q = queue.PriorityQueue()

	q.put((0, pancakes))

	while True:
		distance, pancakes = q.get()

		if is_all_happy(pancakes): return distance

		for i in range(1, len(pancakes) + 1):
			x = (distance+1, flipped(i, pancakes))
			q.put(x)

def min_flips_g(pancakes): # greedy?
	if is_all_happy(pancakes): return 0

	if pancakes[-1] == '+': return min_flips_g(pancakes[0:-1])

	assert(pancakes[-1] == '-')

	if pancakes[0] == '-':
		pancakes = flipped(len(pancakes), pancakes)
		return 1 + min_flips_g(pancakes)
	else:

		i = 0
		while True:
			if pancakes[i] == '-': break
			i += 1

		pancakes = flipped(i, pancakes)
		pancakes = flipped(len(pancakes), pancakes)
		return 2 + min_flips_g(pancakes)

def random_pancake(l):
	return ''.join(random.choice('+-') for _ in range(l))

# for _ in range(100):
# 	p = random_pancake(100)
# 	print(p, min_flips_g(p))

T = int(input())

for t in range(T):
	S = input()
	print("Case #{0}: {1}".format(t+1, min_flips_g(S)))
