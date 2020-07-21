#!/usr/bin/env pypy3

from itertools import combinations

N, K, C = input().split(' ')
N = int(N)
K = int(K)
C = int(C)

contestants = []

for _ in range(N):
	row = input().split(' ')
	row = list(map(int, row))
	contestants += [row]

def score(group):
	t = zip(*group)
	return sum(map(max, t))

scores = []
for group in combinations(contestants, K):
	scores += [score(group)]

print(sorted(scores)[::-1][C-1])
