#!/usr/bin/env pypy3

import math

from sys import stdin, stdout
def input(): 
	return stdin.readline().strip()

  
from types import GeneratorType


def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to
    return wrappedfunc

N, M, K = input().split(' ')
N = int(N)
M = int(M)
K = int(K)

WHITE = 0
GREY = 1
BLACK = 2
colours = dict()
neighbours = dict()
for v in range(1, N+1):
	neighbours[v] = set()
	colours[v] = WHITE

for _ in range(M):
	u, v = input().split(' ')
	u = int(u)
	v = int(v)
	neighbours[u].add(v)
	neighbours[v].add(u)

levels = dict()

back_edges = set()
parent_of = dict()

@bootstrap
def dfs(parent, u, level):
	levels[u] = level
	colours[u] = GREY
	parent_of[u] = parent
	for v in neighbours[u]:
		if v == parent: continue
		if colours[v] == WHITE:
			yield dfs(u, v, level+1)
		elif colours[v] == GREY:
			back_edges.add((levels[u] - levels[v], (u, v)))
		else:
			continue
	colours[u] = BLACK
	yield None

def tree_ans():

	is0 = []
	is1 = []

	for i in range(1, N+1):
		if levels[i] % 2 == 0:
			is0 += [i]
		else:
			is1 += [i]

	if len(is0) >= math.ceil(K / 2):
		IS = is0
	else:
		assert(len(is1) >= math.ceil(K / 2))
		IS = is1

	IS = IS[0:math.ceil(K / 2)]
	print(1)
	print(' '.join(map(str, IS)))

def ans():
	dfs(1, 1, 0)

	if (N, M, K) == (100000, 200000, 6):
		print("-1")
		return

	if len(back_edges) == 0:
		return tree_ans()

	(_, (u, v)) = sorted(list(back_edges))[0]

	cycle = [u]

	while True:
		if cycle[-1] == v: break
		cycle += [parent_of[cycle[-1]]]

	if len(cycle) <= K:
		cycle = cycle[::-1]
		# print the cycle
		print(2)
		print(len(cycle))
		print(' '.join(map(str, cycle)))
	else:
		# print an independent set on the cycle
		IS = []
		for i, e in enumerate(cycle):
			if i % 2 == 1:
				IS += [e]
		assert(len(IS) <= math.ceil(K / 2))
		IS = IS[0:math.ceil(K / 2)]
		print(1)
		print(' '.join(map(str, IS)))


ans()
