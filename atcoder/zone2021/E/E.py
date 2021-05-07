#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

def dijkstra(n, graph, start):
    """ Uses Dijkstra's algortihm to find the shortest path between in a graph. """
    from heapq import heappop, heappush

    dist = [float("inf")] * n
    dist[start] = 0

    queue = [(0, start)]
    while queue:
        path_len, v = heappop(queue)
        if path_len != dist[v]: continue

        for w, edge_len in graph[v]:
            candidate = path_len + edge_len
            if candidate < dist[w]:
                dist[w] = candidate
                heappush(queue, (candidate, w))

    return dist

def ans(R, C, A, B):
    def cell_id(x, y):
        assert(0 <= x < R)
        assert(0 <= y < C)
        return x*C + y

    def shadow_id(x, y):
        return R*C + cell_id(x, y)

    neighbours = []

    for i in range(2*R*C):
        neighbours += [[]]

    for r in range(R):
        for c in range(C):
            neighbours[cell_id(r, c)] += [(shadow_id(r, c), 1)]
            neighbours[shadow_id(r, c)] += [(cell_id(r, c), 0)]

            if r-1 >= 0: neighbours[shadow_id(r, c)] += [(shadow_id(r-1, c), 1)]

    for r in range(R):
        for c in range(C):
            u = cell_id(r, c)
            if c+1 < C: neighbours[u] += [(cell_id(r, c+1), A[r][c])]
            if c-1 >= 0: neighbours[u] += [(cell_id(r, c-1), A[r][c-1])]
            if r+1 < R: neighbours[u] += [(cell_id(r+1, c), B[r][c])]

    dists = dijkstra(2*R*C, neighbours, cell_id(0, 0))

    return dists[cell_id(R-1, C-1)]

R, C = read_int_tuple()
A = []
B = []
for _ in range(R):
    A += [read_int_list()]
for _ in range(R):
    B += [read_int_list()]

print(ans(R, C, A, B))