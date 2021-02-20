#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

from heapq import heappop, heappush
from collections import defaultdict

### CODE HERE

def roundup(A, M):
    if A % M == 0: return A
    A += M
    A -= (A % M)
    return A

def dijkstra(n, graph, start):
    """ Uses Dijkstra's algortihm to find the shortest path between in a graph. """
    dist = [float("inf")] * n
    dist[start] = 0

    queue = [(0, start)]
    while queue:
        path_len, v = heappop(queue)
        if path_len != dist[v]: continue

        for w, edge_len, K in graph[v]:
            candidate = roundup(path_len, K) + edge_len
            if candidate < dist[w]:
                dist[w] = candidate
                heappush(queue, (candidate, w))

    return dist

neighbours = defaultdict(list)

N, M, X, Y = read_int_tuple()
for _ in range(M):
    A, B, T, K = read_int_tuple()
    A -= 1
    B -= 1
    neighbours[A] += [(B, T, K)]
    neighbours[B] += [(A, T, K)]

dist = dijkstra(N, neighbours, X-1)
r = dist[Y-1]
if r == float("inf"): r = -1
print(r)
