#!/usr/bin/env pypy3

from sys import stdin, stdout

def input():
    return stdin.readline().strip()

from collections import defaultdict
from heapq import *

def ans(W, edges):
	degree = defaultdict(int)
	for u, v in edges:
		degree[u] += 1
		degree[v] += 1
	weights = []
	for i in range(len(W)):
		weights += [-W[i]]*(degree[i] - 1)

	heapify(weights)
	ret = [sum(W)]

	while len(weights):
		ret += ([ret[-1] - heappop(weights)])

	return ret

for _ in range(int(input())):
	N = int(input())
	W = list(map(int, input().split()))
	edges = []
	for _ in range(N-1):
		[u, v] = list(map(int, input().split()))
		u -= 1
		v -= 1
		edges += [(u, v)]

	print(*ans(W, edges))