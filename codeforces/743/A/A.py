#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

from collections import defaultdict
from heapq import *

### CODE HERE

class DigraphSources:
    def __init__(self, N):
        self.out_neighbours = defaultdict(list)
        self.in_degree = defaultdict(int)
        self.sources = set(range(N))

    def add_edge(self, u, v):
        # print("edge", u, v)
        self.out_neighbours[u] += [v]
        self.in_degree[v] += 1
        self.recompute(v)

    def recompute(self, v):
        if self.in_degree[v] == 0:
            self.sources.add(v)
            return v
        elif v in self.sources:
            self.sources.remove(v)

    def remove_source(self, u):
        assert(self.in_degree[u] == 0)
        self.sources.remove(u)
        ret = []
        for v in self.out_neighbours[u]:
            self.in_degree[v] -= 1
            r = self.recompute(v)
            if r is not None:
                ret += [r]
        return ret

def ans(N, dependencies):
    dependencies = [[x-1 for x in a] for a in dependencies]

    graph = DigraphSources(N)

    for u in range(N):
        for v in dependencies[u]:
            graph.add_edge(v, u)

    ret = 0
    num_removed = 0
    while True:
        if num_removed == N: return ret
        sources = list(graph.sources)
        if len(sources) == 0: return -1

        ret += 1

        heapify(sources)

        while len(sources):
            u = heappop(sources)
            r = graph.remove_source(u)
            if len(r):
                for v in r:
                    if v > u:
                        heappush(sources, v)
            num_removed += 1


    return graph.sources, graph.in_degree

for _ in range(read_int()):
    N = read_int()
    dependencies = [read_int_list()[1:] for _ in range(N)]
    print(ans(N, dependencies))
