#!/usr/bin/env python3
import sys

from collections import defaultdict

N, M = input().split()
N = int(N)
M = int(M)

neighbours = defaultdict(set)

edges = set()

for _ in range(M):
    a, b = input().split()
    a = int(a)
    b = int(b)
    edges.add((a, b))
    neighbours[a].add(b)
    neighbours[b].add(a)

degree = {}

for node in neighbours:
    degree[node] = len(neighbours[node])

def is_clique(a, b, c):
    return knows(a, b) and knows(b, c) and knows(c, a)

def knows(a, b):
    return a in neighbours[b] and b in neighbours[a]

degrees = set()
for a in range(1, N+1):
    for b in range(1, N+1):
        for c in range(1, N+1):
            if not is_clique(a, b, c): continue
            degrees.add((degree[a] + degree[b] + degree[c], (a, b, c)))

if len(degrees) == 0:
    print(-1)
else:
    print(min(degrees))