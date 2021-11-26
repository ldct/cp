#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

from collections import defaultdict

def bfs(N, start, neighbours):
    INF = 10*N
    dist = [INF]*(N+1)
    for s in start:
        dist[s] = 0
    worklist = start[:]
    while True:
        next_worklist = []
        for u in worklist:
            for v in neighbours[u]:
                if dist[v] < INF: continue
                dist[v] = dist[u]+1
                next_worklist += [v]
        if len(next_worklist) == 0: break
        worklist = next_worklist
    return dist

def ans(N, X, neighbours):
    dist_green = bfs(N, [1], neighbours)
    dist_red = bfs(N, X, neighbours)
    for u in range(2, N+1):
        if len(neighbours[u]) == 1:
            if dist_green[u] < dist_red[u]:
                return "YES"

    return "NO"

for _ in range(read_int()):
    assert("" == input())
    N, K = read_int_tuple()
    neighbours = defaultdict(list)
    X = read_int_list()
    for _ in range(N-1):
        u, v = read_int_tuple()
        neighbours[u] += [v]
        neighbours[v] += [u]
    print(ans(N, X, neighbours))