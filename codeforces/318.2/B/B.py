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

triplets = set()
for a, b in edges:
    mutual_neighbours = neighbours[a] & neighbours[b]
    if len(mutual_neighbours) == 0:
        continue
    best_mn = sorted((degree[n], n) for n in mutual_neighbours)[-1][1]
    triplets.add((a, b, best_mn))

def recognition(a, b, c):
    return degree[a] + degree[b] + degree[c] - 6

print(triplets)
if len(triplets) == 0:
    print(-1)
else:
    mn_d = [recognition(*triplet) for triplet in triplets]
    print(mn_d)
    print(min(mn_d))