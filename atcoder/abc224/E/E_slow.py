#!/usr/bin/env pypy3

from sys import stdin, stdout

def input(): return stdin.readline().strip()
def read_int_list(): return list(map(int, input().split()))
def read_int_tuple(): return tuple(map(int, input().split()))
def read_int(): return int(input())

from copy import copy
from collections import defaultdict

class DigraphSources:
    def __init__(self):
        self.out_neighbours = defaultdict(list)
        self.in_degree = defaultdict(int)
        self.sources = set()
        self.nodes = set()

    def add_node(self, u):
        self.sources.add(u)
        self.nodes.add(u)

    def add_edge(self, u, v):
        # assert(u in self.nodes)
        # assert(v in self.nodes)
        # print(f"{u} -> {v}")
        self.out_neighbours[u] += [v]
        self.in_degree[v] += 1
        self.recompute(v)

    def recompute(self, v):
        return
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

    def copy(self):
        ret = DigraphSources()
        ret.out_neighbours = copy(self.out_neighbours)
        ret.in_degree = copy(self.in_degree)
        ret.sources = copy(self.sources)
        ret.nodes = copy(self.nodes)
        return ret

    def toposort(self):
        g = self.copy()
        n = len(g.nodes)
        ret = []
        while len(g.sources):
            S = set(g.sources)
            for s in S:
                ret += [s]
                g.remove_source(s)
                n -= 1
        assert(n == 0, "not a DAG")
        return ret

    def longest_paths(self):
        ts = self.toposort()
        ts.reverse()

        ret = defaultdict(int)
        for u in ts:
            for v in self.out_neighbours[u]:
                ret[u] = max(ret[u], 1 + ret[v])
        return ret

### CODE HERE

H, W, N = read_int_list()

cols = defaultdict(list)
rows = defaultdict(list)
int_of = defaultdict(int)

graph = DigraphSources()

nodes = []
grid = []
for _ in range(N):
    grid += [read_int_tuple()]

for x, y, n in grid:
    nodes += [(x, y)]
    graph.add_node((x, y))
    graph.add_node((x, y))
    cols[x] += [(x, y, n)]
    rows[y] += [(x, y, n)]

import sys
sys.exit(0)

def group(vals):
    d = defaultdict(list)
    for k, v in vals:
        d[k] += [v]
    ret = []
    for k in d:
        ret += [(k, d[k])]
    ret.sort()
    return ret

_gensym_counter = -1
def gensym():
    global _gensym_counter
    _gensym_counter += 1
    return _gensym_counter

for x in cols:
    lst = cols[x]
    vals = [(n, (x, y)) for x, y, n in lst]
    vals = group(vals)
    for j in range(len(vals)-1):
        u, v = vals[j], vals[j+1]
        r = gensym()
        graph.add_node(r)
        for p in u[1]:
            graph.add_edge(p, r)
        for q in v[1]:
            graph.add_edge(r, q)

for y in rows:
    lst = rows[y]
    vals = [(n, (x, y)) for x, y, n in lst]
    vals = group(vals)
    for j in range(len(vals)-1):
        u, v = vals[j], vals[j+1]
        r = gensym()
        graph.add_node(r)
        for p in u[1]:
            graph.add_edge(p, r)
        for q in v[1]:
            graph.add_edge(r, q)

# r = graph.longest_paths()
# for u in nodes:
#     print(r[u] // 2)