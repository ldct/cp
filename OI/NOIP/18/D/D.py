#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

### CODE HERE

from heapq import *
from collections import defaultdict

neighbours = defaultdict(list)

N, M = read_int_tuple()
visited = [False]*(M+10)

for _ in range(M):
    u, v = read_int_tuple()
    neighbours[u] += [v]
    neighbours[v] += [u]

worklist = [1]
ret = []
visited[1] = True

while len(worklist):
    u = heappop(worklist)
    ret += [u]
    for v in neighbours[u]:
        if visited[v]: continue
        visited[v] = True
        heappush(worklist, v)

print(ret)
