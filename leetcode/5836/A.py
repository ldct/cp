#!/usr/bin/env pypy3

from heapq import *

def countPaths(N, roads) -> int:
    neighbours = []
    for _ in range(N):
        neighbours += [[]]

    for [u, v, w] in roads:
        neighbours[u] += [(v, w)]
        neighbours[v] += [(u, w)]

    distance = [float("inf")]*N
    distance[0] = 0
    num_shortest = [0]*N
    num_shortest[0] = 1

    worklist = [(0, 0)]

    while worklist:
        pl, u = heappop(worklist)
        for child, w in neighbours[u]:

            if distance[child] > distance[u] + w:
                assert(pl == distance[u])
                heappush(worklist, (distance[u]+w, child))
                distance[child] = distance[u] + w
                num_shortest[child] = num_shortest[u]
            elif distance[child] == distance[u] + w:
                num_shortest[child] += num_shortest[u]

    return num_shortest[N-1] % (10**9+7)

print(countPaths(7, [[0,6,7],[0,1,2],[1,2,3],[1,3,3],[6,3,3],[3,5,1],[6,5,1],[2,5,1],[0,4,5],[4,6,2]]))