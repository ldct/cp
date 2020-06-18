#!/usr/bin/env pypy3

from types import GeneratorType
from sys import stdin, stdout
import math

def input(): 
    return stdin.readline().strip()

def bootstrap(f, stack=[]):
    def wrappedfunc(*args, **kwargs):
        if stack:
            return f(*args, **kwargs)
        else:
            to = f(*args, **kwargs)
            while True:
                if type(to) is GeneratorType:
                    stack.append(to)
                    to = next(to)
                else:
                    stack.pop()
                    if not stack:
                        break
                    to = stack[-1].send(to)
            return to
    return wrappedfunc

class Graph:

    WHITE = 0
    GREY = 1
    BLACK = 2
    
    def __init__(self, N):
        self.N = N
        self.colours = dict()
        self.neighbours = dict()

        for v in range(1, N+1):
            self.neighbours[v] = set()
            self.colours[v] = Graph.WHITE

    @classmethod
    def line(self, N):
        g = Graph(N)
        for i in range(1, N):
            g.add_edge(i,i+1)
        return g

    def add_edge(self, u, v):
        self.neighbours[u].add(v)
        self.neighbours[v].add(u)

    def uncontractable_cycle(self):
        self.levels = dict()
        self.parent_of = dict()

        for v in range(1, self.N+1):
            if self.colours[v] == Graph.WHITE:
                r = self._uncontractable_cycle(v, v, 0)
                if r is not None: return r

        return None
        
    @bootstrap
    def _uncontractable_cycle(self, parent, u, level):
        self.levels[u] = level
        self.colours[u] = Graph.GREY
        self.parent_of[u] = parent

        back_edges = []
        
        for v in self.neighbours[u]:
            if v == parent: continue
            if self.colours[v] == Graph.GREY:
                back_edges += [(self.levels[u] - self.levels[v], (u, v))]

        if len(back_edges):
            (_, (u, v)) = sorted(back_edges)[0]
            cycle = [u]

            while True:
                if cycle[-1] == v: break
                cycle += [self.parent_of[cycle[-1]]]

            yield cycle
            return 

        for v in self.neighbours[u]:
            if v == parent: continue
            if self.colours[v] == Graph.WHITE:
                r = yield self._uncontractable_cycle(u, v, level+1)
                if r is not None:
                    yield r
            else:
                continue

        self.colours[u] = Graph.BLACK

        yield None

def ans(g, N, K):
    cycle = g.uncontractable_cycle()

    if cycle is not None:           
        if len(cycle) <= K:
            cycle = cycle[::-1]
            # print the cycle
            print(2)
            print(len(cycle))
            print(' '.join(map(str, cycle)))
        else:
            # print an independent set on the cycle
            IS = []
            for i, e in enumerate(cycle):
                if i % 2 == 1:
                    IS += [e]
            assert(len(IS) >= math.ceil(K / 2))
            IS = IS[0:math.ceil(K / 2)]
            print(1)
            print(' '.join(map(str, IS)))

        return

    
    is0 = []
    is1 = []

    for i in range(1, N+1):
        if g.levels[i] % 2 == 0:
            is0 += [i]
        else:
            is1 += [i]

    if len(is0) >= math.ceil(K / 2):
        IS = is0
    else:
        # assert(len(is1) >= math.ceil(K / 2))
        IS = is1

    IS = IS[0:math.ceil(K / 2)]
    print(1)
    print(' '.join(map(str, IS)))

N, M, K = input().split(' ')
N = int(N)
M = int(M)
K = int(K)

g = Graph(N)

for _ in range(M):
    u, v = input().split(' ')
    u = int(u)
    v = int(v)
    g.add_edge(u, v)

ans(g, N, K)
