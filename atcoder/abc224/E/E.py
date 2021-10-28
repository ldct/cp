#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

# sinks means outdegree 0
class DigraphSinks:
    def __init__(self):
        self.in_neighbours = defaultdict(list)
        self.out_degree = defaultdict(int)

    def add_edge(self, u, v):
        self.in_neighbours[v] += [u]
        self.out_degree[u] += 1
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
### CODE HERE

for _ in range(read_int()):
    pass